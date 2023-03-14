import argparse
try:
    import queue  # Python 3.x
except ImportError:
    import Queue as queue  # Python 2.x
import sys
import threading

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('filename', help='audio file to be played back')