import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue named 'hello'
channel.queue_declare(queue='hello')

# Send a message to the queue
def sending():
    for i in range(10):
        channel.basic_publish(exchange='',
                                routing_key='hello',
                                body=f'Hello World!{i}')
        print(f" [x] Sent 'Hello World!'{i}")

    # Close the connection
    connection.close()


if __name__ == '__main__':
    sending()