import pika

credentials = pika.PlainCredentials('chris', 'chris')

connection = pika.BlockingConnection(
    pika.ConnectionParameters('192.168.13.32', 5672, '/', credentials)
)
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

print(" [x] Sent 'Hello World!'")
connection.close()

