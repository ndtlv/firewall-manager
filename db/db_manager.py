import logging
from functools import wraps
from typing import Union, Optional

from .models import db, Firewall, FirewallRule, FilteringPolicy

MODELS = [Firewall, FirewallRule, FilteringPolicy]


class DBManager:
    """
    A service called to manage all interactions with the chosen Sqlite database
    """
    def __init__(self, database):
        self._db = database

    def open(self):
        if self._db.is_closed():
            self._db.connect()

    def close(self):
        if not self._db.is_closed():
            self._db.close()

    @staticmethod
    def db_connection(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self.open()
            result = func(self, *args, **kwargs)
            self.close()

            return result
        return wrapper

    @db_connection
    def init(self):
        self._db.create_tables(MODELS)
        logging.debug('Database init successful')

    @db_connection
    def create_row(self, model: Union[*MODELS], config: dict):
        try:
            row = model.create(**config)
            row.save()
        except Exception as error:
            logging.error(f'Error when creating instance of {model} from {config}: {error}')
            raise
        else:
            return row

    @db_connection
    def get_row(self, model: Union[*MODELS], row_id: str, return_field: Optional[str] = None):
        try:
            row = model.select().where(model.id == row_id).get()
        except Exception as error:
            logging.error(f'Error when searching for row with id {row_id} in {model}: {error}')
            raise
        else:
            return getattr(row, return_field) if return_field else row

    @db_connection
    def get_rows(self, model: Union[*MODELS], row_id: Optional[str] = None):
        if row_id:
            return [self.get_row(model, row_id)]

        try:
            rows = list(model.select())
        except Exception as error:
            logging.error(f'Error when searching for rows in {model}: {error}')
            raise
        else:
            return rows

    @db_connection
    def delete_row(self, model: Union[*MODELS], row_id: str):
        try:
            query = model.delete().where(model.id == row_id)
            query.execute()
        except Exception as error:
            logging.error(f'Error when deleting row {row_id} in {model}: {error}')
            raise

    @db_connection
    def update_row(self, model: Union[*MODELS], row_id: str, config: dict):
        try:
            query = model.update(**config).where(model.id == row_id)
            query.execute()

            row = model.select().where(model.id == row_id).get()
        except Exception as error:
            logging.error(f'Error when updating row {row_id} in {model} with data {config}: {error}')
            raise
        else:
            return row


db_manager = DBManager(db)
