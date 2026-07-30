from aio_pika import Message, connect, DeliveryMode
import json

from src.exception.error import CustomError

class RabbitClient:

    def __init__(self):
        self.connection = None
        self.channel = None

    async def connect(self):
        try:
            self.connection = await connect("amqp://guest:guest@localhost:5672/") 
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