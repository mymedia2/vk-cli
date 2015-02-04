#!/usr/bin/env python3
import unittest, argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", default=2, type=int)
v = parser.parse_args().verbosity
loader = unittest.TestLoader()
suite = loader.discover(start_dir="tests", pattern="*.py")
runner = unittest.TextTestRunner(verbosity=v)
result = runner.run(suite)
