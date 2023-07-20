import redis


class PagesRepository:
    def __new__(cls):
        """Реализация синглтона, чтобы объект бд был один"""
        if not hasattr(cls, "instance"):
            cls.instance = super(PagesRepository, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.rdb = redis.Redis()

    def add(self, key: int, type: str, value: int) -> None:
        self.rdb.set(key, value)

    def exists(self, key: int, type: str) -> bool:
        return bool(self.rdb.exists(key))

    def decr(self, key: int, type: str) -> None:
        self.rdb.decr(key)

    def get(self, key: int, type: str) -> str:
        return self.rdb.get(key)

    def increment(self, key: int, type: str) -> None:
        self.rdb.incr(key)





