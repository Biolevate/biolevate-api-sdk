"""Integration tests for ProvidersResource."""

import pytest

from biolevate import BiolevateClient, NotFoundError


@pytest.mark.asyncio
class TestProvidersList:
    async def test_returns_at_least_one_provider(self, live_client: BiolevateClient) -> None:
        page = await live_client.providers.list()

        assert page.data is not None
        assert len(page.data) > 0

    async def test_pagination_page_size_is_respected(self, live_client: BiolevateClient) -> None:
        page = await live_client.providers.list(page=0, page_size=1)

        assert page.data is not None
        assert len(page.data) <= 1

    async def test_total_elements_is_consistent(self, live_client: BiolevateClient) -> None:
        page = await live_client.providers.list(page=0, page_size=100)

        assert page.total_elements is not None
        assert page.total_elements >= len(page.data)

    async def test_has_next_is_false_on_small_result_set(self, live_client: BiolevateClient) -> None:
        page = await live_client.providers.list(page=0, page_size=100)

        if page.total_elements <= 100:
            assert page.has_next is False

    async def test_second_page_is_empty_when_total_fits_in_first(self, live_client: BiolevateClient) -> None:
        first = await live_client.providers.list(page=0, page_size=100)

        if not first.has_next:
            second = await live_client.providers.list(page=1, page_size=100)
            assert second.data == [] or len(second.data) == 0


@pytest.mark.asyncio
class TestProvidersGet:
    async def test_get_by_id_returns_correct_provider(
        self,
        live_client: BiolevateClient,
        provider_id: str,
    ) -> None:
        provider = await live_client.providers.get(provider_id)

        assert str(provider.id.id) == provider_id
        assert provider.name is not None
        assert provider.type is not None

    async def test_get_non_existent_raises_not_found(self, live_client: BiolevateClient) -> None:
        with pytest.raises(NotFoundError):
            await live_client.providers.get("00000000-0000-0000-0000-000000000000")

    async def test_provider_has_config(
        self,
        live_client: BiolevateClient,
        provider_id: str,
    ) -> None:
        provider = await live_client.providers.get(provider_id)

        assert provider.config is not None
