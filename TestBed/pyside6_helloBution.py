from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class HelloCounter(QWidget):
    def __init__(self):
        super().__init__()

        # Counter variable
        self.count = 0

        # Create UI elements
        self.label = QLabel(f"Hello World {self.count}")
        self.button = QPushButton("Add +1")

        # Connect the button click to the method
        self.button.clicked.connect(self.increment_count)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle("Hello World Counter")
        self.setFixedSize(300, 150)

    def increment_count(self):
        self.count += 1
        self.label.setText(f"Hello World {self.count}")

# Run the app
app = QApplication([])
window = HelloCounter()
window.show()
app.exec()
