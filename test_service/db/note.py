"""Experiment script for databases

Author: Alexander Hultnér, 2017

I use this script as a place to hack around with SQL Alchemy, should not be
seen as a part of the project.
"""
from functools import reduce
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from test_service import config
from test_service.util.jsontools import json_dump, json, ExtendedEncoder

print(config.DB_USER)
print(config.DB_PASSWORD)
print(config.DB_HOST)
print(config.DB_PORT)


def connect(user, password, database, schema, host='localhost', port=5432):
    """Returns a connection and a metadata object"""
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, database)

    # The return value of create_engine() is our connection object
    con = create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    metadata = MetaData(bind=con, schema=schema, reflect=True)

    return con, metadata


Base = declarative_base()
connection, meta = connect(config.DB_USER, config.DB_PASSWORD,
                           config.DB_DATABASE, 'flask_test', config.DB_HOST,
                           config.DB_PORT)
connection.echo = True


class Note(Base):
    """ Model for notes
    ORM Class reflecting the database implementation
    """
    __table__ = Table('note', meta, autoload=True, schema=config.DB_SCHEMA)

    def as_dict(self):
        """ Return dict representation of model """
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }  # pylint: disable=E1133

    @property
    def json(self):
        """ Return json representation of model """
        return json.dumps(self.as_dict(), cls=ExtendedEncoder)

    def __repr__(self):
        param_string = reduce(
            (lambda prev, col: "{} {}='{}',"
             .format(prev, col.name, getattr(self, col.name))),
            self.__table__.columns, "").strip(", ")
        return "<{}({})>".format(self.__class__.__name__, param_string)


def json_print(table_proxy):
    """Prints a ResultProxy array as a json object

    Args:
        table_proxy: ResultProxy of rows from a database query
    """
    print(json.dumps([(dict(row.items())) for row in table_proxy]))


def add_note(title, body):
    session = _create_db_session()
    new_note = Note(title="My first note", body="Lorem ipsum dolor sit amet.")
    session.add(new_note)
    session.commit()
    return new_note.json


def update_note(id_, title, body):
    session = _create_db_session()
    # Expand with actual update
    session.commit()
    return json.dumps(dict(message="Not implemented"))


def _create_db_session():
    Session = sessionmaker(bind=connection)
    return Session()


def main():
    """Entry point"""
    session = _create_db_session()

    for table in meta.tables:
        print(table)

    # json_print(data.fetchall())
    print("Test----")
    # print(notes)
    # json_print(notes.select().execute())
    # print(data.fetchone().items())
    note_test = session.query(Note).all()
    # Note()
    print(note_test)
    # json_print(note_test)
    for note in note_test:
        print(note)
        print(note.as_dict())
        print(note.json)

    # note_1 = session.query(Note).filter(Note.id == 1).one()
    # print("Fetched note by id")
    # print(note_1.json)

    print("Full json")
    print(json_dump(note_test))


if __name__ == "__main__":
    main()
