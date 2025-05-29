import csv
from src.models.log import Log
from src.readers.base_reader import LogReader

class CSVLogReader(LogReader):
    def __init__(self, filepath):
        self.filepath = filepath

    def read_logs(self):
        logs = []
        with open(self.filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if self._validate(row):
                    logs.append(Log(row['timestamp'], row['sala'], row['estado'],
                                     float(row['temperatura']), float(row['humedad']), int(row['co2'])))
        return logs

    def _validate(self, row):
        keys = {'timestamp', 'sala', 'estado', 'temperatura', 'humedad', 'co2'}
        return keys.issubset(row.keys())