from utils.data_handler import clean_sales_data

def main():
    file_path = "data/sales_data.txt"
    clean_data = clean_sales_data(file_path)

    # Future analytics can be added here
    # Example:
    # total_revenue = sum(item["Quantity"] * item["UnitPrice"] for item in clean_data)

if __name__ == "__main__":
    main()
