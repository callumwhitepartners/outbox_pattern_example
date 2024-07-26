from rocketry import Rocketry
from rocketry.conditions.api import every
from outbox.outbox_processor import OutboxProcessor
from outbox.sql_alchemy_message_outbox import SqlAlchemyMessageOutbox
from shared.db import Db
from apos import Apos

from library.domain.events import LibraryCardCreated
from notifications.handlers import library_card_created_event_handler

messenger = Apos()
messenger.subscribe_event(LibraryCardCreated, [library_card_created_event_handler])

app = Rocketry()

@app.task(every("10 seconds"))
def process_messages() -> None:
    session = Db("sqlite:///db.sqlite").session
    message_outbox = SqlAlchemyMessageOutbox(session)
    processor = OutboxProcessor(message_outbox, session, messenger)

    processor.process_outbox_message()


if __name__ == "__main__":
    app.run()
