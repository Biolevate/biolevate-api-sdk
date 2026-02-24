"""Integration tests for ProviderItemsResource."""

from __future__ import annotations

import io
import time

import pytest

from biolevate import BiolevateClient

_RUN_ID = str(int(time.time()))


@pytest.mark.asyncio
class TestProviderItemsCreateFolder:
    async def test_creates_folder_successfully(
        self,
        live_client: BiolevateClient,
        provider_id: str,
        test_folder_key: str,
    ) -> None:
        subfolder_key = f"{test_folder_key}subfolder-{_RUN_ID}/"
        item = await live_client.items.create_folder(provider_id, key=subfolder_key)

        assert item is not None
        assert item.type == "FOLDER"

        await live_client.items.delete(provider_id, key=subfolder_key)


@pytest.mark.asyncio
class TestProviderItemsUpload:
    async def test_uploads_file_successfully(
        self,
        live_client: BiolevateClient,
        provider_id: str,
        test_folder_key: str,
    ) -> None:
        file_name = f"upload-test-{_RUN_ID}.txt"
        content = b"Integration test file content"

        item = await live_client.items.upload(
            provider_id,
            key=test_folder_key,
            file=io.BytesIO(content),
            file_name=file_name,
            mime_type="text/plain",
        )

        assert item is not None
        assert item.key.endswith(file_name)
        assert item.type == "FILE"

        await live_client.items.delete(provider_id, key=f"{test_folder_key}{file_name}")


@pytest.mark.asyncio
class TestProviderItemsList:
    async def test_lists_items_in_root(
        self,
        live_client: BiolevateClient,
        provider_id: str,
    ) -> None:
        result = await live_client.items.list(provider_id, key="/")

        assert result is not None
        assert result.items is not None
        assert isinstance(result.items, list)

    async def test_lists_items_in_test_folder(
        self,
        live_client: BiolevateClient,
        provider_id: str,
        test_folder_key: str,
        uploaded_item_key: str,
    ) -> None:
        result = await live_client.items.list(provider_id, key=test_folder_key)

        assert result.items is not None
        keys = [item.key for item in result.items]
        assert uploaded_item_key in keys

    async def test_returns_empty_list_for_missing_path(
        self,
        live_client: BiolevateClient,
        provider_id: str,
    ) -> None:
        result = await live_client.items.list(provider_id, key="definitely-does-not-exist-xyz/")
        assert result.items == []


@pytest.mark.asyncio
class TestProviderItemsRename:
    async def test_renames_file(
        self,
        live_client: BiolevateClient,
        provider_id: str,
        test_folder_key: str,
    ) -> None:
        original_name = f"rename-source-{_RUN_ID}.txt"
        renamed_name = f"rename-dest-{_RUN_ID}.txt"
        original_key = f"{test_folder_key}{original_name}"

        await live_client.items.upload(
            provider_id,
            key=test_folder_key,
            file=io.BytesIO(b"to be renamed"),
            file_name=original_name,
            mime_type="text/plain",
        )

        item = await live_client.items.rename(provider_id, key=original_key, new_name=renamed_name)

        assert item.key.endswith(renamed_name)

        await live_client.items.delete(provider_id, key=f"{test_folder_key}{renamed_name}")


@pytest.mark.asyncio
class TestProviderItemsGetDownloadUrl:
    async def test_returns_presigned_url(
        self,
        live_client: BiolevateClient,
        provider_id: str,
        uploaded_item_key: str,
    ) -> None:
        result = await live_client.items.get_download_url(provider_id, key=uploaded_item_key)

        assert result.url is not None
        assert result.url.startswith("http")

    async def test_returns_url_even_for_missing_file(
        self,
        live_client: BiolevateClient,
        provider_id: str,
    ) -> None:
        result = await live_client.items.get_download_url(provider_id, key="ghost/file.pdf")
        assert result.url is not None
        assert result.url.startswith("http")


@pytest.mark.asyncio
class TestProviderItemsDelete:
    async def test_deletes_file(
        self,
        live_client: BiolevateClient,
        provider_id: str,
        test_folder_key: str,
    ) -> None:
        file_name = f"delete-me-{_RUN_ID}.txt"
        file_key = f"{test_folder_key}{file_name}"

        await live_client.items.upload(
            provider_id,
            key=test_folder_key,
            file=io.BytesIO(b"temporary"),
            file_name=file_name,
            mime_type="text/plain",
        )

        await live_client.items.delete(provider_id, key=file_key)

    async def test_delete_completes_for_existing_item(
        self,
        live_client: BiolevateClient,
        provider_id: str,
        test_folder_key: str,
    ) -> None:
        file_name = f"delete-check-{_RUN_ID}.txt"
        file_key = f"{test_folder_key}{file_name}"
        await live_client.items.upload(
            provider_id,
            key=test_folder_key,
            file=io.BytesIO(b"to be deleted"),
            file_name=file_name,
            mime_type="text/plain",
        )
        await live_client.items.delete(provider_id, key=file_key)
