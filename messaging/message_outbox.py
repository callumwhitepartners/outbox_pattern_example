from abc import ABC, abstractmethod

from messaging.message import OutboxMessage
from shared.event import Event


class IMessageOutbox(ABC):
    @abstractmethod
    def save(self, event: Event) -> None:
        pass

    @abstractmethod
    def mark_as_published(self, message: OutboxMessage) -> None:
        pass

    @abstractmethod
    def to_publish(self) -> list[OutboxMessage]:
        pass
