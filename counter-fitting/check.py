import configparser
import sys
import os
simlex_path = "counter-fitting/linguistic_constraints/SimLex-999.txt"

if not os.path.exists(simlex_path):
    print(f"SimLex file not found at {simlex_path}")
else:
    print("found")