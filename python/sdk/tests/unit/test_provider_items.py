"""Unit tests for ProviderItemsResource."""

import io

import pytest
import respx
from httpx import Response

from biolevate import APIError, AuthenticationError, BiolevateClient, NotFoundError

PROVIDER_ID = "550e8400-e29b-41d4-a716-446655440000"


@pytest.mark.asyncio
class TestProviderItemsList:
    @respx.mock
    async def test_returns_items_in_directory(
        self,
        client: BiolevateClient,
        base_url: str,
        list_items_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(200, json=list_items_payload)
        )

        result = await client.items.list(PROVIDER_ID, key="/")

        assert len(result.items) == 1
        assert result.items[0].key == "documents/report.pdf"

    @respx.mock
    async def test_sends_key_param(
        self,
        client: BiolevateClient,
        base_url: str,
        list_items_payload: dict,
    ) -> None:
        route = respx.get(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(200, json=list_items_payload)
        )

        await client.items.list(PROVIDER_ID, key="documents/")

        assert "key=documents" in str(route.calls.last.request.url)

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.items.list(PROVIDER_ID, key="does-not-exist/")

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(401, json={"error": "Unauthorized"})
        )

        with pytest.raises(AuthenticationError):
            await client.items.list(PROVIDER_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(403, json={"error": "Forbidden"})
        )

        with pytest.raises(AuthenticationError):
            await client.items.list(PROVIDER_ID)


@pytest.mark.asyncio
class TestProviderItemsUpload:
    @respx.mock
    async def test_uploads_file_and_returns_item(
        self,
        client: BiolevateClient,
        base_url: str,
        provider_item_payload: dict,
    ) -> None:
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(201, json=provider_item_payload)
        )

        content = io.BytesIO(b"PDF content")
        item = await client.items.upload(PROVIDER_ID, key="documents/", file=content, file_name="report.pdf")

        assert item.key == "documents/report.pdf"
        assert item.type == "FILE"

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(401)
        )

        with pytest.raises(AuthenticationError):
            await client.items.upload(PROVIDER_ID, key="/", file=io.BytesIO(b"x"), file_name="f.txt")

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(403)
        )

        with pytest.raises(AuthenticationError):
            await client.items.upload(PROVIDER_ID, key="/", file=io.BytesIO(b"x"), file_name="f.txt")

    @respx.mock
    async def test_raises_api_error_on_unexpected_status(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(500, text="Server error")
        )

        with pytest.raises(APIError) as exc_info:
            await client.items.upload(PROVIDER_ID, key="/", file=io.BytesIO(b"x"), file_name="f.txt")

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestProviderItemsCreateFolder:
    @respx.mock
    async def test_creates_folder_and_returns_item(
        self,
        client: BiolevateClient,
        base_url: str,
        provider_item_payload: dict,
    ) -> None:
        folder_payload = {**provider_item_payload, "name": "new-folder", "type": "FOLDER"}
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(201, json=folder_payload)
        )

        item = await client.items.create_folder(PROVIDER_ID, key="new-folder/")

        assert item.type == "FOLDER"

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.items.create_folder(PROVIDER_ID, key="missing-parent/folder/")


@pytest.mark.asyncio
class TestProviderItemsRename:
    @respx.mock
    async def test_renames_item(
        self,
        client: BiolevateClient,
        base_url: str,
        provider_item_payload: dict,
    ) -> None:
        renamed_payload = {**provider_item_payload, "key": "documents/renamed.pdf"}
        respx.patch(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(200, json=renamed_payload)
        )

        item = await client.items.rename(PROVIDER_ID, key="documents/report.pdf", new_name="renamed.pdf")

        assert item.key == "documents/renamed.pdf"

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.patch(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.items.rename(PROVIDER_ID, key="ghost.pdf", new_name="anything.pdf")

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.patch(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(401, json={"error": "Unauthorized"})
        )

        with pytest.raises(AuthenticationError):
            await client.items.rename(PROVIDER_ID, key="x.pdf", new_name="y.pdf")

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.patch(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.items.rename(PROVIDER_ID, key="x.pdf", new_name="y.pdf")

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.patch(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.items.rename(PROVIDER_ID, key="x.pdf", new_name="y.pdf")

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestProviderItemsDelete:
    @respx.mock
    async def test_deletes_item(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(204)
        )

        await client.items.delete(PROVIDER_ID, key="documents/report.pdf")

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.items.delete(PROVIDER_ID, key="ghost.pdf")

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(
            return_value=Response(401, json={"error": "Unauthorized"})
        )

        with pytest.raises(AuthenticationError):
            await client.items.delete(PROVIDER_ID, key="x.pdf")

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.items.delete(PROVIDER_ID, key="x.pdf")

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/providers/{PROVIDER_ID}/items").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.items.delete(PROVIDER_ID, key="x.pdf")

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestProviderItemsGetDownloadUrl:
    @respx.mock
    async def test_returns_download_url(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        payload = {"url": "https://storage.example.com/report.pdf?sig=abc"}
        respx.get(f"{base_url}/api/core/providers/{PROVIDER_ID}/items/download-url").mock(
            return_value=Response(200, json=payload)
        )

        result = await client.items.get_download_url(PROVIDER_ID, key="documents/report.pdf")

        assert "https://" in result.url

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/providers/{PROVIDER_ID}/items/download-url").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.items.get_download_url(PROVIDER_ID, key="ghost.pdf")

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/providers/{PROVIDER_ID}/items/download-url").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.items.get_download_url(PROVIDER_ID, key="x.pdf")

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/providers/{PROVIDER_ID}/items/download-url").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.items.get_download_url(PROVIDER_ID, key="x.pdf")

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/providers/{PROVIDER_ID}/items/download-url").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.items.get_download_url(PROVIDER_ID, key="x.pdf")

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestProviderItemsGetUploadUrl:
    @respx.mock
    async def test_returns_upload_url(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        payload = {"url": "https://storage.example.com/upload?sig=xyz", "key": "documents/new.pdf"}
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items/upload-url").mock(
            return_value=Response(200, json=payload)
        )

        result = await client.items.get_upload_url(PROVIDER_ID, key="documents/new.pdf", size=1024)

        assert "https://" in result.url

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items/upload-url").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.items.get_upload_url(PROVIDER_ID, key="missing/new.pdf")

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items/upload-url").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.items.get_upload_url(PROVIDER_ID, key="x.pdf")

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items/upload-url").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.items.get_upload_url(PROVIDER_ID, key="x.pdf")

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items/upload-url").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.items.get_upload_url(PROVIDER_ID, key="x.pdf")

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestProviderItemsConfirmUpload:
    @respx.mock
    async def test_confirms_upload(
        self,
        client: BiolevateClient,
        base_url: str,
        provider_item_payload: dict,
    ) -> None:
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items/confirm").mock(
            return_value=Response(200, json=provider_item_payload)
        )

        item = await client.items.confirm_upload(PROVIDER_ID, key="documents/report.pdf")

        assert item.key == "documents/report.pdf"

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items/confirm").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.items.confirm_upload(PROVIDER_ID, key="ghost.pdf")

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items/confirm").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.items.confirm_upload(PROVIDER_ID, key="x.pdf")

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items/confirm").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.items.confirm_upload(PROVIDER_ID, key="x.pdf")

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/providers/{PROVIDER_ID}/items/confirm").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.items.confirm_upload(PROVIDER_ID, key="x.pdf")

        assert exc_info.value.status_code == 500
