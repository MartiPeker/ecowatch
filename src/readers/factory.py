from src.readers.csv_reader import CSVLogReader

class LogReaderFactory:
    @staticmethod
    def get_reader(format, path):
        if format == 'csv':
            return CSVLogReader(path)
        raise ValueError("Formato no soportado")