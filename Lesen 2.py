from PyQt6.QtWidgets import*

app = QApplication([])

window = QWidget()

start = QPushButton("Почати")
text_lbl = QLabel("Наша вікторина")
text= QLabel("Переможець вікторини:")
n = QCheckBox("Пвіпкерк")

line.addWidget(text)
main_line.addWidget(start)
main_line.addWidget(text_lbl)
main_line.addWidget(n)


window.setLayout(main_line)

window.show()
app.exec()
