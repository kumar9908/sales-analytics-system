# Sales Analytics System (Python)

## 📌 Project Overview

The **Sales Analytics System** is an end-to-end Python application that processes raw sales data, validates and filters transactions, performs analytics, integrates external product data via API, and generates a comprehensive formatted sales report.

This project is designed using a **modular architecture** and follows real-world data handling practices such as error handling, validation rules, and reporting.

---

## 🗂️ Project Structure

```
sales-analytics-system/
├── main.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── sales_data.txt
│   └── enriched_sales_data.txt
│
├── output/
│   └── sales_report.txt
│
└── utils/
    ├── file_handler.py
    ├── data_handler.py
    ├── data_processor.py
    ├── api_handler.py
    └── report_generator.py
```

---

## ⚙️ Features

* Reads pipe-delimited sales data with encoding handling
* Cleans and validates real-world dirty data
* Supports optional user-driven filtering (region & amount)
* Performs sales analytics:

  * Total revenue
  * Region-wise performance
  * Top products and customers
  * Daily sales trends
  * Peak sales day
  * Low-performing products
* Integrates external product data using DummyJSON API
* Gracefully handles missing API matches
* Generates a detailed, formatted text report
* Modular, extensible, and production-style design

---

## 🧹 Data Validation Rules

Transactions are considered **invalid** if:

* Quantity ≤ 0
* Unit Price ≤ 0
* Missing required fields
* TransactionID does not start with `T`
* ProductID does not start with `P`
* CustomerID does not start with `C`

Invalid records are excluded from further processing.

---

## 🌐 API Integration

* External API used: **DummyJSON Products API**
* Product IDs are matched by extracting numeric values from sales ProductID
* If no API match exists, the system:

  * Marks `API_Match = False`
  * Continues processing without failure
* This demonstrates **robust real-world integration handling**

---

## 📄 Report Generation

A comprehensive report is generated at:

```
output/sales_report.txt
```

### Report Sections Include:

1. Header & metadata
2. Overall sales summary
3. Region-wise performance
4. Top 5 products
5. Top 5 customers
6. Daily sales trends
7. Product performance analysis
8. API enrichment summary

All monetary values are formatted with commas for readability.

---

## ▶️ How to Run the Project

### 1️⃣ Prerequisites

* Python **3.8+**
* Internet connection (for API integration)

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Application

From the project root directory:

```bash
python main.py
```

The program will:

* Ask whether you want to apply filters
* Execute all processing steps
* Save enriched data and report files automatically

---

## 🧪 Output Files

* `data/enriched_sales_data.txt` → Sales data after API enrichment
* `output/sales_report.txt` → Final formatted analytics report

---

## 🧠 Design Highlights

* Clear separation of concerns (file handling, validation, analytics, API, reporting)
* Defensive programming with graceful error handling
* User-interactive main application flow
* Suitable for academic evaluation and real-world extension

---

## 👤 Author

**Saurav Kumar**

---