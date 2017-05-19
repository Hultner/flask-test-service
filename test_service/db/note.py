"""Experiment script for databases

I use this script as a place to hack around with SQL Alchemy, should not be
seen as a part of the project.
"""
import sqlalchemy
import json
from test_service import config

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
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, schema=schema, reflect=True)

    return con, meta


connection, metadata = connect(config.DB_USER, config.DB_PASSWORD,
                               config.DB_DATABASE, 'flask_test',
                               config.DB_HOST, config.DB_PORT)
connection.echo = True
for table in metadata.tables:
    print(table)

table = metadata.tables['{}.note'.format(config.DB_SCHEMA)]
data = connection.execute(table.select())

# for note in data:
#     print(note)

class Note:
    def as_dict(self):
        return { column.name: getattr(self, column.name) for column in self.__table__.columns }


def json_print(table_proxy):
    """Prints a ResultProxy array as a json object
    
    Args: 
        table_proxy: ResultProxy of rows from a database query
    """
    print(json.dumps([(dict(row.items())) for row in table_proxy]))

jsonPrint(data.fetchall())
print("Test----")
#print(data.fetchone().items())


"""
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
"""