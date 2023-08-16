#/src INIT
# import os

# import importlib.util
# import sys
 
# db_path = os.path.abspath("./src/DB/__init__.py")
# name = "DB"

# spec = importlib.util.spec_from_file_location(name, db_path)
# module = importlib.util.module_from_spec(spec)
# sys.modules[spec.name] = module 
# spec.loader.exec_module(module)

from .calc_v5 import the_calc
