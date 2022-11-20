from core.config import *
from dbapi.available_dbnames import AvailableDBs
from peewee import *
from dbapi.exceptions.wrong_dbname import WrongDBNameException

match(SERVER):
    case AvailableDBs.postgresql:
        db = PostgresqlDatabase(
            DB_NAME, user=USERNAME, password=PASSWORD,
            host=HOST, port=PORT)
    case AvailableDBs.mysql:
        db = MySQLDatabase(
            DB_NAME, user=USERNAME, password=PASSWORD,
            host=HOST, port=PORT)
    case _:
        raise WrongDBNameException()


class Student(Model):
    student_id = IntegerField(primary_key=True)
    name = TextField(null=False)
    surname = TextField(null=False)
    patronymic = TextField(null=False)
    course = SmallIntegerField(null=False)
    group = SmallIntegerField(null=False)
    is_budget = BooleanField(null=False)
    is_expelled = BooleanField(null=False, default=False)
    telegram_id = BigIntegerField(null=False)

    class Meta:
        database = db


db.connect()
db.create_tables([Student])
