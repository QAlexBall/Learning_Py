import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='192.168.13.201'
    )
)

channel = connection.channel()
channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

result = channel.queue_declare(exclusive=True, queue='')
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    print(sys.stderr, "Usage: %s [binding_key]..." % (sys.argv[0],))
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(
        exchange='topic_logs', queue=queue_name, routing_key=binding_key
    )

print('[*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
channel.basic_consume(on_message_callback=callback, 
                      queue=queue_name)
channel.start_consuming()
