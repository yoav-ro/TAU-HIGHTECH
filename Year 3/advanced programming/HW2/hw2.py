import numpy as np
from abc import ABC, abstractmethod
from sklearn.metrics import accuracy_score, f1_score, precision_score
import gc
from datetime import datetime

# --- Part 1 ---

# Q1

class DummyModel:
    """A mock model that returns random predictions for testing purposes."""
    def __init__(self):
        self.model = ''

    def predict(self, X):
        """Return random 0 and 1 values for each sample in X."""
        return np.random.randint(0, 2, len(X))

def eval_accuracy(y_true, y_pred):
    """Strategy: Calculate Accuracy score."""
    return accuracy_score(y_true, y_pred)

def eval_f1(y_true, y_pred):
    """Strategy: Calculate F1 score."""
    return f1_score(y_true, y_pred)
  
def eval_precition(y_true, y_pred):
    """Strategy: Calculate Precision score."""
    return precision_score(y_true, y_pred)

class ModelEvaluator:
    """
    The Context class for the Strategy Pattern.
    It maintains a reference to a Strategy (function) and allows switching it at runtime.
    """
    def __init__(self, model, strategy=None):
        self.model = model
        self.strategy = strategy

    def set_strategy(self, strategy):
        """Allows dynamic switching of the evaluation metric."""
        self.strategy = strategy

    def evaluate(self, X, y_true):
        """
        Executes the current strategy on the model's predictions.
        """
        y_pred = self.model.predict(X)
        result = self.strategy(y_true, y_pred)
        return result

def q1_main():
    """Driver code to demonstrate switching strategies (metrics) on the fly."""
    X = np.random.rand(100) 
    y_true = np.random.randint(0, 2, 100)
    my_model = DummyModel()

    evaluator = ModelEvaluator(my_model)

    print("Starting Evaluation:")

    # 1. Set Strategy to Accuracy
    evaluator.set_strategy(eval_accuracy)
    acc = evaluator.evaluate(X, y_true)
    print(f"Accuracy: {acc:.4f}")

    # 2. Set Strategy to F1
    evaluator.set_strategy(eval_f1)
    f1 = evaluator.evaluate(X, y_true)
    print(f"F1 Score: {f1:.4f}")

    # 3. Set Strategy to Precision
    evaluator.set_strategy(eval_precition)
    prec = evaluator.evaluate(X, y_true)
    print(f"Precision: {prec:.4f}")

    print("Evaluation Completed.")


# Q2

class CpuMonitor(ABC):
    """
    Observer Interface.
    All concrete monitors must implement the update method.
    """
    @abstractmethod
    def update(self, usage_percent):
        pass

class CpuSensor:
    """
    The Subject (Observable).
    Maintains a list of observers (monitors) and notifies them of state changes.
    """
    def __init__(self):
        self._monitors = []
        self._cpu_usage = 0

    def attach(self, monitor: CpuMonitor):
        """Subscribes an observer to the subject."""
        if monitor not in self._monitors:
            self._monitors.append(monitor)

    def detach(self, monitor: CpuMonitor):
        """Unsubscribes an observer."""
        if monitor in self._monitors:
            self._monitors.remove(monitor)

    def notify(self):
        """Trigger an update call on all subscribed monitors."""
        for monitor in self._monitors:
            monitor.update(self._cpu_usage)

    def set_cpu_usage(self, value):
        """Updates state and triggers notification."""
        print("CPU usage updated.")
        self._cpu_usage = value
        self.notify()


class LoggingMonitor(CpuMonitor):
    """Observer that logs usage data with timestamps."""
    def __init__(self):
        self._usage_log = {}

    def update(self, usage_percent):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self._usage_log[timestamp] = usage_percent

    def print_log(self):
        print(f"CPU usage logs: {self._usage_log}")

class HighUsageWarningMonitor(CpuMonitor):
    """Observer that prints a warning if usage exceeds a threshold."""
    def __init__(self, threshold=85):
        self.threshold = threshold

    def update(self, usage_percent):
        if usage_percent > self.threshold:
            print("Warning! CPU usages is too high!")

class GcTriggerMonitor(CpuMonitor):
    """Observer that triggers Garbage Collection if usage is critical."""
    def __init__(self, threshold=90):
        self.threshold = threshold

    def update(self, usage_percent):
        if usage_percent > self.threshold:
            print("CPU usage is too high. Engaging Garbage Collegtion.")
            gc_count = gc.collect()
            print(f"Gargage Collection completed. Objects collected: {gc_count}")


def q2_main():
    """Driver code demonstrating multiple observers reacting to single subject updates."""
    sensor = CpuSensor()

    logger = LoggingMonitor()
    warner = HighUsageWarningMonitor()
    gc_monitor = GcTriggerMonitor()

    sensor.attach(logger)
    sensor.attach(warner)
    sensor.attach(gc_monitor)

    sensor.set_cpu_usage(45)
    sensor.set_cpu_usage(88)
    sensor.set_cpu_usage(95)

    logger.print_log()

# Q3

class Logger(ABC):
    """Abstract Product interface."""
    @abstractmethod
    def log(self, message):
        pass

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
    def log(self, message):
        pass

# The Factory
def GetLogger(logger):
    """
    Factory Function.
    Returns the class reference based on the input string string.
    """
    print(f"logger is {logger}")
    logger_map = {
        "console": ConsoleLogger,
        "file": FileLogger,
        "null": NullLogger
    }

    if logger not in logger_map:
        raise ValueError("Logger type doesnt exist")
    return logger_map[logger]

def q3_main():
    # Create a File Logger via Factory
    config_file = {"logger_type": "file", "path": "log_file.txt"}
    logger1 = GetLogger(config_file["logger_type"])(config_file["path"])
    logger1.log("This goes to a file.")

    # Create a Console Logger via Factory
    config_console = {"logger_type": "console"}
    logger2 = GetLogger(config_console["logger_type"])()
    logger2.log("---Printing a message.---")
    
    loggers = [logger1, logger2]
    for logger in loggers:
        logger.log("Working through the same interface!")

# --- Part 2 ---

# Q4(a)
def accumulating_monitor_demo(n=10000, report_every=1000): 
    sensor = CpuSensor() 
    for i in range(n): 
        m = LoggingMonitor()     
        sensor.attach(m) 
        del m
 
        if (i + 1) % report_every == 0: 
            print(f"[A] After {i+1} attachments → monitor count = {len(sensor._monitors)}") 
            print("GC counts:", gc.get_count())

# Q5(b)
import weakref 

class AlternativeCpuSensor:
    def __init__(self):
        self._monitors = weakref.WeakSet() # Does not increment reference count
        self._cpu_usage = 0

    def attach(self, monitor):
        self._monitors.add(monitor)

    def detach(self, monitor):
        self._monitors.discard(monitor)

    def notify(self):
        for monitor in self._monitors:
            monitor.update(self._cpu_usage)

    def set_cpu_usage(self, value):
        print("CPU usage updated.")
        self._cpu_usage = value
        self.notify()

def vanishing_monitor_demo(n=10000, report_every=1000): 
    sensor = AlternativeCpuSensor() 
    for i in range(n): 
        m = LoggingMonitor() 
        sensor.attach(m) 
        del m 
 
        if (i + 1) % report_every == 0: 
            print(f"[B] After {i+1} attachments → monitor count = {len(sensor._monitors)}") 
            print("GC counts:", gc.get_count())

if __name__ == "__main__":
    q1_main()
    q2_main()
    q3_main()
    accumulating_monitor_demo()
    vanishing_monitor_demo()
    pass