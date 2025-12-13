import numpy as np
from abc import ABC, abstractmethod
from sklearn.metrics import accuracy_score, f1_score, precision_score

#Q1
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

# --- 4. The Context (Evaluator) ---
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

if __name__ == "__main__":
    # Generate random data (100 samples)
    # X shape: (100 samples)
    X = np.random.rand(100) 
    y_true = np.random.randint(0, 2, 100)

    # Initialize the model
    my_model = DummyModel()

    # Initialize the evaluator
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