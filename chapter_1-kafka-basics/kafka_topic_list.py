from kafka.admin import KafkaAdminClient

def list_kafka_topics(bootstrap_servers):
    # Create a KafkaAdminClient to get metadata about topics
    admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

    # Get the list of topics
    topics = admin_client.list_topics()

    # Filter out internal topics (topics that start with '__')
    user_topics = [topic for topic in topics if not topic.startswith('__')]

    # Print the list of user topics
    print("List of Kafka Topics:")
    for topic in user_topics:
        print(topic)

if __name__ == "__main__":
    # Specify the Kafka broker(s) as a comma-separated list with SSL configurations
    your_bootstrap_servers = '0.0.0.0:9092'  # Use the actual broker addresses and ports
    ssl_config = {
    'security_protocol': 'SSL',
    'ssl_cafile': '/home/codewithneeraj/certificate/kafka_cert/ca-cert',  # Path to CA certificate file
    'ssl_certfile': '/home/codewithneeraj/certificate/kafka_cert/server-cert',  # Path to client certificate file .pem
    'ssl_keyfile': '/home/codewithneeraj/certificate/kafka_cert/ca-cert',  # Path to client private key file
}

    # Call the function to list Kafka topics
    list_kafka_topics(your_bootstrap_servers)
