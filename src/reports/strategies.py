from abc import ABC, abstractmethod
from collections import defaultdict
from statistics import mean
from datetime import datetime, timedelta

class ReportStrategy(ABC):
    @abstractmethod
    def generate(self, logs):
        pass

class ReporteEstadoPorSala(ReportStrategy):
    def generate(self, logs):
        estado_por_sala = defaultdict(list)
        for log in logs:
            estado_por_sala[log.sala].append(log.estado)
        return dict(estado_por_sala)

class ReporteAlertasCriticas(ReportStrategy):
    def generate(self, logs):
        return [log for log in logs if log.estado == "WARNING"]

class ReporteEstadisticasPorSala(ReportStrategy):
    def generate(self, logs):
        stats = {}
        for log in logs:
            sala = log.sala
            if sala not in stats:
                stats[sala] = {
                    "registros": 0,
                    "temperaturas": [],
                    "humedades": [],
                    "co2s": [],
                }
            stats[sala]["registros"] += 1
            stats[sala]["temperaturas"].append(log.temperatura)
            stats[sala]["humedades"].append(log.humedad)
            stats[sala]["co2s"].append(log.co2)

        resumen = {}
        for sala, data in stats.items():
            resumen[sala] = {
                "registros": data["registros"],
                "temp_max": max(data["temperaturas"]),
                "temp_min": min(data["temperaturas"]),
                "promedio_temperatura": round(mean(data["temperaturas"]), 2),
                "promedio_humedad": round(mean(data["humedades"]), 2),
                "promedio_co2": round(mean(data["co2s"]), 2),
            }
        return resumen

class ReporteCada5Minutos(ReportStrategy):
    def generate(self, logs):
        grouped = defaultdict(lambda: defaultdict(list))
        for log in logs:
            bucket = log.timestamp.replace(minute=(log.timestamp.minute // 5) * 5, second=0, microsecond=0)
            grouped[bucket][log.sala].append(log)

        resumen = {}
        for bucket, salas_logs in grouped.items():
            resumen[str(bucket)] = {}
            for sala, logs in salas_logs.items():
                resumen[str(bucket)][sala] = {
                    "count": len(logs),
                    "warnings": sum(1 for l in logs if l.estado == "WARNING"),
                    "avg_temp": round(mean(l.temperatura for l in logs), 2),
                    "avg_humidity": round(mean(l.humedad for l in logs), 2),
                    "avg_co2": round(mean(l.co2 for l in logs), 2),
                }
        return resumen