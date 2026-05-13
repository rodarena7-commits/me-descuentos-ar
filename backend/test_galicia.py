import asyncio
import sys
sys.path.insert(0, '.')
from app.scrapers.galicia import scrape_galicia

async def main():
    results = await scrape_galicia()
    print(f"Total resultados: {len(results)}")
    for i, r in enumerate(results[:10]):
        print(f"\n--- [{i+1}] ---")
        print(f"  title:            {r['title']}")
        print(f"  description:      {r['description']}")
        print(f"  discount_type:    {r['discount_type']}")
        print(f"  percentage:       {r['percentage']}")
        print(f"  max_amount:       {r['max_amount']}")
        print(f"  category:         {r['category']}")
        print(f"  days_of_week:     {r['days_of_week']}")
        print(f"  url:              {r['url']}")
        print(f"  is_limited_stock: {r['is_limited_stock']}")

asyncio.run(main())
