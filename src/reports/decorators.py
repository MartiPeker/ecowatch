import json
import csv
import os

class ReportComponent:
    def build_and_display(self, logs):
        raise NotImplementedError

class RawReport(ReportComponent):
    def __init__(self, title, strategy):
        self.title = title
        self.strategy = strategy

    def build_and_display(self, logs):
        return self.strategy.generate(logs)

class PrettyPrintReport(ReportComponent):
    def __init__(self, report_component):
        self.report_component = report_component

    def build_and_display(self, logs):
        print("\n" + "-" * 42)
        print(f"-------- {self.report_component.title.upper()} --------")
        print("-" * 42)
        result = self.report_component.strategy.generate(logs)

        if isinstance(result, dict):
            if all(isinstance(v, dict) for v in result.values()):
                self._print_dict_of_dicts(result)
            elif all(isinstance(v, list) for v in result.values()):
                self._print_dict_of_lists(result)
            else:
                print(result)
        elif isinstance(result, list) and result and hasattr(result[0], '__dict__'):
            self._print_object_list(result)
        else:
            print(result)

        return result

    def _print_dict_of_dicts(self, data):
        headers = ["SALA"] + list(next(iter(data.values())).keys())
        rows = [[sala] + list(map(str, data[sala].values())) for sala in sorted(data)]
        self._print_table(headers, rows)

    def _print_dict_of_lists(self, data):
        for key in sorted(data.keys()):
            print(f"{key}: {', '.join(data[key])}")

    def _print_object_list(self, data):
        headers = ["timestamp", "sala", "estado", "temperatura", "humedad", "co2"]
        rows = [[
            str(getattr(obj, "timestamp", "")),
            getattr(obj, "sala", ""),
            getattr(obj, "estado", ""),
            getattr(obj, "temperatura", ""),
            getattr(obj, "humedad", ""),
            getattr(obj, "co2", "")
        ] for obj in data]
        self._print_table(headers, rows)

    def _print_table(self, headers, rows):
        col_widths = [max(len(str(cell)) for cell in column) for column in zip(*([headers] + rows))]
        fmt = " | ".join(f"{{:<{w}}}" for w in col_widths)
        print(fmt.format(*headers))
        print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))
        for row in rows:
            print(fmt.format(*row))

class ExportToFileReport(ReportComponent):
    def __init__(self, report_component, export_format='json'):
        self.report_component = report_component
        self.export_format = export_format

    def build_and_display(self, logs):
        result = self.report_component.build_and_display(logs)
        filename = f"{self.report_component.title.lower().replace(' ', '_')}.{self.export_format}"

        os.makedirs("output", exist_ok=True)
        filepath = os.path.join("output", filename)

        if self.export_format == 'json':
            with open(filepath, "w") as f:
                json.dump(result, f, indent=4)
        elif self.export_format == 'csv' and isinstance(result, dict):
            with open(filepath, "w", newline='') as f:
                writer = csv.writer(f)
                headers_written = False
                for key, value in result.items():
                    if isinstance(value, dict):
                        if not headers_written:
                            writer.writerow(["sala"] + list(value.keys()))
                            headers_written = True
                        writer.writerow([key] + list(value.values()))
        print(f"[Archivo exportado a {filepath}]")
