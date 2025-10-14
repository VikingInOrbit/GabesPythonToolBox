from PySide6.QtWidgets import QApplication, QLabel

# Create the application
app = QApplication([])

# Create a simple label widget with some text
label = QLabel("Hello, World!")
label.show()  # Display the label in a window

# Run the application's event loop
app.exec()
