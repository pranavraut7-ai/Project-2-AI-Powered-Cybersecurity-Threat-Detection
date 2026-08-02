# AI-Powered Cybersecurity Threat Detection System

An industry-oriented Machine Learning project that simulates a Security Operations Center (SOC) workflow for detecting cyber threats using public cybersecurity datasets.

> 🚧 This project is currently under active development.

---

## Project Objective

The goal of this project is to build a machine learning system capable of detecting malicious network activity using structured cybersecurity datasets. The system demonstrates an end-to-end workflow including data preprocessing, feature engineering, model training, threat prediction, alert generation, and visualization.

---

## Features (Planned)

- Dataset preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Machine Learning model training
- Model evaluation
- Threat detection
- Alert generation
- Visualization dashboard
- Model persistence
- Professional documentation

---

## Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Jupyter Notebook

---

## Project Status

Current Phase:

> Milestone 2 – Environment Setup

Upcoming:

- Dataset integration
- Data preprocessing
- Model development
- Threat detection engine
- Visualization
- Documentation

---

## Repository Structure

```text
src/
data/
models/
outputs/
assets/
docs/
```

---

## License

This project is licensed under the MIT License.



# Dataset Setup

This project uses the **CICIDS2017** dataset for training and evaluating the machine learning models.

> **Note:** The dataset is **not included** in this repository because of its large size.

## Download Dataset

Download the CICIDS2017 Machine Learning CSV files from the official Canadian Institute for Cybersecurity (CIC) website or a trusted mirror.

## Required CSV Files

Place the following CSV files inside:

```
data/raw/
```

Directory structure:

```
Project-2-AI-Powered-Cybersecurity-Threat-Detection/
│
├── data/
│   └── raw/
│       ├── Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
│       ├── Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
│       ├── Friday-WorkingHours-Morning.pcap_ISCX.csv
│       ├── Monday-WorkingHours.pcap_ISCX.csv
│       ├── Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
│       ├── Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
│       ├── Tuesday-WorkingHours.pcap_ISCX.csv
│       └── Wednesday-workingHours.pcap_ISCX.csv
```

## Verify Dataset

After copying the dataset, run:

```bash
python main.py
```

If the dataset is detected successfully, the loader will automatically:

- Validate the dataset directory
- Discover all CSV files
- Merge the CSV files
- Begin the preprocessing pipeline
