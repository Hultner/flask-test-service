"""Experiment script for databases

I use this script as a place to hack around with SQL Alchemy, should not be
seen as a part of the project.
"""
from test_service.util.jsontools import json_dump, json, ExtendedEncoder
from datetime import datetime
from functools import reduce
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta
from test_service import config



Base = declarative_base()

print(config.DB_USER)
print(config.DB_PASSWORD)
print(config.DB_HOST)
print(config.DB_PORT)




print(json.dumps(datetime.now(), cls=ExtendedEncoder))
json_dump(datetime.now())



def connect(user, password, database, schema, host='localhost', port=5432):
    """Returns a connection and a metadata object"""
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, database)

    # The return value of create_engine() is our connection object
    con = create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = MetaData(bind=con, schema=schema, reflect=True)

    return con, meta


connection, meta = connect(config.DB_USER, config.DB_PASSWORD,
                               config.DB_DATABASE, 'flask_test',
                               config.DB_HOST, config.DB_PORT)

connection.echo = True
Session = sessionmaker(bind=connection)
for table in meta.tables:
    print(table)

#table = metadata.tables['{}.note'.format(config.DB_SCHEMA)]
#data = connection.execute(table.select())

#notes = Table('note', metadata, autoload=True, autoload_with=connection, schema=config.DB_SCHEMA)

# for note in data:
#     print(note)


class Note(Base):
    #__table__ = Table('note', meta, autoload=True, autoload_with=connection, schema=config.DB_SCHEMA)
    __table__ = Table('note', meta, autoload=True, schema=config.DB_SCHEMA)
    #__tablename__ = "note"

    """Model for notes"""
    def as_dict(self):
        """ Return dict representation of model """
        return {column.name: getattr(self, column.name)
                for column in self.__table__.columns}

    @property
    def json(self):
        """ Return json representation of model """
        return json.dumps(self.as_dict(), cls=ExtendedEncoder)

    def __repr__(self):
        param_string = reduce(
            (lambda prev, col: "{} {}='{}',".format(prev, col.name, getattr(self, col.name))),
            self.__table__.columns, ""
        ).strip(", ")
        return "<{}({})>".format(self.__class__.__name__, param_string)



def json_print(table_proxy):
    """Prints a ResultProxy array as a json object

    Args:
        table_proxy: ResultProxy of rows from a database query
    """
    print(json.dumps([(dict(row.items())) for row in table_proxy]))

session = Session()

#json_print(data.fetchall())
print("Test----")
#print(notes)
#json_print(notes.select().execute())
# print(data.fetchone().items())
note_test = session.query(Note).all()
#Note()
print(note_test)
#json_print(note_test)
for note in note_test:
    print(note)
    print(note.as_dict())
    print(note.json)

#note_1 = session.query(Note).filter(Note.id == 1).one()
#print("Fetched note by id")
#print(note_1.json)

print("Full json")
print(json_dump(note_test))
"""
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
"""
