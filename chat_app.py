import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class ChatWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Main layout with avatar/left column and chat area
        main_layout = QtWidgets.QHBoxLayout()
        self.setLayout(main_layout)

        # Left column: avatar at top
        left_layout = QtWidgets.QVBoxLayout()
        avatar_label = QtWidgets.QLabel()
        avatar_pixmap = QtGui.QPixmap("your_avatar.png")
        avatar_pixmap = avatar_pixmap.scaled(120, 120, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        avatar_label.setPixmap(avatar_pixmap)
        left_layout.addWidget(avatar_label)
        left_layout.addStretch()
        main_layout.addLayout(left_layout)

        # Right column: chat area and input row
        chat_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(chat_layout)

        # Chat display area
        self.chat_display = QtWidgets.QTextBrowser()
        self.chat_display.setStyleSheet(
            """
            QTextBrowser {
                background: #001f3f;
                color: white;
                border: none;
                font: 14px;
            }
            """
        )
        chat_layout.addWidget(self.chat_display, stretch=1)

        # Bottom input row with logo, text field, and send button
        input_layout = QtWidgets.QHBoxLayout()

        logo_label = QtWidgets.QLabel()
        logo_pixmap = QtGui.QPixmap("Logo.png.png")
        logo_pixmap = logo_pixmap.scaled(40, 40, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        logo_label.setPixmap(logo_pixmap)
        input_layout.addWidget(logo_label)

        self.user_input = QtWidgets.QLineEdit()
        self.user_input.setPlaceholderText("Enter message...")
        input_layout.addWidget(self.user_input, stretch=1)

        send_button = QtWidgets.QPushButton("Send")
        send_button.clicked.connect(self.handle_send)
        input_layout.addWidget(send_button)

        chat_layout.addLayout(input_layout)

        # Window settings
        self.setWindowTitle("Chat Interface")
        self.setMinimumSize(600, 400)

    def handle_send(self):
        message = self.user_input.text().strip()
        if message:
            self.append_message("You", message)
            response = "Model response for: " + message
            self.append_message("Agent", response)
            self.user_input.clear()

    def append_message(self, sender, text):
        formatted = f"<b>{sender}:</b> {text}"
        self.chat_display.append(formatted)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())
