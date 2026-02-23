#!/usr/bin/env python3
"""Integration tests for the Provider Items resource."""

from __future__ import annotations

import asyncio
import io
import time
from typing import Any

import httpx

from scripts.common import create_client, get_base_parser
from scripts.test_utils import TestRunner


def resolve_url(url: str, base_url: str) -> str:
    """Resolve URL by prepending base URL if it's a relative path (proxy URL)."""
    if not url:
        return url
    if url.startswith("http://") or url.startswith("https://"):
        return url
    base = base_url.rstrip("/")
    path = url if url.startswith("/") else f"/{url}"
    return f"{base}{path}"


def get_name_from_key(key: str) -> str:
    """Extract the item name from a key path."""
    return key.rstrip("/").split("/")[-1]


async def main() -> None:
    parser = get_base_parser("Test Provider Items resource")
    parser.add_argument(
        "--provider-id",
        type=str,
        default=None,
        help="ID of the provider to use (default: first available)",
    )
    args = parser.parse_args()

    client = create_client(args)
    runner = TestRunner(resource="provider_items", api_url=args.api_url)

    timestamp = int(time.time())
    test_folder_name = f"SDK-TEST-{timestamp}"
    test_file_name = "test-file.txt"
    test_file_content = f"Test content created at {timestamp}".encode()
    presigned_file_name = "presigned-upload.txt"
    presigned_file_content = f"Presigned upload content {timestamp}".encode()

    provider_id: str | None = None
    folder_created = False
    file_uploaded = False
    renamed_file_name: str | None = None
    renamed_folder_name: str | None = None
    actual_file_key: str | None = None
    actual_folder_key: str | None = None
    folder_rename_succeeded = False
    presigned_file_uploaded = False
    presigned_upload_supported = True

    async with client:
        # Setup: Get provider ID (from CLI or first available)
        async def test_setup() -> dict[str, Any]:
            nonlocal provider_id
            if args.provider_id:
                provider_id = args.provider_id
                return {"provider_id": provider_id, "source": "cli"}
            result = await client.providers.list(page=0, page_size=1)
            if result.data and len(result.data) > 0:
                provider = result.data[0]
                provider_id = str(provider.id.id) if provider.id else None
                return {"provider_id": provider_id, "provider_name": provider.name}
            raise AssertionError("No providers available for testing")

        await runner.run_test(
            name="setup_get_provider",
            test_fn=test_setup,
            expected_message="Found provider for items testing",
        )

        if not provider_id:
            runner.skip_test("all_remaining", "No provider available")
            runner.print_and_save()
            return  
                  
        # Test 1: List items at root
        async def test_list_root() -> dict[str, Any]:
            result = await client.items.list(provider_id, key="")  # type: ignore[arg-type]
            return {
                "items_count": len(result.items) if result.items else 0,
                "has_next": result.next_cursor is not None,
            }

        await runner.run_test(
            name="list_root",
            test_fn=test_list_root,
            expected_message="Listed items at root",
        )

        # Test 2: Create folder
        async def test_create_folder() -> dict[str, Any]:
            nonlocal folder_created
            result = await client.items.create_folder(
                provider_id,  # type: ignore[arg-type]
                key=f"{test_folder_name}/",
            )
            folder_created = True
            return {
                "folder_created": test_folder_name,
                "folder_key": result.key,
            }

        await runner.run_test(
            name="create_folder",
            test_fn=test_create_folder,
            expected_message=f"Created folder {test_folder_name}",
        )

        # Test 3: Verify folder can be listed (go into the folder)
        async def test_verify_folder_accessible() -> dict[str, Any]:
            result = await client.items.list(provider_id, key=f"{test_folder_name}/")  # type: ignore[arg-type]
            return {
                "folder_accessible": True,
                "folder_path": f"{test_folder_name}/",
                "items_in_folder": len(result.items) if result.items else 0,
            }

        await runner.run_test(
            name="verify_folder_accessible",
            test_fn=test_verify_folder_accessible,
            expected_message="Folder is accessible",
        )

        # Test 4: Upload file directly (multipart)
        async def test_upload_direct() -> dict[str, Any]:
            nonlocal file_uploaded
            file_obj = io.BytesIO(test_file_content)
            result = await client.items.upload(
                provider_id,  # type: ignore[arg-type]
                key=f"{test_folder_name}/",
                file=file_obj,
                file_name=test_file_name,
                mime_type="text/plain",
            )
            file_uploaded = True
            return {
                "file_key": result.key,
                "file_type": result.type,
            }

        await runner.run_test(
            name="upload_direct",
            test_fn=test_upload_direct,
            expected_message=f"Uploaded file {test_file_name}",
        )

        # Test 5: Verify file exists in listing
        async def test_verify_file_exists() -> dict[str, Any]:
            result = await client.items.list(provider_id, key=f"{test_folder_name}/")  # type: ignore[arg-type]
            file_found = False
            if result.items:
                for item in result.items:
                    if item.key and item.key.endswith(test_file_name) and item.type == "FILE":
                        file_found = True
                        break
            assert file_found, f"File {test_file_name} not found in listing"
            return {"file_found": file_found, "file_name": test_file_name}

        await runner.run_test(
            name="verify_file_exists",
            test_fn=test_verify_file_exists,
            expected_message="Uploaded file appears in listing",
        )

        # Test 6: Rename file
        async def test_rename_file() -> dict[str, Any]:
            nonlocal renamed_file_name, actual_file_key
            renamed_file_name = f"renamed-{test_file_name}"
            result = await client.items.rename(
                provider_id,  # type: ignore[arg-type]
                key=f"{test_folder_name}/{test_file_name}",
                new_name=renamed_file_name,
            )
            actual_file_key = result.key
            return {
                "old_name": test_file_name,
                "new_name": get_name_from_key(result.key) if result.key else None,
                "actual_key": result.key,
                "type": result.type,
            }

        await runner.run_test(
            name="rename_file",
            test_fn=test_rename_file,
            expected_message="File renamed successfully",
        )

        # Test 7: Rename folder
        async def test_rename_folder() -> dict[str, Any]:
            nonlocal renamed_folder_name, folder_rename_succeeded, actual_folder_key
            renamed_folder_name = f"{test_folder_name}-RENAMED"
            result = await client.items.rename(
                provider_id,  # type: ignore[arg-type]
                key=f"{test_folder_name}/",
                new_name=renamed_folder_name,
            )
            folder_rename_succeeded = True
            actual_folder_key = result.key
            expected_key = f"{renamed_folder_name}/"
            if result.key != expected_key:
                print(f"Warning: Expected key '{expected_key}', got '{result.key}'")
            return {
                "old_name": test_folder_name,
                "new_name": get_name_from_key(result.key) if result.key else None,
                "actual_key": result.key,
                "expected_key": expected_key,
                "type": result.type,
            }

        await runner.run_test(
            name="rename_folder",
            test_fn=test_rename_folder,
            expected_message="Folder renamed successfully",
        )

        # Use actual folder key from rename result, falling back to expected path
        if folder_rename_succeeded and actual_folder_key:
            current_folder_key = actual_folder_key.rstrip("/")
        else:
            current_folder_key = test_folder_name

        # Test 8: Get download URL
        download_url: str | None = None

        async def test_get_download_url() -> dict[str, Any]:
            nonlocal download_url
            file_key = f"{current_folder_key}/{renamed_file_name}"
            result = await client.items.get_download_url(
                provider_id,  # type: ignore[arg-type]
                key=file_key,
            )
            raw_url = result.url
            assert raw_url, "Download URL should not be empty"
            download_url = resolve_url(raw_url, args.api_url)
            is_proxy = raw_url != download_url
            return {
                "file_key": file_key,
                "url_present": bool(download_url),
                "is_proxy_url": is_proxy,
                "resolved_url": download_url[:80] + "..." if len(download_url) > 80 else download_url,
            }

        await runner.run_test(
            name="get_download_url",
            test_fn=test_get_download_url,
            expected_message="Got presigned download URL",
        )

        # Test 9: Actually download file via presigned URL
        async def test_download_via_url() -> dict[str, Any]:
            assert download_url, "Download URL not available"
            is_direct_url = download_url.startswith(("http://", "https://")) and args.api_url not in download_url
            headers = {} if is_direct_url else {"Authorization": f"Bearer {args.token}"}
            async with httpx.AsyncClient() as http:
                resp = await http.get(download_url, headers=headers)
                assert resp.status_code == 200, f"Download failed: {resp.status_code}"
                content = resp.content
                assert content == test_file_content, "Downloaded content doesn't match"
            return {
                "status_code": resp.status_code,
                "content_length": len(content),
                "content_matches": content == test_file_content,
            }

        await runner.run_test(
            name="download_via_url",
            test_fn=test_download_via_url,
            expected_message="Downloaded file via presigned URL",
        )

        # Test 10: Get upload URL for presigned upload (may not be supported by all providers)
        upload_url: str | None = None

        async def test_get_upload_url() -> dict[str, Any]:
            nonlocal upload_url, presigned_upload_supported
            file_key = f"{current_folder_key}/{presigned_file_name}"
            result = await client.items.get_upload_url(
                provider_id,  # type: ignore[arg-type]
                key=file_key,
                size=len(presigned_file_content),
                media_type="text/plain",
            )
            raw_url = result.url
            if not raw_url:
                presigned_upload_supported = False
                return {
                    "file_key": file_key,
                    "presigned_supported": False,
                    "note": "Provider does not support presigned uploads",
                }
            upload_url = resolve_url(raw_url, args.api_url)
            is_proxy = raw_url != upload_url
            return {
                "file_key": file_key,
                "presigned_supported": True,
                "is_proxy_url": is_proxy,
                "resolved_url": upload_url[:80] + "..." if len(upload_url) > 80 else upload_url,
            }

        await runner.run_test(
            name="get_upload_url",
            test_fn=test_get_upload_url,
            expected_message="Got presigned upload URL",
        )

        # Test 11-14: Presigned upload flow (skip if not supported)
        if presigned_upload_supported and upload_url:
            async def test_upload_via_presigned() -> dict[str, Any]:
                nonlocal presigned_file_uploaded
                is_direct_url = upload_url.startswith(("http://", "https://"))  # type: ignore[union-attr]
                headers: dict[str, str] = {"Content-Type": "text/plain"}
                if is_direct_url:
                    headers["x-ms-blob-type"] = "BlockBlob"
                else:
                    headers["Authorization"] = f"Bearer {args.token}"
                async with httpx.AsyncClient() as http:
                    resp = await http.put(
                        upload_url,  # type: ignore[arg-type]
                        content=presigned_file_content,
                        headers=headers,
                    )
                    assert resp.status_code in (200, 201), f"Upload failed: {resp.status_code}"
                presigned_file_uploaded = True
                return {
                    "status_code": resp.status_code,
                    "bytes_uploaded": len(presigned_file_content),
                }

            await runner.run_test(
                name="upload_via_presigned",
                test_fn=test_upload_via_presigned,
                expected_message="Uploaded file via presigned URL",
            )

            async def test_confirm_upload() -> dict[str, Any]:
                file_key = f"{current_folder_key}/{presigned_file_name}"
                result = await client.items.confirm_upload(
                    provider_id,  # type: ignore[arg-type]
                    key=file_key,
                )
                assert result.key and result.key.endswith(presigned_file_name), "Confirmed file key mismatch"
                return {
                    "file_key": result.key,
                    "file_type": result.type,
                }

            await runner.run_test(
                name="confirm_upload",
                test_fn=test_confirm_upload,
                expected_message="Confirmed presigned upload",
            )

            async def test_verify_presigned_upload() -> dict[str, Any]:
                file_key = f"{current_folder_key}/{presigned_file_name}"
                result = await client.items.get_download_url(
                    provider_id,  # type: ignore[arg-type]
                    key=file_key,
                )
                assert result.url, "Download URL should not be empty"
                resolved = resolve_url(result.url, args.api_url)
                is_direct_url = resolved.startswith(("http://", "https://")) and args.api_url not in resolved
                dl_headers = {} if is_direct_url else {"Authorization": f"Bearer {args.token}"}
                async with httpx.AsyncClient() as http:
                    resp = await http.get(resolved, headers=dl_headers)
                    assert resp.status_code == 200, f"Download failed: {resp.status_code}"
                    assert resp.content == presigned_file_content, "Content mismatch"
                return {
                    "content_matches": resp.content == presigned_file_content,
                    "content_length": len(resp.content),
                }

            await runner.run_test(
                name="verify_presigned_upload",
                test_fn=test_verify_presigned_upload,
                expected_message="Verified presigned upload content",
            )

            async def test_delete_presigned_file() -> dict[str, Any]:
                await client.items.delete(
                    provider_id,  # type: ignore[arg-type]
                    key=f"{current_folder_key}/{presigned_file_name}",
                )
                return {"deleted_file": presigned_file_name}

            await runner.run_test(
                name="delete_presigned_file",
                test_fn=test_delete_presigned_file,
                expected_message="Deleted presigned uploaded file",
            )
        else:
            runner.skip_test("upload_via_presigned", "Presigned uploads not supported by this provider")
            runner.skip_test("confirm_upload", "Presigned uploads not supported by this provider")
            runner.skip_test("verify_presigned_upload", "Presigned uploads not supported by this provider")
            runner.skip_test("delete_presigned_file", "Presigned uploads not supported by this provider")

        # Test 15: Delete renamed file
        async def test_delete_file() -> dict[str, Any]:
            await client.items.delete(
                provider_id,  # type: ignore[arg-type]
                key=f"{current_folder_key}/{renamed_file_name}",
            )
            return {"deleted_file": renamed_file_name}

        await runner.run_test(
            name="delete_file",
            test_fn=test_delete_file,
            expected_message="Deleted test file",
        )

        # Test 16: Delete folder
        async def test_delete_folder() -> dict[str, Any]:
            await client.items.delete(
                provider_id,  # type: ignore[arg-type]
                key=f"{current_folder_key}/",
            )
            return {"deleted_folder": current_folder_key}

        await runner.run_test(
            name="delete_folder",
            test_fn=test_delete_folder,
            expected_message="Deleted test folder",
        )

        # Test 17: Verify folder is deleted
        async def test_verify_folder_deleted() -> dict[str, Any]:
            result = await client.items.list(provider_id, key="")  # type: ignore[arg-type]
            folder_found = False
            if result.items:
                for item in result.items:
                    if item.key and current_folder_key in item.key:
                        folder_found = True
                        break
            assert not folder_found, f"Folder {current_folder_key} still exists"
            return {"folder_deleted": True, "folder_name": current_folder_key}

        await runner.run_test(
            name="verify_folder_deleted",
            test_fn=test_verify_folder_deleted,
            expected_message="Verified folder is deleted",
        )

        # Test 18: Rename non-existent file (should raise error)
        async def test_error_rename_nonexistent() -> dict[str, Any]:
            from biolevate import APIError, NotFoundError

            try:
                await client.items.rename(
                    provider_id,  # type: ignore[arg-type]
                    key="non-existent-file-xyz.txt",
                    new_name="new-name.txt",
                )
                raise AssertionError("Expected error was not raised")
            except NotFoundError:
                return {"error_type": "NotFoundError", "correctly_raised": True}
            except APIError as e:
                return {"error_type": "APIError", "status": e.status_code, "correctly_raised": True}

        await runner.run_test(
            name="error_rename_nonexistent",
            test_fn=test_error_rename_nonexistent,
            expected_message="Error raised for non-existent file rename",
        )

        # Test 19: Get non-existent provider (should raise NotFoundError)
        async def test_not_found_provider() -> dict[str, Any]:
            from biolevate import NotFoundError

            try:
                await client.items.list(
                    "00000000-0000-0000-0000-000000000000",
                    key="",
                )
                raise AssertionError("Expected NotFoundError was not raised")
            except NotFoundError:
                return {"error_type": "NotFoundError", "correctly_raised": True}

        await runner.run_test(
            name="not_found_provider",
            test_fn=test_not_found_provider,
            expected_message="NotFoundError raised for non-existent provider",
        )

    runner.print_and_save()


if __name__ == "__main__":
    asyncio.run(main())
