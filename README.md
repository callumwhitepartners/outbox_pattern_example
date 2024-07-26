# The outbox pattern
The outbox pattern, also known as the transactional outbox or store and forward event publisher, is an effective solution for ensuring reliable message delivery in distributed systems. This pattern addresses the need to maintain consistency between business entities and events by storing them within the same transaction.

Using this approach guarantees "at least once delivery," meaning each event will be delivered at least once. However, this can result in the same event being delivered multiple times. Therefore, it's crucial to design event handlers to be idempotent, ensuring they can handle duplicate events without causing issues.

To implement the outbox pattern, save both business entity changes and the corresponding events to an outbox table within a single database transaction. After the transaction commits, a separate process reads from the outbox table and publishes the events to the message broker or event bus. This ensures system resilience and consistency, even during failures or retries.

