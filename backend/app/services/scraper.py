import json

def extract_rozetka_id(href: str) -> int:
    part = href.rstrip("/").split("/")[-1] 
    return int(part.replace("p", ""))

async def fetch_product(rozetka_id: int, page) -> dict:
    url = f"https://common-api.rozetka.com.ua/v1/api/product/details?country=UA&lang=ua&ids={rozetka_id}&platform=desktop"
    await page.goto(url)
    content = await page.inner_text("body")
    data = json.loads(content)
    return data["data"][0]

async def search_rozetka(text: str, page) -> list[dict]:
    url = f"https://common-api.rozetka.com.ua/v1/api/catalog/search?country=UA&lang=ua&page=1&platform=desktop&text={text}"
    await page.goto(url)
    content = await page.inner_text("body")
    data = json.loads(content)
    ids = [item["id"] for item in data["data"]["goods"]]
    
    ids_str = ",".join(str(i) for i in ids)
    return await fetch_products_by_ids(ids_str, page)

async def fetch_products_by_ids(ids: str, page) -> list[dict]:
    url = f"https://common-api.rozetka.com.ua/v1/api/product/details?country=UA&lang=ua&ids={ids}&platform=desktop"
    await page.goto(url)
    content = await page.inner_text("body")
    data = json.loads(content)
    return data["data"]