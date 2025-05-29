class ReportBuilder:
    def __init__(self, strategy):
        self.strategy = strategy

    def build_report(self, logs):
        return self.strategy.generate(logs)