import sqlite3


class DataBase:

    def __init__(self, path_to_db="nispa.sqlite"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None,
                fetchone=False, fetchall=False, commit=False):

        if not parameters:
            parameters = tuple()
        with self.connection as connect:

            cursor = connect.cursor()
            connect.set_trace_callback(logger)
            try:
                cursor.execute(sql, parameters)
            except Exception as e:
                print(f"An error occurred: {e}")
            data = None

            if commit:
                connect.commit()
            if fetchone:
                data = cursor.fetchone()

            if fetchall:
                data = cursor.fetchall()

        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        user_id int NOT NULL,
        username varchar(255) NOT NULL,
        full_name varchar(255) NOT NULL,
        lang_code varchar(50) NOT NULL,
        is_premium varchar(50) NOT NULL,
        register_time varchar(255) NOT NULL,
        PRIMARY KEY (user_id)
        );
        """
        self.execute(sql, commit=True)

    def add_user(self, user_id: int, username: str, full_name: str,
                 lang_code: str, is_premium: str, register_time: str):
        sql = "INSERT INTO Users(user_id, username, full_name, lang_code, is_premium, register_time) VALUES(?,?,?,?,?,?)"
        parameters = (user_id, username, full_name, lang_code, is_premium, register_time)
        self.execute(sql, parameters=parameters, commit=True)

    def select_all_users(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE user_id = ? OR user_name = ?"
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_email(self, email: str, user_id: int):
        sql = "UPDATE Users SET email = ? WHERE user_id = ?"
        return self.execute(sql, parameters=(email, user_id), commit=True)

    def delete_users(self):
        return self.execute("DELETE FROM Users WHERE TRUE", commit=True)

    def delete_user(self, user_id: int):
        sql = "DELETE FROM Users WHERE user_id = ?"
        return self.execute(sql, parameters=(user_id,), commit=True, fetchone=True)

    def select_username(self, user_id: int):
        sql = "SELECT username FROM Users WHERE user_id = ?"
        return self.execute(sql, parameters=(user_id, ), fetchone=True)

def logger(statement):
    print(f""" 
-----------------------------------------------------------------------------------------------------
Executing: 
{statement}
-----------------------------------------------------------------------------------------------------    
""")
