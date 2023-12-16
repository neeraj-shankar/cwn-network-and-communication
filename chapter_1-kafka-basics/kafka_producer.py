from kafka import KafkaProducer

# Specify the Kafka broker(s) and SSL configuration
bootstrap_servers = 'localhost:9092'
ssl_config = {
    'security_protocol': 'SSL',
    'ssl_cafile': '/home/codewithneeraj/certificate/kafka_cert/ca-cert',  # Path to CA certificate file
    'ssl_certfile': '/home/codewithneeraj/certificate/kafka_cert/server-cert',  # Path to client certificate file .pem
    'ssl_keyfile': '/home/codewithneeraj/certificate/kafka_cert/ca-cert',  # Path to client private key file
}

# Create a Kafka producer instance with SSL configuration
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    api_version=(0,11,5),
)

# Produce a message
topic = 'sample.data'
message_key = b'key'
message_value = b'Hello, Kafka with SSL!'

# Produce the message asynchronously
future = producer.send(topic, key=message_key, value=message_value)

# Wait for the message to be sent
record_metadata = future.get(timeout=10)

print('Message sent to partition {}, offset {}'.format(record_metadata.partition, record_metadata.offset))

# Close the producer to release resources
producer.close()
