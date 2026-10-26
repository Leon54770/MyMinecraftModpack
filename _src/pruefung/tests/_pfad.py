# Macht _src/ importierbar (snbt, questlib, pruefung.*), egal von wo die Tests laufen.
import os, sys

SRC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if SRC not in sys.path:
    sys.path.insert(0, SRC)
