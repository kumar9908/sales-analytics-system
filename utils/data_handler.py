import csv

def clean_sales_data(file_path):
    total_records = 0
    invalid_records = 0
    valid_records = []

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        reader = csv.reader(file, delimiter='|')
        header = next(reader)  # skip header

        for row in reader:
            if not row or len(row) < 8:
                continue

            total_records += 1

            try:
                transaction_id = row[0].strip()
                date = row[1].strip()
                product_id = row[2].strip()
                product_name = row[3].replace(',', '').strip()
                quantity = int(row[4].replace(',', '').strip())
                unit_price = float(row[5].replace(',', '').strip())
                customer_id = row[6].strip()
                region = row[7].strip()

                # Validation rules (as per assignment)
                if (
                    not transaction_id.startswith('T') or
                    quantity <= 0 or
                    unit_price <= 0 or
                    not customer_id or
                    not region
                ):
                    invalid_records += 1
                    continue

                valid_records.append({
                    "TransactionID": transaction_id,
                    "Date": date,
                    "ProductID": product_id,
                    "ProductName": product_name,
                    "Quantity": quantity,
                    "UnitPrice": unit_price,
                    "CustomerID": customer_id,
                    "Region": region
                })

            except Exception:
                invalid_records += 1
                continue

    # REQUIRED VALIDATION OUTPUT
    print(f"Total records parsed: {total_records}")
    print(f"Invalid records removed: {invalid_records}")
    print(f"Valid records after cleaning: {len(valid_records)}")

    return valid_records

def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """
    Validates transactions and applies optional filters
    """

    total_input = len(transactions)
    invalid_count = 0
    valid_transactions = []

    # ---------- VALIDATION ----------
    for tx in transactions:
        try:
            if (
                not tx.get("TransactionID", "").startswith("T") or
                not tx.get("ProductID", "").startswith("P") or
                not tx.get("CustomerID", "").startswith("C") or
                tx.get("Quantity", 0) <= 0 or
                tx.get("UnitPrice", 0) <= 0
            ):
                invalid_count += 1
                continue

            valid_transactions.append(tx)

        except Exception:
            invalid_count += 1

    # ---------- DISPLAY FILTER OPTIONS ----------
    regions = sorted(set(tx["Region"] for tx in valid_transactions))
    amounts = [tx["Quantity"] * tx["UnitPrice"] for tx in valid_transactions]

    print("\nAvailable Regions:", regions)
    print(f"Transaction Amount Range: {min(amounts)} - {max(amounts)}")

    # ---------- REGION FILTER ----------
    filtered_by_region = 0
    if region:
        before = len(valid_transactions)
        valid_transactions = [
            tx for tx in valid_transactions if tx["Region"] == region
        ]
        filtered_by_region = before - len(valid_transactions)
        print(f"Records after region filter ({region}): {len(valid_transactions)}")

    # ---------- AMOUNT FILTER ----------
    filtered_by_amount = 0
    if min_amount is not None or max_amount is not None:
        before = len(valid_transactions)

        def amount_ok(tx):
            amount = tx["Quantity"] * tx["UnitPrice"]
            if min_amount is not None and amount < min_amount:
                return False
            if max_amount is not None and amount > max_amount:
                return False
            return True

        valid_transactions = list(filter(amount_ok, valid_transactions))
        filtered_by_amount = before - len(valid_transactions)
        print(f"Records after amount filter: {len(valid_transactions)}")

    summary = {
        "total_input": total_input,
        "invalid": invalid_count,
        "filtered_by_region": filtered_by_region,
        "filtered_by_amount": filtered_by_amount,
        "final_count": len(valid_transactions)
    }

    return valid_transactions, invalid_count, summary
