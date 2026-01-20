def calculate_total_revenue(transactions):
    """
    Calculates total revenue from all transactions
    """
    total = 0.0
    for tx in transactions:
        total += tx["Quantity"] * tx["UnitPrice"]
    return total

def region_wise_sales(transactions):
    """
    Analyzes sales by region
    """
    region_data = {}
    grand_total = calculate_total_revenue(transactions)

    for tx in transactions:
        region = tx["Region"]
        amount = tx["Quantity"] * tx["UnitPrice"]

        if region not in region_data:
            region_data[region] = {
                "total_sales": 0.0,
                "transaction_count": 0
            }

        region_data[region]["total_sales"] += amount
        region_data[region]["transaction_count"] += 1

    # Add percentage & sort
    result = {}
    for region, data in sorted(
        region_data.items(),
        key=lambda x: x[1]["total_sales"],
        reverse=True
    ):
        result[region] = {
            "total_sales": round(data["total_sales"], 2),
            "transaction_count": data["transaction_count"],
            "percentage": round((data["total_sales"] / grand_total) * 100, 2)
        }

    return result

def top_selling_products(transactions, n=5):
    """
    Finds top n products by total quantity sold
    """
    product_stats = {}

    for tx in transactions:
        product = tx["ProductName"]
        qty = tx["Quantity"]
        revenue = qty * tx["UnitPrice"]

        if product not in product_stats:
            product_stats[product] = {"qty": 0, "revenue": 0.0}

        product_stats[product]["qty"] += qty
        product_stats[product]["revenue"] += revenue

    sorted_products = sorted(
        product_stats.items(),
        key=lambda x: x[1]["qty"],
        reverse=True
    )

    return [
        (name, data["qty"], round(data["revenue"], 2))
        for name, data in sorted_products[:n]
    ]

def customer_analysis(transactions):
    """
    Analyzes customer purchase patterns
    """
    customers = {}

    for tx in transactions:
        cid = tx["CustomerID"]
        amount = tx["Quantity"] * tx["UnitPrice"]
        product = tx["ProductName"]

        if cid not in customers:
            customers[cid] = {
                "total_spent": 0.0,
                "purchase_count": 0,
                "products": set()
            }

        customers[cid]["total_spent"] += amount
        customers[cid]["purchase_count"] += 1
        customers[cid]["products"].add(product)

    # Sort by total_spent descending
    sorted_customers = dict(
        sorted(customers.items(), key=lambda x: x[1]["total_spent"], reverse=True)
    )

    result = {}
    for cid, data in sorted_customers.items():
        result[cid] = {
            "total_spent": round(data["total_spent"], 2),
            "purchase_count": data["purchase_count"],
            "avg_order_value": round(
                data["total_spent"] / data["purchase_count"], 2
            ),
            "products_bought": sorted(list(data["products"]))
        }

    return result

def daily_sales_trend(transactions):
    """
    Analyzes sales trends by date
    """
    daily = {}

    for tx in transactions:
        date = tx["Date"]
        amount = tx["Quantity"] * tx["UnitPrice"]

        if date not in daily:
            daily[date] = {
                "revenue": 0.0,
                "transaction_count": 0,
                "customers": set()
            }

        daily[date]["revenue"] += amount
        daily[date]["transaction_count"] += 1
        daily[date]["customers"].add(tx["CustomerID"])

    result = {}
    for date in sorted(daily.keys()):
        result[date] = {
            "revenue": round(daily[date]["revenue"], 2),
            "transaction_count": daily[date]["transaction_count"],
            "unique_customers": len(daily[date]["customers"])
        }

    return result

def find_peak_sales_day(transactions):
    """
    Identifies the date with highest revenue
    """
    daily = {}

    for tx in transactions:
        date = tx["Date"]
        amount = tx["Quantity"] * tx["UnitPrice"]

        if date not in daily:
            daily[date] = {"revenue": 0.0, "count": 0}

        daily[date]["revenue"] += amount
        daily[date]["count"] += 1

    peak_date = max(daily.items(), key=lambda x: x[1]["revenue"])

    return (
        peak_date[0],
        round(peak_date[1]["revenue"], 2),
        peak_date[1]["count"]
    )

def low_performing_products(transactions, threshold=10):
    """
    Identifies products with low sales
    """
    products = {}

    for tx in transactions:
        name = tx["ProductName"]
        qty = tx["Quantity"]
        revenue = qty * tx["UnitPrice"]

        if name not in products:
            products[name] = {"qty": 0, "revenue": 0.0}

        products[name]["qty"] += qty
        products[name]["revenue"] += revenue

    low_products = [
        (name, data["qty"], round(data["revenue"], 2))
        for name, data in products.items()
        if data["qty"] < threshold
    ]

    return sorted(low_products, key=lambda x: x[1])

