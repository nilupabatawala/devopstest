from fastapi import FastAPI
import pika
import sys

app = FastAPI()

credentials= pika.PlainCredentials('guest','guest')

#publish message to the queue
@app.post("/publish")
def publish_message(message: str):
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq-service', credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='testqueue')

    channel.basic_publish(exchange='direct_logs', routing_key='',
                      body=message)
    

    return {"Message": connection.is_open, "Channel": channel.is_open}

#consume message from the queue
@app.get("/consume")
def publish_message():
    return {"Message": "Consumed"}


