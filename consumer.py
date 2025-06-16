from kafka import KafkaConsumer
import psycopg2
import json
import csv
import os

# Kafka Consumer setup
consumer = KafkaConsumer(
    "realtime-data",
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='sensor-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# PostgreSQL connection
conn = psycopg2.connect(
    dbname="sensordb",
    user="postgres",
    password="3030",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Consume messages and insert into DB + save to CSV
for message in consumer:
    data = message.value
    print("Received:", data)

    # Insert into PostgreSQL
    cursor.execute(
        "INSERT INTO sensor_data (sensor_id, temperature, humidity, timestamp) VALUES (%s, %s, %s, %s)",
        (data["sensor_id"], data["temperature"], data["humidity"], data["timestamp"])
    )
    conn.commit()

    # Save to CSV
    csv_file = 'sensor_data.csv'
    file_exists = os.path.isfile(csv_file)

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["sensor_id", "temperature", "humidity", "timestamp"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)


