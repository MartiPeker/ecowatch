from datetime import datetime

class Log:
    def __init__(self, timestamp, sala, estado, temperatura, humedad, co2):
        self.timestamp = datetime.fromisoformat(timestamp)
        self.sala = sala
        self.estado = estado
        self.temperatura = temperatura
        self.humedad = humedad
        self.co2 = co2

    def __repr__(self):
        return f"Log({self.timestamp}, {self.sala}, {self.estado}, T={self.temperatura}, H={self.humedad}, CO2={self.co2})"