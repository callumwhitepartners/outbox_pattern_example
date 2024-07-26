# The outbox pattern
The outbox pattern (transactional outbox or store and forward event publisher) is the solution.

We want to ensure that our business entities and our business events are stored within the same transaction.

This approach gives us “at least once delivery”.

It is worth noting that “at least once delivery” means that the same events might be delivered multiple times. We should keep this in mind and endeavor to create event handlers that are idempotent.