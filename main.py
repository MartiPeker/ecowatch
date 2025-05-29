from src.readers.factory import LogReaderFactory
from src.reports.strategies import (
    ReporteEstadoPorSala,
    ReporteAlertasCriticas,
    ReporteEstadisticasPorSala,
    ReporteCada5Minutos
)
from src.reports.builder import ReportBuilder
from src.reports.decorator import PrettyPrintReport, RawReport

reader = LogReaderFactory.get_reader('csv', 'logs_ambientales_ecowatch.csv')
logs = reader.read_logs()

#PrettyPrintReport(RawReport("ESTADO POR SALA", ReporteEstadoPorSala())).build_and_display(logs)
PrettyPrintReport(RawReport("ESTADÍSTICAS POR SALA", ReporteEstadisticasPorSala())).build_and_display(logs)
PrettyPrintReport(RawReport("ALERTAS CRÍTICAS", ReporteAlertasCriticas())).build_and_display(logs)
PrettyPrintReport(RawReport("ESTADÍSTICAS CADA 5 MINUTOS", ReporteCada5Minutos())).build_and_display(logs)