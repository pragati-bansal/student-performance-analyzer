# 🎓 Student Performance Analyzer

A backend-focused analytics system built using **Python, MySQL, and Flask**, designed to analyze student academic performance and expose meaningful insights through **REST APIs** documented with **Swagger**.

---

## 🚀 Features

- 📊 View complete student performance data
- ⚠️ Identify weak subjects using configurable thresholds
- 🏆 Fetch top-performing students
- 🧠 Intelligent performance insights (strengths & weaknesses)
- ➕ Controlled data insertion via POST APIs
- 📘 Interactive API documentation using Swagger

---

## 🛠 Tech Stack

- **Python**
- **Flask**
- **Flask-RESTX (Swagger)**
- **MySQL**
- **SQL Views**
- **REST APIs**

---

## 📂 Project Structure


student-performance-analyzer/

```text
student-performance-analyzer/
├── backend/
│   ├── app.py
│   ├── analysis.py
│   └── db_config.py
│
├── database/
│   ├── schema.sql
│   └── sample_data.sql
│
├── frontend/
│
├── .gitignore
└── README.md
```


## 📘 API Documentation (Swagger UI)

After starting the server, access the **Swagger UI** at:

http://127.0.0.1:5000/


Swagger allows you to:
- View all available APIspython backend/app.py

- Enter query parameters
- Use **Try it out** to test endpoints
- See live JSON responses

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/pragati-bansal/student-performance-analyzer.git
cd student-performance-analyzer

pip install -r requirements.txt

source database/schema.sql;
source database/sample_data.sql;

### 🔍 Swagger UI Preview

![Swagger UI](assets/swagger-ui.png)




