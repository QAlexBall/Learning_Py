import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='192.168.13.201'
    )
)
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')
result = channel.queue_declare(exclusive=True, queue='')
queue_name = result.method.queue
severities = sys.argv[1:]
if not severities:
    print( sys.stderr, "Usage: %s [info] [warning] [error]" % (sys.argv[0]))
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
channel.basic_consume(on_message_callback=callback, queue=queue_name)
channel.start_consuming()
