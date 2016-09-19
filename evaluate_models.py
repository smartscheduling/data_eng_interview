"""
Write an implementation of the function evaluate_models()

evaluate_models() should take a dictionary of models, a test set and labels as input,
and it should print out a text evaluation report.

Input parameters:
models: A dictionary with model names as keys, and trained model objects as values.
test_set: A pandas DataFrame containing a standard set of features.
labels: A pandas Series containing the label values (0 or 1) for the test set.

The output report should contain the following information:
    - A table with the precision, recall and fscore for each model
    - A visual plot containing precision, recall and fscore per model

Optional extras:
    1. If any of the passed in models fail with an error, it should be raised and logged correctly.
        Similarly, if the test set and labels do not match, an error should be correctly raised and logged
    2. The report should include the 5 samples with the most false-positive predictions across all models

"""

def evaluate_models(models, test_set, labels):
    pass


if __name__ == '__main__':
    import pandas as pd
    import numpy as np

    class Model1:
        def predict(self, X):
            return np.zeroes(len(X))

    class Model2:
        def predict(self, X):
            return np.ones(len(X))

    class Model3:
        def predict(self, X):
            return np.random.randint(2, size=len(X))

    class Model4:
        def predict(self, X):
            raise Exception("Something went wrong")

    class Model5:
        def predict(self, X):
            return np.ones(len(X) // 2)

    test_set = pd.DataFrame()
    test_set['a'] = np.random.randint(10, size=1000)
    test_set['b'] = np.random.randint(100, size=1000)
    test_set['c'] = np.random.randint(50, size=1000)
    test_set['d'] = np.random.randint(200, size=1000)
    test_set['e'] = np.random.randint(400, size=1000)

    labels = pd.Series(np.random.randint(2, size=1000))

    models_a = {
        'model1': Model1(),
        'model2': Model2(),
        'model3': Model3()
    }

    models_b = {
        'model1': Model1(),
        'model2': Model2(),
        'model3': Model3(),
        'model4': Model4()
    }

    models_c = {
        'model1': Model1(),
        'model2': Model2(),
        'model3': Model3(),
        'model4': Model4(),
        'model5': Model5()
    }

    evaluate_models(models_a, test_set, labels)
    evaluate_models(models_b, test_set, labels)
    evaluate_models(models_c, test_set, labels)



