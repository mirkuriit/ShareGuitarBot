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
        self.rdb.set(f"{key}_{type}", value)

    def exists(self, key: int, type: str) -> bool:
        return bool(self.rdb.exists(f"{key}_{type}"))

    def decr(self, key: int, type: str) -> None:
        self.rdb.decr(f"{key}_{type}")

    def get(self, key: int, type: str) -> str:
        return self.rdb.get(f"{key}_{type}")

    def increment(self, key: int, type: str) -> None:
        self.rdb.incr(f"{key}_{type}")





