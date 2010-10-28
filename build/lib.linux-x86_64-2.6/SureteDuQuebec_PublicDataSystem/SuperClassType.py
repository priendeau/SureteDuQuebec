import os, sys, re
import pynav
from pynav import Pynav


class MClass(type):
    def __new__(meta, name, bases, attrs):
        return type.__new__(meta, name, bases, attrs)
