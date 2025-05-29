from prettytable import PrettyTable

class RawReport:
    def __init__(self, title, strategy):
        self.title = title
        self.strategy = strategy

    def build(self, logs):
        return self.strategy.generate(logs)

class PrettyPrintReport:
    def __init__(self, raw_report):
        self.raw_report = raw_report

    def build_and_display(self, logs):
        data = self.raw_report.build(logs)
        title = self.raw_report.title
        print("\n" + "-" * 42)
        print(f"-------- {title.upper()} --------")
        print("-" * 42)

        if title == "ESTADO POR SALA":
            for sala, estados in data.items():
                print(f"{sala}: {', '.join(estados)}")

        elif title == "ALERTAS CRÍTICAS":
            table = PrettyTable(["timestamp", "sala", "estado", "temperatura", "humedad", "co2"])
            for log in data:
                table.add_row([log.timestamp, log.sala, log.estado, log.temperatura, log.humedad, log.co2])
            print(table)

        elif title == "ESTADÍSTICAS POR SALA":
            table = PrettyTable(["SALA", "registros", "temp_max", "temp_min", "promedio_temperatura", "promedio_humedad", "promedio_co2"])
            for sala, stats in data.items():
                table.add_row([sala, stats["registros"], stats["temp_max"], stats["temp_min"], stats["promedio_temperatura"], stats["promedio_humedad"], stats["promedio_co2"]])
            print(table)

        elif title == "ESTADÍSTICAS CADA 5 MINUTOS":
            for timestamp, salas in data.items():
                print(f"\n>> {timestamp}")
                table = PrettyTable(["Sala", "Logs", "Warnings", "Temp", "Humedad", "CO2"])
                for sala, stats in salas.items():
                    table.add_row([sala, stats["count"], stats["warnings"], stats["avg_temp"], stats["avg_humidity"], stats["avg_co2"]])
                print(table)