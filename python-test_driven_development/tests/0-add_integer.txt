import sys
import os
import importlib.util
import unittest

# 1. Ajouter le dossier parent au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# 2. Charger le fichier manuellement
spec = importlib.util.spec_from_file_location(
    "add_integer",  # nom qu'on lui donne
    os.path.join(os.path.dirname(__file__), '..', '0-add_integer.py')
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
