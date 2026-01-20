Project Overview

The Sales Analytics System is a Python-based application designed to process, clean, and analyze sales transaction data for an e-commerce company.
It handles real-world data quality issues such as missing values, incorrect formats, and invalid records, and prepares clean data for further business analysis and reporting.

This project is developed as part of Module 3: Python Programming Assignment.

🗂️ Project Structure
sales-analytics-system/
│── main.py
│── README.md
│── requirements.txt
│
├── data/
│   └── sales_data.txt
│
└── utils/
    ├── data_handler.py
    ├── file_handler.py
    └── api_handler.py
⚙️ Features

Reads pipe-delimited (|) sales data

Handles non-UTF encoding issues

Cleans real-world dirty data:

Removes invalid records

Fixes comma-separated numbers

Cleans product names containing commas

Validates records based on business rules

Prints validation summary after cleaning

Modular and scalable code structure

🧹 Data Cleaning Rules
❌ Records REMOVED if:

CustomerID is missing

Region is missing

Quantity ≤ 0

UnitPrice ≤ 0

TransactionID does not start with "T"

✅ Records CLEANED & KEPT if:

Product names contain commas (commas removed)

Numeric values contain commas (converted properly)

Empty lines are skipped

📊 Validation Output

After cleaning, the program prints:

Total records parsed: XX
Invalid records removed: XX
Valid records after cleaning: XX

(Expected valid records after cleaning ≈ 70)

▶️ How to Run the Project
1️⃣ Prerequisites

Python 3.8 or higher

Git (optional but recommended)

2️⃣ Install Dependencies

This project uses only standard Python libraries.
No external packages are required.

(Optional)

pip install -r requirements.txt
3️⃣ Run the Application

Navigate to the project root directory and run:

python main.py
🧠 main.py (Execution Flow)

Loads the sales data file from data/

Calls the cleaning function from utils/data_handler.py

Displays validation statistics

Returns cleaned data for future analytics

🔮 Future Enhancements

Sales revenue analysis

Region-wise performance reports

API-based product data integration

CSV / JSON report generation

Visualization using charts

🛠️ Technologies Used

Python 3

File handling

Exception handling

Modular programming

👤 Author

Saurav Kumar