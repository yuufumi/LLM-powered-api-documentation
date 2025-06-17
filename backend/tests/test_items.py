import pytest
from httpx import AsyncClient
from app.core.config import settings

API_V1_STR = settings.API_V1_STR

@pytest.mark.asyncio
async def test_create_item(client: AsyncClient):
    response = await client.post(
        f"{API_V1_STR}/items/", json={"title": "Test Item", "description": "A description"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Item"
    assert "id" in data

@pytest.mark.asyncio
async def test_read_items(client: AsyncClient):
    # First create some items
    await client.post(f"{API_V1_STR}/items/", json={"title": "Item 1"})
    await client.post(f"{API_V1_STR}/items/", json={"title": "Item 2"})

    response = await client.get(f"{API_V1_STR}/items/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 2 # Could be more if other tests ran first
    assert any(item["title"] == "Item 1" for item in data)
    assert any(item["title"] == "Item 2" for item in data)