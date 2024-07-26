import uuid

from library.application.service import LibraryCardService
from library.infra.sql_alchemy_library_card_repository import SqlAlchemyLibraryCardRepository
from messaging.sql_alchemy_message_outbox import SqlAlchemyMessageOutbox
from shared.db import Db
from shared.event_bus import StoreAndForwardEventBus
import time


def main() -> None:
    session = Db("sqlite:///db.sqlite").session
    repo = SqlAlchemyLibraryCardRepository(session)
    message_outbox = SqlAlchemyMessageOutbox(session)
    event_bus = StoreAndForwardEventBus(message_outbox)
    service = LibraryCardService(repo, event_bus, session)

    service.create(uuid.uuid4().hex)
    
if __name__ == "__main__":
    main()
