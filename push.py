from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    client_id='me',
    api_version=(0, 10, 1)
)

producer.send("tampa-collector", b"this is a message")
result = future.get(timeout=60)
