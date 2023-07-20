import sqlite3
import os

from models.models import User


class Users:
    def __new__(cls):
        """Реализация синглтона, чтобы объект бд был один"""
        if not hasattr(cls, "instance"):
            cls.instance = super(Users, cls).__new__(cls)
        return cls.instance
    
    def __init__(self) -> None:
        self.conn = sqlite3.connect(os.path.join("db.db"))
        self.cursor = self.conn.cursor()

    def is_user_exists(self, telegram_id: int) -> bool:
        result = self.cursor.execute("""SELECT telegram_id FROM users WHERE
                                     (telegram_id == ?)""", (telegram_id,))
        return len(self.cursor.fetchall()) > 0

    def add_new_user(self, user: User) -> None:
        print(user)
        a = self.cursor.execute(f"""
        INSERT INTO users 
        (telegram_id, first_name, last_name, username, uc_count)
        VALUES (?, ?, ?, ?, ?)""", user.to_tuple())
        print(a)
        self.conn.commit()

    def delete_user(self, telegram_id: int) -> None:
        self.cursor.execute("""
        DELETE FROM users 
        WHERE 
        telegram_id == ?""", (telegram_id,))
        self.conn.commit()

    def update_useful_count(self, telegram_id: int) -> None:
        self.cursor.execute("""
        UPDATE users 
        SET 
        uc_count = uc_count + 1
        WHERE telegram_id == ?""", (telegram_id,))
        self.conn.commit()

