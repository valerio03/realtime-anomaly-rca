# Realtime Anomaly Detection and Root Cause Analysis  
AI-powered system for detecting anomalies in streaming data and identifying their root causes in real time.
## 🚀 Overview  
This project provides a scalable pipeline for real-time anomaly detection and root cause analysis (RCA).  
It uses **Kafka** for streaming, **ClickHouse** for fast storage, and **deep learning models** for anomaly detection.  
The system can be extended to monitor IoT devices, financial transactions, healthcare systems, or industrial data.  
## 📂 Project Structure  
realtime-anomaly-rca/
│── apps/                # Core microservices (producer, featurizer, detector, rca, api, app)
│── configs/             # Config files for services
│── eval/                # Evaluation scripts and benchmarks
│── infra/               # Infrastructure (Kafka, ClickHouse, Grafana)
│── models/              # Pre-trained and trained ML models
│── notebooks/           # Experiments and prototyping
│── docker-compose.yml   # Service orchestration
│── Makefile             # Automation commands
│── .gitignore
│── README.md
