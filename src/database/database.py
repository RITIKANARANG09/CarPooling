import sqlite3
from src.config.app_config import AppConfig
from src.helper.logs import Log
import logging
logger = logging.getLogger(__name__)
class Database:
    def __init__(self):
        self.connection=sqlite3.connect(AppConfig.DATABASE_PATH)
        self.cursor=self.connection.cursor()

    def add_data(self, query: str, data:tuple) -> None:
        self.cursor.execute(query,data)
        self.connection.commit()
        logger.info(Log.ADDED_DATA)

    def get_data(self, query: str, data: tuple = None):
        if data is not None:
            self.cursor.execute(query,data)
        else:
            self.cursor.execute(query)
        result= self.cursor.fetchall()

        if result:
            logger.info(Log.FETCHED_DATA)
            return result
        else:
            return None

    def delete_data(self,query,value:tuple):
        self.cursor.execute(query,value)
        self.connection.commit()
        logger.info(Log.DELETED_DATA)

