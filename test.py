import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simple PyQt6 Window")
        self.setGeometry(100, 100, 300, 200)  # Window size (x, y, width, height)

        # Label to show status
        self.label = QLabel("Click 'Click Me'", self)

        # Button to update label
        self.button = QPushButton("Click Me", self)
        self.button.clicked.connect(self.update_label)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def update_label(self):
        self.label.setText("Button Clicked")

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleApp()
    window.show()
    sys.exit(app.exec())
