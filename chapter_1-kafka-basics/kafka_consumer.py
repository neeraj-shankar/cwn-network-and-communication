from kafka import KafkaConsumer
from kafka.errors import KafkaError

# Define the Kafka broker's address (replace with your Bitnami Kafka Docker container's address)
kafka_broker = ["localhost:9093", "localhost:9092"] # Replace with your Kafka broker's SSL-enabled address

# Define the Kafka topic you want to consume messages from
kafka_topic = "sample.data"  # Replace with your Kafka topic name

# Configure SSL settings
ssl_config = {
    'security_protocol': 'SSL',
    'ssl_cafile': 'path/to/ssl/ca-cert',  
    'ssl_certfile': "/home/codewithneeraj/certificate/kafka_cert/server-cert",  
    'ssl_keyfile': "/home/codewithneeraj/certificate/kafka_cert/ca-cert" ,
}

# Kafka Consumer configuration
consumer = KafkaConsumer(
    kafka_topic,
    bootstrap_servers=kafka_broker,
    api_version=(0,11,5),
    auto_offset_reset='earliest',  # Start consuming from the beginning of the topic
    enable_auto_commit=False,  # Disable auto-commit of offsets
    **ssl_config  # Add SSL configuration
)

# Consume and print messages
for message in consumer:
    if message.error():
        if message.error().code() == KafkaError._PARTITION_EOF:
            print('Reached end of partition')
        else:
            print('Error while consuming message: {}'.format(message.error()))
    else:
        print('Received message: {}'.format(message.value))

# Close the consumer
consumer.close()
