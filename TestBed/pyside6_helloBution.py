import random
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtGui import QPainter, QColor, QFont
from PySide6.QtCore import QRect, Qt
from GabesPythonToolBox.PySide6.Utility.LoadFont import LoadFont

class ColorRectWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.color = QColor("gray")  # initial color

    def set_random_color(self):
        # Generate random RGB values (0–255)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = QColor(r, g, b)
        self.update()  # trigger repaint

    def paintEvent(self, event):
        """Draw a rectangle that scales with widget size and is centered."""
        painter = QPainter(self)

        w = self.width()
        h = self.height()

        # Rectangle as a percentage of widget size
        rect_width = int(w * 0.8)
        rect_height = int(h * 0.6)

        # Center rectangle
        x = (w - rect_width) // 2
        y = (h - rect_height) // 2

        painter.setBrush(self.color)
        painter.drawRect(QRect(x, y, rect_width, rect_height))


class HelloCounter(QWidget):
    def __init__(self):
        super().__init__()

        # Counter
        self.count = 0

        # Widgets
        self.label = QLabel(f"Hello World {self.count}")
        self.button = QPushButton("Add +1 and Change Color")
        self.rect_widget = ColorRectWidget()

        # Connect button click
        self.button.clicked.connect(self.increment_and_recolor)

        # Layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # remove borders
        layout.setSpacing(5)
        layout.addWidget(self.rect_widget)
        layout.addWidget(self.label,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.button)
        self.setLayout(layout)

        font = LoadFont()
        font.setPointSize(18)  # text size in points
        self.label.setFont(font)
        self.button.setFont(font)

        # Window settings
        self.setWindowTitle("Hello World + Random Color Box")
        self.setMinimumSize(320, 300)  # allows resizing
        self.resize(400, 350)  # initial size

    def increment_and_recolor(self):
        self.count += 1
        self.label.setText(f"Hello World {self.count}")
        self.rect_widget.set_random_color()


# Run the app
if __name__ == "__main__":
    app = QApplication([])
    window = HelloCounter()
    window.show()
    app.exec()
