import sys
import threading
import keyboard  # Module to listen for hotkeys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from backend import recognize_speech, control_spotify  # Import functions from backend

class SpotifyVoiceControlApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        # Start hotkey listener in a separate thread
        self.hotkey_thread = threading.Thread(target=self.listen_for_hotkey, daemon=True)
        self.hotkey_thread.start()

    def initUI(self):
        self.setWindowTitle("Spotify Voice Controller")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel("Press 'Ctrl + Shift + S' to start listening", self)

        self.start_button = QPushButton("Start Listening", self)
        self.start_button.clicked.connect(self.start_listening)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

    def listen_for_hotkey(self):
        """Listens for a hotkey and starts speech recognition when pressed."""
        keyboard.add_hotkey("ctrl+shift+s", self.start_listening)  # Assign hotkey

        # Keep the thread alive to listen continuously
        keyboard.wait()

    def start_listening(self):
        """Calls backend to recognize speech and update UI."""
        self.label.setText("Listening...")
        command = recognize_speech()  # Call backend function
        self.label.setText(f"Recognized: {command}")

        # Control Spotify based on command
        response = control_spotify(command)
        self.label.setText(response)  # Update UI with result

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpotifyVoiceControlApp()
    window.show()
    sys.exit(app.exec())
