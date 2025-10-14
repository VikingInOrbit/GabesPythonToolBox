from ...Utility.Debug import *
from PySide6.QtGui import QFontDatabase, QFont
import os

def LoadFont(size:int =8,relative_path:str="Deps\Fonts\ROBOTOMONONERDFONTMONO-REGULAR.TTF"):
    path = os.path.abspath(relative_path)
    
    # Load font from a file
    font_id = QFontDatabase.addApplicationFont(path)
    if font_id != -1:
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family, size)
        return font
    else:
        print("Failed to load font")
        Debug.log(f"Failed to load font","WarningError",group="Error")
        return None
