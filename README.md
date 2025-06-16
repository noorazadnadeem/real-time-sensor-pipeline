# real-time-sensor-pipeline
Real-time data pipeline using Kafka, Python, PostgreSQL, and CSV

This project demonstrates a real-time data ingestion and storage pipeline using Apache Kafka, Python, PostgreSQL, and CSV.

## 📌 Tech Stack
- Apache Kafka
- Python 3
- PostgreSQL
- Libraries: `kafka-python`, `psycopg2`, `csv`, `json`

## 🔄 Pipeline Flow
1. **Producer** generates simulated sensor data (temperature, humidity, timestamp).
2. **Kafka Consumer** listens to a topic and writes data to:
   - PostgreSQL database: `sensordb`, table: `sensor_data`
   - CSV file: `sensor_data.csv`

---

## 🛠️ Setup Instructions

### ✅ Step 1: Start Zookeeper
```bash
zookeeper-server-start.bat ..\..\config\zookeeper.properties
✅ Step 2: Start Kafka Server
bash
Copy
Edit
kafka-server-start.bat ..\..\config\server.properties
✅ Step 3: Create Kafka Topic (Run Once)
bash
Copy
Edit
kafka-topics.bat --create --topic realtime-data --bootstrap-server localhost:9092
✅ Step 4: Create PostgreSQL Database and Table
sql
Copy
Edit
CREATE DATABASE sensordb;

CREATE TABLE sensor_data (
    sensor_id VARCHAR(50),
    temperature FLOAT,
    humidity FLOAT,
    timestamp TIMESTAMP
);
✅ Step 5: Run Python Scripts
Start Producer:
bash
Copy
Edit
py producer.py
Start Consumer:
bash
Copy
Edit
py consumer.py
📂 Directory Structure
Copy
Edit
KafkaRealTimeProject/
├── producer.py
├── consumer.py
├── sensor_data.csv
├── README.md
🙋‍♂️ Author
Nadeem Azad
GitHub: @noorazadnadeem
