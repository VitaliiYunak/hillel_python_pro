from cassandra.cluster import Cluster
import uuid
from datetime import datetime, timedelta

# Підключення до Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()


# Створення таблиці для логів подій
session.execute("""
CREATE TABLE IF NOT EXISTS logs (
    event_id UUID PRIMARY KEY,
    user_id UUID,
    event_type TEXT,
    timestamp TIMESTAMP,
    metadata TEXT)
""")


# CRUD операції
def create_event_log(user_id, event_type, metadata):
    event_id = uuid.uuid4()
    timestamp = datetime.now()

    session.execute("""
    INSERT INTO logs (event_id, user_id, event_type, timestamp, metadata)
    VALUES (%s, %s, %s, %s, %s)
    """, (event_id, user_id, event_type, timestamp, metadata))
    print(f"Лог події додано з event_id: {event_id}")


def read_event(event_type):
    get_events = datetime.now() - timedelta(days=1)
    events = session.execute("""
    SELECT * FROM logs 
    WHERE event_type = %s AND timestamp >= %s
    """, (event_type, get_events))
    for i in events:
        print(i)


def update_event(event_id, new_metadata):
    session.execute("""
    UPDATE logs 
    SET metadata = %s 
    WHERE event_id = %s
    """, (new_metadata, event_id))
    print(f"Оновлено для event_id: {event_id}")


def delete_old_events():
    events_7ago = datetime.now() - timedelta(days=7)
    session.execute("""
    DELETE FROM logs 
    WHERE timestamp < %s
    """, (events_7ago,))
    print("Події старші за 7 днів видалені.")


if __name__ == "__main__":
    create_event_log(uuid.uuid4(), "login", "Користуввач залогінився")
    read_event("login")
    delete_old_events()
