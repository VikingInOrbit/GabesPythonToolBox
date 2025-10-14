from PySide6.QtGui import QIcon
import os

def LoadIcon(relative_path: str = "Deps\Images\GRLogo_profile.jpg"):
    path = os.path.abspath(relative_path)

    # Load the image
    if not os.path.exists(path):
        print(f"Icon file not found: {path}")
        return None

    icon = QIcon(path)
    if icon.isNull():
        print(f"Failed to load icon: {path}")
        return None

    return icon