from aio_pika import Message, connect, DeliveryMode
import json
import os
from dotenv import load_dotenv

from src.exception.error import CustomError

load_dotenv()
class RabbitClient:

    def __init__(self):
        self.connection = None
        self.channel = None
        self.rabbit_url = os.getenv("RABBITMQ_URL")

    async def connect(self):
        try:
            self.connection = await connect(self.rabbit_url) 
            self.channel = await self.connection.channel()
        except Exception as e:
            raise CustomError("Failed to connect to rabbitMQ", 500, "rabbit-connection") from e

    async def create_queue(self, queue_name):
        if self.channel is None:
            raise CustomError("Failed to create the channel", 500, "rabbit-channel")

        await self.channel.declare_queue(
            queue_name,
            durable=True,
            arguments={
                "x-dead-letter-exchange": "",
                "x-dead-letter-routing-key": f"{queue_name}.dlq"
            }
        )
    
    async def publish(self, queue_name, message):
        if self.channel is None:
            raise CustomError("Failed to create the channel", 500, "rabbit-channel")
        
        parsed_message = Message(
            body=self.parse_message(message),
            delivery_mode=DeliveryMode.PERSISTENT,
            content_type="application/json"
        )        
        
        await self.channel.default_exchange.publish(
            parsed_message,
            routing_key=queue_name,
        )

    async def close(self):
        if self.connection:
            await self.connection.close()
    
    def parse_message(self, message):
        return json.dumps(message).encode("utf-8")