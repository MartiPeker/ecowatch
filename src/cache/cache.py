from collections import deque
from datetime import datetime, timedelta

class Cache:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Cache, cls).__new__(cls)
            cls._instance.logs = deque()
        return cls._instance

    def add_log(self, log):
        now = datetime.now()
        five_min_ago = now - timedelta(minutes=5)
        self.logs.append(log)
        while self.logs and self.logs[0].timestamp < five_min_ago:
            self.logs.popleft()

    def get_logs_by_sala(self, sala):
        return [log for log in self.logs if log.sala == sala]

    def get_logs_by_timestamp(self, ts):
        ts_dt = datetime.fromisoformat(ts)
        return [log for log in self.logs if log.timestamp == ts_dt]