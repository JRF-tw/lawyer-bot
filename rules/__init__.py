'''
Find all rules in `rules` directory.
'''
def __find_rules__():
    import os
    import importlib
    import inspect

    classes = {}
    for f in os.listdir(os.path.dirname(__file__)):
        name, ext = os.path.splitext(f)
        if ext == '.py' and name != '__init__':
            module = importlib.import_module('.' + name, __name__)
            classes.update(inspect.getmembers(module, inspect.isclass))
    return classes

globals().update(__find_rules__())
