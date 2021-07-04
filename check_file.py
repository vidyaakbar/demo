import os
import test_main
from os import path
import pytest

def check_file(name):
    return path.exists(name)
