from PySide6.QtWidgets import QApplication, QLabel, QWidget
from GabesPythonToolBox.PySide6.Utility.LoadIcon import LoadIcon

app = QApplication([])

# Load icon


# Create window
window = QWidget()
window.setWindowTitle("Hello World Window")

icon = LoadIcon()  # or your relative path
if icon:
    window.setWindowIcon(icon)

# Add label inside the window
label = QLabel("Hello, World!", parent=window)
label.move(50, 50)  # optional: position inside the window

# Set window size and show
window.resize(400, 300)
window.show()

app.exec()
