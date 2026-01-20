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
