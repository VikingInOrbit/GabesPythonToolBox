import random
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QRect

class ColorRectWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.color = QColor("gray")  # start color

    def set_random_color(self):
        # Generate random RGB values (0–255)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = QColor(r, g, b)
        self.update()  # trigger repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(self.color)
        painter.drawRect(QRect(50, 30, 200, 100))  # x, y, width, height


class HelloCounter(QWidget):
    def __init__(self):
        super().__init__()

        # Counter variable
        self.count = 0

        # Create UI elements
        self.label = QLabel(f"Hello World {self.count}")
        self.button = QPushButton("Add +1 and Change Color")
        self.rect_widget = ColorRectWidget()

        # Connect button
        self.button.clicked.connect(self.increment_and_recolor)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.rect_widget)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        self.setLayout(layout)

        # Window setup
        self.setWindowTitle("Hello World + Random Color Box")
        self.setFixedSize(320, 300)

    def increment_and_recolor(self):
        self.count += 1
        self.label.setText(f"Hello World {self.count}")
        self.rect_widget.set_random_color()


# Run the app
app = QApplication([])
window = HelloCounter()
window.show()
app.exec()
