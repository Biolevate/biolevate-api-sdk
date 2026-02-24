"""Test utilities with report generation for integration tests."""

from __future__ import annotations

import json
import time
import traceback
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, TypeVar

T = TypeVar("T")


class TestStatus(Enum):
    PASSED = "PASSED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


@dataclass
class TestResult:
    name: str
    status: TestStatus
    duration_ms: float
    message: str = ""
    details: dict[str, Any] = field(default_factory=dict)
    error: str | None = None


@dataclass
class TestReport:
    resource: str
    timestamp: datetime
    api_url: str
    results: list[TestResult] = field(default_factory=list)

    @property
    def total(self) -> int:
        return len(self.results)

    @property
    def passed(self) -> int:
        return sum(1 for r in self.results if r.status == TestStatus.PASSED)

    @property
    def failed(self) -> int:
        return sum(1 for r in self.results if r.status == TestStatus.FAILED)

    @property
    def skipped(self) -> int:
        return sum(1 for r in self.results if r.status == TestStatus.SKIPPED)

    @property
    def total_duration_ms(self) -> float:
        return sum(r.duration_ms for r in self.results)

    def add(self, result: TestResult) -> None:
        self.results.append(result)

    def to_dict(self) -> dict[str, Any]:
        return {
            "resource": self.resource,
            "timestamp": self.timestamp.isoformat(),
            "api_url": self.api_url,
            "summary": {
                "total": self.total,
                "passed": self.passed,
                "failed": self.failed,
                "skipped": self.skipped,
                "duration_ms": round(self.total_duration_ms, 2),
            },
            "results": [
                {
                    "name": r.name,
                    "status": r.status.value,
                    "duration_ms": round(r.duration_ms, 2),
                    "message": r.message,
                    "details": r.details,
                    "error": r.error,
                }
                for r in self.results
            ],
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, default=str)

    def save(self, output_dir: Path | str = "test-reports") -> Path:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        timestamp_str = self.timestamp.strftime("%Y%m%d_%H%M%S")
        filename = f"{self.resource}_{timestamp_str}.json"
        filepath = output_path / filename

        filepath.write_text(self.to_json())
        return filepath

    def print_summary(self) -> None:
        print("\n" + "=" * 60)
        print(f"TEST REPORT: {self.resource.upper()}")
        print("=" * 60)
        print(f"Timestamp: {self.timestamp.isoformat()}")
        print(f"API URL:   {self.api_url}")
        print("-" * 60)

        for result in self.results:
            status_icon = {
                TestStatus.PASSED: "[PASS]",
                TestStatus.FAILED: "[FAIL]",
                TestStatus.SKIPPED: "[SKIP]",
            }[result.status]

            print(f"{status_icon} {result.name} ({result.duration_ms:.0f}ms)")
            if result.message:
                print(f"         {result.message}")
            if result.error:
                print(f"         Error: {result.error}")

        print("-" * 60)
        print(f"Total: {self.total} | Passed: {self.passed} | Failed: {self.failed} | Skipped: {self.skipped}")
        print(f"Duration: {self.total_duration_ms:.0f}ms")
        print("=" * 60 + "\n")


class TestRunner:
    def __init__(self, resource: str, api_url: str) -> None:
        self.report = TestReport(
            resource=resource,
            timestamp=datetime.now(),
            api_url=api_url,
        )

    async def run_test(
        self,
        name: str,
        test_fn: Callable[[], T],
        expected_message: str = "",
    ) -> TestResult:
        start_time = time.perf_counter()
        try:
            result = await test_fn()
            duration_ms = (time.perf_counter() - start_time) * 1000

            details = {}
            if hasattr(result, "to_dict"):
                details["response"] = result.to_dict()
            elif isinstance(result, dict):
                details["response"] = result

            test_result = TestResult(
                name=name,
                status=TestStatus.PASSED,
                duration_ms=duration_ms,
                message=expected_message or "OK",
                details=details,
            )
        except Exception as e:
            duration_ms = (time.perf_counter() - start_time) * 1000
            test_result = TestResult(
                name=name,
                status=TestStatus.FAILED,
                duration_ms=duration_ms,
                message=str(e),
                error=traceback.format_exc(),
            )

        self.report.add(test_result)
        return test_result

    def skip_test(self, name: str, reason: str) -> TestResult:
        test_result = TestResult(
            name=name,
            status=TestStatus.SKIPPED,
            duration_ms=0,
            message=reason,
        )
        self.report.add(test_result)
        return test_result

    def print_and_save(self, output_dir: str = "test-reports") -> Path:
        self.report.print_summary()
        filepath = self.report.save(output_dir)
        print(f"Report saved to: {filepath}")
        return filepath
