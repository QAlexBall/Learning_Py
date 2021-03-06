import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.13.201'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True, queue='')
queue_name = result.method.queue
channel.queue_bind(exchange='logs', 
                   queue=queue_name)
print('[*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print("[x] %r" % body)

channel.basic_consume(on_message_callback=callback,
                      queue=queue_name)
channel.start_consuming()
