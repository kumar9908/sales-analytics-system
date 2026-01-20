def fetch_product_data():
    """
    Placeholder for external API integration.
    """
    return {}
import requests

def fetch_all_products():
    """
    Fetches all products from DummyJSON API
    """
    url = "https://dummyjson.com/products?limit=100"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        products = data.get("products", [])

        print(f"API Success: Fetched {len(products)} products")
        return products

    except Exception as e:
        print(f"API Failure: {e}")
        return []

def create_product_mapping(api_products):
    """
    Creates a mapping of product IDs to product info
    """
    product_mapping = {}

    for product in api_products:
        pid = product.get("id")

        product_mapping[pid] = {
            "title": product.get("title"),
            "category": product.get("category"),
            "brand": product.get("brand"),
            "rating": product.get("rating")
        }

    return product_mapping

def enrich_sales_data(transactions, product_mapping):
    enriched = []

    for t in transactions:
        record = t.copy()
        product_id = t.get("ProductID", "")

        # ✅ Extract numeric ID (P101 → 101)
        try:
            numeric_id = int("".join(filter(str.isdigit, product_id)))
        except Exception:
            numeric_id = None

        api_product = product_mapping.get(numeric_id)

        if api_product:
            record["API_Category"] = api_product.get("category")
            record["API_Brand"] = api_product.get("brand")
            record["API_Rating"] = api_product.get("rating")
            record["API_Match"] = True
        else:
            record["API_Category"] = None
            record["API_Brand"] = None
            record["API_Rating"] = None
            record["API_Match"] = False

        enriched.append(record)

    return enriched


def save_enriched_data(enriched_transactions, filename="data/enriched_sales_data.txt"):
    """
    Saves enriched transactions back to file
    """

    headers = [
        "TransactionID", "Date", "ProductID", "ProductName",
        "Quantity", "UnitPrice", "CustomerID", "Region",
        "API_Category", "API_Brand", "API_Rating", "API_Match"
    ]

    with open(filename, "w", encoding="utf-8") as file:
        file.write("|".join(headers) + "\n")

        for tx in enriched_transactions:
            row = []
            for h in headers:
                value = tx.get(h)
                row.append("" if value is None else str(value))

            file.write("|".join(row) + "\n")

    print(f"Enriched data saved to {filename}")

