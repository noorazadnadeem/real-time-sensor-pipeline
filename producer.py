from kafka import KafkaProducer
import json
import random
import time

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simulate and send sensor data
while True:
    sensor_data = {
        "sensor_id": random.randint(1, 10),
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "timestamp": time.time()
    }
    producer.send("realtime-data", value=sensor_data)
    print("Sent:", sensor_data)
    time.sleep(2)

