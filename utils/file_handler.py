def save_clean_data(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for record in data:
            file.write(str(record) + "\n")

def read_sales_data(filename):
    """
    Reads sales data from file handling encoding issues

    Returns: list of raw lines (strings)
    """

    encodings = ["utf-8", "latin-1", "cp1252"]

    for encoding in encodings:
        try:
            with open(filename, "r", encoding=encoding, errors="ignore") as file:
                lines = file.readlines()

                # Remove header and empty lines
                cleaned_lines = [
                    line.strip()
                    for line in lines[1:]
                    if line.strip()
                ]

                return cleaned_lines

        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return []

        except UnicodeDecodeError:
            continue

    print("Error: Unable to read file with supported encodings.")
    return []


def parse_transactions(raw_lines):
    """
    Parses raw lines into clean list of dictionaries
    """

    transactions = []

    for line in raw_lines:
        try:
            parts = line.split("|")

            if len(parts) != 8:
                continue

            transaction = {
                "TransactionID": parts[0].strip(),
                "Date": parts[1].strip(),
                "ProductID": parts[2].strip(),
                "ProductName": parts[3].replace(",", "").strip(),
                "Quantity": int(parts[4].replace(",", "").strip()),
                "UnitPrice": float(parts[5].replace(",", "").strip()),
                "CustomerID": parts[6].strip(),
                "Region": parts[7].strip()
            }

            transactions.append(transaction)

        except ValueError:
            continue
        except Exception:
            continue

    return transactions
