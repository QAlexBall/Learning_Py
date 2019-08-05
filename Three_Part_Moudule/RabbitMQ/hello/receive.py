import pika 

credentials = pika.PlainCredentials('chris', 'chris')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        '192.168.13.32', 
        5672, 
        '/', 
        credentials)
)
channel = connection.channel()

channel.queue_declare(queue='test', durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(on_message_callback=callback,
                      queue='test')
                      #  no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+c')
channel.start_consuming()

