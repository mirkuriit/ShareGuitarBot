class User:
    def __init__(self, telegram_id: int,
                 first_name: str = None,
                 last_name: str = None,
                 username: str = None,
                 uc_count: int = 0):
        self.telegram_id = telegram_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.uc_count = uc_count

    def to_tuple(self) -> tuple:
        return self.telegram_id, self.first_name, self.last_name, self.username, self.uc_count

    def __str__(self):
        return f"('{self.telegram_id}', " \
               f"'{self.first_name}', " \
               f"'{self.last_name}', " \
               f"'{self.username}'," \
               f" '{self.uc_count}', "


class Material:
    def __init__(self, who_added: int,
                 content: str,
                 type: str):
        self.who_added = who_added
        self.content = content
        self.type = type

    def to_tuple(self) -> tuple:
        return self.who_added, self.content, self.type

