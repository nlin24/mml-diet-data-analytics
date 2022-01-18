import re
import sqlite3
import os
import datetime

class Db_utils:
    def __init__(self, database='mmlmy.db', table='diet'):
        database_exist = self.check_exist(database)
        if not database_exist:
            raise FileNotFoundError(
            f'Database {database} does not exists')
        try:
            self.connection = sqlite3.connect(database)
            self.cursor = self.connection.cursor()
            self.table = table
            self.database = database
        except sqlite3.Error as err:
            print(err)
        
    def __del__(self):
        self.connection.close()

    def check_exist(self, path_to_database):
        return os.path.exists(path_to_database)

    def get_today_date(self):
        return int(datetime.date.today().strftime('%Y%m%d'))

    def insert_diet(self, diet):
        """
        Insert 1 into food column in the diet table for today
        If a row already created for today, update_diet_existing_date
        If row for today not yet exist (check_today_exist), insert_diet_new_date
        If column does not exist (check_diet_exist), add_diet   
        """
        today = self.get_today_date()
        if not self.check_diet_column_exist(diet):
            self.add_diet_column(diet)
        if self.check_date_row_exist(today):
            self.update_diet_existing_date(diet=diet, existing_date=today)
        else:
            self.insert_diet_new_date(diet=diet, new_date=today)


    def get_diet_on_a_date(self, date):
        command = (
            f"SELECT * from {self.table} "
            f"WHERE date = {date};"
        )
        self.cursor.execute(command)
        self.connection.commit()
        results = self.cursor.fetchall()
        return results

    def update_diet_existing_date(self, diet, existing_date):
        command = (
            f"UPDATE {self.table} "
            f"SET {diet} = 1 "
            f"WHERE date = {existing_date};"
        )
        self.cursor.execute(command)
        self.connection.commit()

    def insert_diet_new_date(self, diet, new_date):
        command = (
            f"INSERT INTO {self.table} "
            f"(date, {diet}) " # columns
            f"VALUES ({new_date}, 1);"  # values
        )
        self.cursor.execute(command)
        self.connection.commit()
    
    def add_diet_column(self, diet):
        command = (
            f"ALTER table {self.table} "
            f"ADD column {diet}"
        )
        self.cursor.execute(command)
        self.connection.commit()

    def check_diet_column_exist(self, diet):
        try:
            command = (
                f"SELECT {diet} from {self.table};"
            )
            self.cursor.execute(command)
            self.connection.commit()
            return True
        except sqlite3.Error as err:
            return False


    def check_date_row_exist(self, lookup_date):
        command = (
            f"SELECT date from {self.table} "
            f"WHERE date = {lookup_date};"
        )
        self.cursor.execute(command)
        self.connection.commit()
        result = self.cursor.fetchall()
        return len(result) > 0




        
        
