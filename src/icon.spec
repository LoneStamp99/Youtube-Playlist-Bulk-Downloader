# my_scripts.spec

# Import the required module
from PyInstaller.utils.win32 import Icon

# Specify the path to the icon file
icon_path = 'icon/icon.ico'

# Set the icon for the executables
exe1 = Icon(icon_path=icon_path)
exe2 = Icon(icon_path=icon_path)
exe3 = Icon(icon_path=icon_path)
