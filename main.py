from PyQt6.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIntValidator

app = QApplication([])

window = QWidget()
layout = QVBoxLayout()

line_edit = QLineEdit()
line_edit.setValidator(QIntValidator(0, 100))  # Only allows integers between 0 and 100
layout.addWidget(line_edit)

button = QPushButton("Submit")
layout.addWidget(button)

window.setLayout(layout)
window.show()
app.exec()