from sqlalchemy.orm import aliased

from thor.db import create_sa_connection
from thor.models import Module

# The connection string for connecting to the database
connection_string = "postgresql+psycopg2://postgres@localhost:15432/repository"

# Get the engine and the session we need to use engine for core and session for orm
engine, session = create_sa_connection(connection_string)

# Elementary Algebra
collection_uuid = "0889907c-f0ef-496a-bcb8-2a5bb121717f"

ParentModule = aliased(Module, name='parent_module')

# Get the collection from the DB
collection = session.query(Module).join(ParentModule, Module.parent1).filter(Module.uuid == collection_uuid).first()

print(collection)
