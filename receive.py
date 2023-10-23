import pika, sys, os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    # Define a callback function to receive messages from the queue
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        

    # Tell RabbitMQ to call the callback function whenever there is a message in the queue
    channel.basic_consume(queue='hello',
                            auto_ack=True,
                            on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)