import unittest


class TestModuleAvailability(unittest.TestCase):
    def test_flask_available(self):
        try:
            import flask
            flask_available = True
        except ImportError:
            flask_available = False

        self.assertTrue(flask_available, msg="Flask module is not available.")
        if flask_available:
            print("Flask module is installed successfully.")

    def test_mlflow_available(self):
        try:
            import mlflow
            mlflow_available = True
        except ImportError:
            mlflow_available = False

        self.assertTrue(mlflow_available, msg="MLflow module is not available.")
        if mlflow_available:
            print("MLflow module is installed successfully.")

    def test_numpy_available(self):
        try:
            import numpy
            numpy_available = True
        except ImportError:
            numpy_available = False

        self.assertTrue(numpy_available, msg="NumPy module is not available.")
        if numpy_available:
            print("NumPy module is installed successfully.")

    def test_pandas_available(self):
        try:
            import pandas
            pandas_available = True
        except ImportError:
            pandas_available = False

        self.assertTrue(pandas_available, msg="Pandas module is not available.")
        if pandas_available:
            print("Pandas module is installed successfully.")

    def test_requests_available(self):
        try:
            import requests
            requests_available = True
        except ImportError:
            requests_available = False

        self.assertTrue(requests_available, msg="Requests module is not available.")
        if requests_available:
            print("Requests module is installed successfully.")

    def test_scikit_learn_available(self):
        try:
            import sklearn
            scikit_learn_available = True
        except ImportError:
            scikit_learn_available = False

        self.assertTrue(scikit_learn_available, msg="scikit-learn module is not available.")
        if scikit_learn_available:
            print("scikit-learn module is installed successfully.")

    def test_setuptools_available(self):
        try:
            import setuptools
            setuptools_available = True
        except ImportError:
            setuptools_available = False

        self.assertTrue(setuptools_available, msg="Setuptools module is not available.")
        if setuptools_available:
            print("Setuptools module is installed successfully.")

if __name__ == '__main__':
    unittest.main()
