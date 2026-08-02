# 🛡️ AI-Powered Cybersecurity Threat Detection System

An end-to-end Machine Learning project that simulates a **Security Operations Center (SOC)** workflow by detecting malicious network traffic using the **CICIDS2017** cybersecurity dataset.

> 🚧 **Project Status:** Active Development

---

# 📌 Overview

Cyberattacks are increasing in both frequency and sophistication, making automated threat detection a critical requirement for modern organizations.

This project demonstrates a complete machine learning pipeline capable of identifying malicious network activities from network traffic data. The system performs data preprocessing, feature engineering, model training, evaluation, threat prediction, severity analysis, and alert generation in a modular and scalable architecture.

The project has been designed following industry-level software engineering practices with clean code organization, reusable modules, logging support, documentation, and model persistence.

---

# 🎯 Objectives

The primary objectives of this project are:

- Build a complete cybersecurity threat detection pipeline.
- Perform preprocessing on raw network traffic datasets.
- Engineer machine-learning-ready features.
- Train and compare multiple classification models.
- Automatically select the best-performing model.
- Predict threats using unseen network traffic.
- Generate severity levels and alerts.
- Produce evaluation reports and visualizations.
- Maintain a modular, production-ready codebase.

---

# ✨ Features

- Automated dataset loading
- Data cleaning and preprocessing
- Feature engineering pipeline
- Label encoding
- Feature scaling
- Train/Test split
- Multiple Machine Learning models
- Automatic best model selection
- Threat prediction
- Threat severity classification
- Alert generation
- Evaluation reports
- Confusion matrix generation
- Model persistence using Joblib
- Professional logging system
- Modular project architecture

---

# 🧠 Machine Learning Models

The project currently trains and evaluates the following algorithms:

- Logistic Regression
- Decision Tree
- Random Forest ⭐ (Best Model)
- Extra Trees

Each model is evaluated using standard classification metrics before selecting the best-performing model.

---

# 🛠 Technology Stack

### Programming Language

- Python 3.12

### Machine Learning

- Scikit-learn

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib

### Model Persistence

- Joblib

### Development Environment

- Visual Studio Code

### Version Control

- Git
- GitHub

---

# 📂 Project Structure

```
Project-2-AI-Powered-Cybersecurity-Threat-Detection/
│
├── assets/
│
├── docs/
│   ├── architecture.md
│   ├── dataset.md
│   ├── interview-guide.md
│   └── workflow.md
│
├── notebooks/
│   └── EDA.ipynb
│
├── src/
│   ├── detection/
│   ├── models/
│   ├── preprocessing/
│   ├── training/
│   ├── utils/
│   └── visualization/
│
├── data/
│   └── raw/
│
├── outputs/
│
├── detect.py
├── train.py
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🏗 Project Architecture

```
                    Raw Dataset
                         │
                         ▼
                  Dataset Loader
                         │
                         ▼
                  Data Cleaning
                         │
                         ▼
               Feature Engineering
                         │
                         ▼
                  Model Training
                         │
                         ▼
                 Model Evaluation
                         │
                         ▼
                 Best Model Saved
                         │
                         ▼
                 Threat Prediction
                         │
                         ▼
               Severity Classification
                         │
                         ▼
                  Alert Generation
```

---

# 📊 Dataset

This project uses the **CICIDS2017** dataset developed by the **Canadian Institute for Cybersecurity (CIC)**.

The dataset contains realistic network traffic collected under both normal and malicious conditions, making it suitable for intrusion detection research and machine learning applications.

For repository size optimization, the dataset is **not included** in this repository.

---

# 📥 Dataset Setup

Download the CICIDS2017 Machine Learning CSV files from the official CIC website or another trusted mirror.

Place all CSV files inside:

```
data/raw/
```

Example:

```
data/
└── raw/
    ├── Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
    ├── Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
    ├── Friday-WorkingHours-Morning.pcap_ISCX.csv
    ├── Monday-WorkingHours.pcap_ISCX.csv
    ├── Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
    ├── Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
    ├── Tuesday-WorkingHours.pcap_ISCX.csv
    └── Wednesday-workingHours.pcap_ISCX.csv
```

---

# ⚙ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/pranavraut7-ai/Project-2-AI-Powered-Cybersecurity-Threat-Detection.git
```

---

## 2. Navigate to the Project

```bash
cd Project-2-AI-Powered-Cybersecurity-Threat-Detection
```

---

## 3. Create Virtual Environment

Windows

```bash
python -m venv .venv
```

---

## 4. Activate Virtual Environment

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Command Prompt

```cmd
.venv\Scripts\activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Download the Dataset

Copy all CICIDS2017 CSV files into:

```
data/raw/
```

---

## 7. Verify Installation

Run:

```bash
python main.py
```

If everything is configured correctly, the project will automatically:

- Load all dataset files
- Merge datasets
- Clean the data
- Perform feature engineering
- Train machine learning models
- Evaluate model performance
- Save the best-performing model

---

➡️ **Part 2 will continue from here with:**
- Usage Guide
- CLI Menu
- Training Workflow
- Detection Workflow
- Results & Performance
- Future Scope
- Contributing
- License
- Author
- Acknowledgements


