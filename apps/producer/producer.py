from kafka import kafkaproducer
import json
import time
import random

#connect to kafka broker 
producer = kafkaproducer(
    bootstrap_servers="localhost=9092",
    value_serialiser=lambda v: json.dumps(v).encode("utf-8")
)

topic = "events"

while true:
    #simulated sensor/transaction event 
    message = {
        "senson_id": random.randit(1, 5),
        "value" round(random.uniform(20.0, 100.0), 2),
        "timestamp": time.time()
    }
    producer.send(topic,message)
    print(f"sent: {message}")
    time.sleep(1)