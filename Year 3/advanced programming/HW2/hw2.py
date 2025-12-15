import numpy as np
from abc import ABC, abstractmethod
from sklearn.metrics import accuracy_score, f1_score, precision_score
import gc
from datetime import datetime

#---Q1---
class DummyModel:
    def __init__(self):
        self.model = ''

    def predict(self, X):
        """ Return random 0 and 1 values for each sample in X """
        return np.random.randint(0, 2, len(X))

def eval_accuracy(y_true, y_pred):
    return accuracy_score(y_true, y_pred)

def eval_f1(y_true, y_pred):
    return f1_score(y_true, y_pred)
  
def eval_precition(y_true, y_pred):
    return precision_score(y_true, y_pred)

# Strategy pattern main class
class ModelEvaluator:
    """
    This class handles the evaluation process. It takes a model and a 
    strategy, keeping them decoupled.
    """
    def __init__(self, model, strategy=None):
        self.model = model
        self.strategy = strategy

    # Switch strategies during runtime
    def set_strategy(self, strategy):
        self.strategy = strategy

    def evaluate(self, X, y_true):
        # Get predictions from the model
        y_pred = self.model.predict(X)
        result = self.strategy(y_true, y_pred)
        return result

def q1_main():
    X = np.random.rand(100) 
    y_true = np.random.randint(0, 2, 100)
    my_model = DummyModel()

    evaluator = ModelEvaluator(my_model)

    print("Starting Evaluation:")

    # Using Accuracy
    evaluator.set_strategy(eval_accuracy)
    acc = evaluator.evaluate(X, y_true)
    print(f"Accuracy: {acc:.4f}")

    # Using F1
    evaluator.set_strategy(eval_f1)
    f1 = evaluator.evaluate(X, y_true)
    print(f"F1 Score: {f1:.4f}")

    # Using Precision
    evaluator.set_strategy(eval_precition)
    prec = evaluator.evaluate(X, y_true)
    print(f"Precision: {prec:.4f}")

    print("Evaluation Completed.")


#---Q2---

# Abstract base monitor class for all the next monitors to inherit from, to ensure they all have the "upadate" method
class CpuMonitor(ABC):
    @abstractmethod
    def update(self, usage_percent):
        pass

class CpuSensor:
    def __init__(self):
        self._monitors = []
        self._cpu_usage = 0

    def attach_monitor(self, monitor: CpuMonitor):
        if monitor not in self._monitors:
            self._monitors.append(monitor)
            print("New monitor attached.")

    def detach_monitor(self, monitor: CpuMonitor):
        if monitor in self._monitors:
            self._monitors.remove(monitor)
            print("A monitor has been removed.")

    def notify(self):
        for monitor in self._monitors:
            monitor.update(self._cpu_usage)

    def set_cpu_usage(self, value):
        print("CPU usage updated.")
        self._cpu_usage = value
        self.notify()


# Monitor classes
class LoggingMonitor(CpuMonitor):
    def __init__(self):
        self._usage_log = {}

    def update(self, usage_percent):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self._usage_log[timestamp] = usage_percent

    def print_log(self):
        print(f"CPU usage logs: {self._usage_log}")

class HighUsageWarningMonitor(CpuMonitor):
    def __init__(self, threshold=85):
        self.threshold = threshold

    def update(self, usage_percent):
        if usage_percent > self.threshold:
            print("Warning! CPU usages is too high!")

class GcTriggerMonitor(CpuMonitor):
    def __init__(self, threshold=90):
        self.threshold = threshold

    def update(self, usage_percent):
        if usage_percent > self.threshold:
            print("CPU usage is too high. Engaging Garbage Collegtion.")
            gc_count = gc.collect()
            print(f"Gargage Collection completed. Objects collected: {gc_count}")


def q2_main():
    sensor = CpuSensor()

    logger = LoggingMonitor()
    warner = HighUsageWarningMonitor()
    gc_monitor = GcTriggerMonitor()

    sensor.attach_monitor(logger)
    sensor.attach_monitor(warner)
    sensor.attach_monitor(gc_monitor)

    # Simpulate differate useage
    sensor.set_cpu_usage(45)
    sensor.set_cpu_usage(88)
    sensor.set_cpu_usage(95)

    # Print LoggingMonitor's results:
    logger.print_log()

#---Q3---

# Abstract Logger class
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

# All required logger types
class ConsoleLogger(Logger):
    def log(self, message):
        print(f"[Console] {message}")

class FileLogger(Logger):
    def __init__(self, path):
        self.path = path

    def log(self, message):
        with open(self.path, "a") as f:
            f.write(f"{message}\n")

class NullLogger(Logger):
    def log(self):
        pass

def GetLogger(logger="console_logger"):
    print(f"logger is {logger}")
    logger_map={
        "console": ConsoleLogger,
        "file": FileLogger,
        "null": NullLogger
    }

    if logger not in logger_map:
        raise ValueError("Logger type doesnt exist")
    return logger_map[logger]

def q3_main():
    # File logger config
    config_file = {"logger_type": "file", "path": "log_file.txt"}
    logger1 = GetLogger(config_file["logger_type"])(config_file["path"])
    logger1.log("This goes to a file.")

    # Console logger config
    config_console = {"logger_type": "console"}
    logger2 = GetLogger(config_console["logger_type"])()
    logger2.log("---Printing a message.---")
    
    # Console and config through the same interface
    loggers = [logger1, logger2]
    for logger in loggers:
        logger.log("Working through the same interface!")

if __name__ == "__main__":
    # q1_main()
    # q2_main()
    q3_main()
    pass