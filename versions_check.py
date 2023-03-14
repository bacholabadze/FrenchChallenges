# PyQT6 Version Check
from PyQt6.QtCore import QT_VERSION_STR
print("PyQt5 version: ", QT_VERSION_STR)

# PySide6 Version Check
import PySide6
print("PySide6 version: ", PySide6.__version__)

# Python Version Check
import sys
print("Python Version: ", sys.version)

# Windows Version Check
import platform
print("Windows version: ", platform.platform())


