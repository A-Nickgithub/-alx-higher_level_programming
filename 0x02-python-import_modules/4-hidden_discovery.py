#!/usr/bin/python3
"""
this program prints all the names defined by the compiled
module that is going to be imported here
it should print one name per line
it should print only names that do not start with __
"""
if __name__ == "__main__":
    import importlib.util

    spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for name in sorted(dir(module)):
        if not name.startswith("__"):
            print(name)
