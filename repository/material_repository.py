import sqlite3
import os

from models.models import Material

RECORDS_COUNT = 10
class Materials:
    def __new__(cls):
        """Реализация синглтона, чтобы объект бд был один"""
        if not hasattr(cls, "instance"):
            cls.instance = super(Materials, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.conn = sqlite3.connect(os.path.join("db.db"))
        self.cursor = self.conn.cursor()

    def add_material(self, material: Material) -> None:
        self.cursor.execute("""
        INSERT INTO materials
        (who_added, content, type)
        VALUES (?, ?, ?)""", material.to_tuple())
        self.conn.commit()

    def delete_material(self, material_id: int):
        self.cursor.execute("""
        DELETE FROM
        materials 
        WHERE 
        material_id == ?""", (material_id,))
        self.conn.commit()

    def get_own_materials(self,
                          r_count: int,
                          type: str,
                          telegram_id: int,
                          page: int = 1) -> list[tuple[str, str]]:
        if type == "text" or type == "theory":
            self.cursor.execute("""
            SELECT content, reg_time
            FROM
            materials
            WHERE 
            type == ? 
            and
            who_added == ?
            LIMIT
            (?-1)*?, ?""", (type, telegram_id, page, r_count, r_count))
            results = self.cursor.fetchall()
            print("results", results)
            return results

    def change_material(self, material_id: int,
                        new_content: str):
        self.cursor.execute("""
        UPDATE 
        materials
        SET
        content = ?
        WHERE 
        material_id == ?""", (material_id, new_content))

    def count_user_material(self, type: str,
                            telegram_id: int) -> int:
        self.cursor.execute("""
        SELECT 
        COUNT(*)
        FROM 
        materials
        WHERE
        type == ? and who_added == ?""", (type, telegram_id))
        result = self.cursor.fetchone()
        return result[0]

    def count_user_materials_pages(self, type: str,
                                   telegram_id: int,
                                   records_count: int=RECORDS_COUNT):
        material_num = self.count_user_material(type, telegram_id)
        if material_num % records_count == 0:
            return material_num // records_count
        else:
            return material_num // records_count + 1

    def get_id_from_number(self, type: str,
                           telegram_id: int,
                           number: int) -> int:
        self.cursor.execute("""
        SELECT material_id
        FROM 
        materials 
        WHERE 
        who_added == ? AND type == ?
        LIMIT
        ?-1, 1""", (telegram_id, type, number))
        return int(self.cursor.fetchone()[0])

