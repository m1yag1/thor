from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_sa_connection(connection_string, echo=False):
    """ A nice helper function for creating the session and engine required
    for sqlalchemy interactions with the database.
    :param connection:
    :return:
    """
    engine = create_engine(connection_string, echo=echo)
    Session = sessionmaker(bind=engine)
    session = Session()
    return engine, session
