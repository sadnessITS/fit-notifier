import enum
from exceptions import WrongDBNameException
from peewee import PostgresqlDatabase, MySQLDatabase


class DBName(enum.IntEnum):
    postgresql = 0,
    mysql = 1,


class DataBaseAPI:
    def __init__(self, database: int, db_file_name: str, user: str,
                 password: str, host: str, port: int):
        '''This is where the parameters to connect the database are passed
            @param database -- server, specify with enum DBName
            @param db_file_name -- database name
            @param user -- username
            @param password -- password for user
            @param host -- host
            @param port -- port
        '''
        self.database: int = database
        self.db_file_name: str = db_file_name
        self.user: str = user
        self.password: str = password
        self.host: str = host
        self.port: int = port

    def get_instanse(self):
        '''Get instance of selected database'''
        match(self.database):
            case DBName.postgresql:
                self.db = PostgresqlDatabase(
                    self.db_file_name, user=self.user, password=self.password,
                    host=self.host, port=self.port)

            case DBName.mysql:
                self.db = MySQLDatabase(self.db_file_name, user=self.user, password=self.password,
                                        host=self.host, port=self.port)

            case _:
                raise WrongDBNameException()

        return self.db
