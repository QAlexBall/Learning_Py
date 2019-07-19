import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='test')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(on_message_callback=callback,
                      queue='test')
                      #  no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+c')
channel.start_consuming()

