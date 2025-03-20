import json
from dataclasses import dataclass
from typing import Optional
from aio_pika import Message, connect_robust
from aio_pika.abc import AbstractChannel, AbstractRobustConnection
from server.core.types import string

RABBIT_URL = "amqp://hinsun:hinsun@localhost:5672/"
RABBITMQ_QUEUE = "submissions"

@dataclass
class RabbitMQConnection:
    connection: Optional[AbstractRobustConnection] = None
    channel: Optional[AbstractChannel] = None

    async def _clear(self) -> None:
        if not self.channel or not self.connection:
            return

        if not self.channel.is_closed:
            await self.channel.close()
        if not self.connection.is_closed:
            await self.connection.close()

        self.connection = None
        self.channel = None

    async def connect(self) -> None:
        try:
            self.connection = await connect_robust(RABBIT_URL)
            self.channel = await self.connection.channel(publisher_confirms=False)
            print("Connected to RabbitMQ")
        except Exception as exception:
            print(f"Failed to connect to RabbitMQ: {exception}")

    async def disconnect(self) -> None:
        await self._clear()

    async def send_messages(
        self,
        messages: string,
        routing_key: str = RABBITMQ_QUEUE
    ) -> None:
        if not self.channel:
            raise RuntimeError("Not connected")

        async with self.channel.transaction():
            body = Message(body=json.dumps(messages).encode())
            await self.channel.default_exchange.publish(body, routing_key=routing_key)

rabbitmq_connection = RabbitMQConnection()
