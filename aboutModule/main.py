import importlib

test = importlib.import_module('test_module')
print dir(test)
if hasattr(test, "BROKER_URL"):
    print test.BROKER_URL
print dir()
