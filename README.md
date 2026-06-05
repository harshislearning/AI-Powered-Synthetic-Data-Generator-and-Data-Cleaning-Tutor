# 📊 AI-Powered Synthetic Data Generator & Data Cleaning Tutor

An AI-powered web application that generates realistic synthetic datasets with intentionally injected data quality issues and automatically provides step-by-step data cleaning solutions in **Python** or **SQL**.

Built using **Streamlit**, **Faker**, **Pandas**, and **Groq LLM**.

---

## 🚀 Features

### 📈 Synthetic Dataset Generation

Generate realistic datasets for any domain such as:

* Students
* Employees
* Sales
* Healthcare
* Banking
* Office Management
* Custom Domains

Users can define:

* Dataset Domain
* Column Names
* Number of Rows
* Messiness Level

---

### 🧹 Dirty Data Generation

The application intentionally introduces real-world data quality issues:

#### Easy Level

* Missing Values

#### Medium Level

* Missing Values
* Duplicate Records
* Case Inconsistencies

#### Hard Level

* Missing Values
* Duplicate Records
* Typographical Errors
* Case Inconsistencies
* Extra Spaces

This helps users practice real-world data cleaning techniques.

---

### 🤖 AI-Powered Dataset Context

Using Groq LLM, the application generates a realistic context description for the selected dataset domain.

Example:

**Students Dataset**

> Contains student names, email addresses, departments, attendance records, and academic marks.

---

### 💻 AI Cleaning Solution Generator

After generating a dirty dataset, users can automatically generate data-cleaning solutions in:

* Python
* SQL

The generated solution includes:

* Missing Value Handling
* Duplicate Removal
* Case Standardization
* Extra Space Removal
* Typo Detection Suggestions
* Exporting Cleaned Dataset

---

### 📥 Download Support

Users can download:

* Generated Dirty Dataset (.csv)
* Generated Python Cleaning Solution
* Generated SQL Cleaning Solution

---

## 🏗️ Project Architecture

```text
synthetic-data-generator/
│
├── app.py
├── data_generator.py
├── dirty_data.py
├── llm_helper.py
├── solution_generator.py
│
├── outputs/
│   └── generated_dataset.csv
│
├── requirements.txt
├── .env
└── README.md
```

---

## 🛠️ Technologies Used

| Technology          | Purpose                   |
| ------------------- | ------------------------- |
| Python              | Core Development          |
| Streamlit           | Web Application           |
| Pandas              | Data Processing           |
| Faker               | Synthetic Data Generation |
| NumPy               | Data Manipulation         |
| Groq API            | LLM Integration           |
| Qwen / Llama Models | AI Solution Generation    |

---

## ⚙️ Installation

### 1. Download Repo

```bash
Download repo files
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Groq API Setup

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from:

https://console.groq.com

---

## ▶️ Run Application

```bash
streamlit run app.py
```

The application will open automatically at:

```text
http://localhost:8501
```

---

## 📚 Example Workflow

### Step 1

Enter dataset details:

```text
Domain:
Office Employees

Columns:
Name,
Email,
Department,
Salary,
City
```

### Step 2

Select:

```text
Rows = 100

Messiness Level = Hard
```

### Step 3

Generate Dataset

The system creates:

* Realistic synthetic records
* Missing values
* Duplicates
* Typos
* Case inconsistencies
* Extra spaces

---

### Step 4

Download Dataset

```text
office_dataset.csv
```

---

### Step 5

Choose Cleaning Language

* Python
* SQL

---

### Step 6

Generate AI Cleaning Solution

The AI produces a complete step-by-step cleaning script.

---

## 🎯 Learning Outcomes

This project helps users learn:

* Data Cleaning
* Data Preprocessing
* Data Quality Assessment
* Python Data Analysis
* SQL Data Cleaning
* Synthetic Data Generation
* Prompt Engineering
* LLM Integration

---

## 📸 Application Screenshots

Add screenshots here:

```text
<img width="1907" height="974" alt="Screenshot (142)" src="https://github.com/user-attachments/assets/c4049043-7a1d-47f2-be08-63f6a45c09b2" />

<img width="1920" height="974" alt="Screenshot (143)" src="https://github.com/user-attachments/assets/245eb651-d45f-4822-9edb-edc869a6417b" />

<img width="1912" height="974" alt="Screenshot (144)" src="https://github.com/user-attachments/assets/4125f352-0312-486a-8c71-bb6c981bcce3" />

```

---

## 🔮 Future Enhancements

* Excel Export
* Dataset Templates
* Data Quality Dashboard
* Automated Cleaning Score
* Multiple Table Generation
* Relational Database Simulation
* Data Profiling Reports
* AI-Powered Dataset Suggestions
* Docker Deployment
* Cloud Deployment

---

## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and research purposes.
