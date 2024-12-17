from PyQt6.QtWidgets import*

app = QApplication([])

window = QWidget()

boo = QLabel('В якому році народився Т. Шевченко? ')
radio1 = QRadioButton('1841')
radio2 = QRadioButton('1643')
radio3 = QRadioButton('1956')
radio4 = QRadioButton('1941')

main_line = QVBoxLayout()

main_line.addWidget(boo)

main_line2 = QHBoxLayout()

main_line3 = QHBoxLayout()

main_line4 = QHBoxLayout()

main_line2.addWidget(radio1)
main_line2.addWidget(radio2)
main_line2.addWidget(radio3)
main_line2.addWidget(radio4)

def radio1_func():
    msg = QMessageBox()
    msg.setText('Ого правильно!)')
    msg.exec()

def radio2_func():
    msg = QMessageBox()
    msg.setText('Не правильно!(')
    msg.exec()

def radio3_func():
    msg = QMessageBox()
    msg.setText('Не правильно!(')
    msg.exec()

def radio4_func():
    msg = QMessageBox()
    msg.setText('Не правильно!(')
    msg.exec()

radio1.clicked.connect(radio1_func)
radio2.clicked.connect(radio2_func)
radio3.clicked.connect(radio3_func)
radio4.clicked.connect(radio4_func)

main_line.addLayout(main_line2)

Ok = QLabel(' У тебе багато домашніх улюбленців?')
ty1 = QRadioButton('Так)')
ty2 = QRadioButton('Ні')

main_line.addWidget(Ok)

main_line3.addWidget(ty1)
main_line3.addWidget(ty2)

def ty1_1():
    msg = QMessageBox()
    msg.setText('То дуже добре')
    msg.exec()

def ty2_2():
    msg = QMessageBox()
    msg.setText('Ясненько')
    msg.exec()

main_line.addLayout(main_line3)

ty1.clicked.connect(ty1_1)
ty2.clicked.connect(ty2_2)

qp = QLabel('Чи часто ти читаєш книги чи якісь історії?')


main_line.addWidget(qp)

main_line4.addWidget(p1)
main_line4.addWidget(p2)
main_line4.addWidget(p3)

def p1_1():
    msg = QMessageBox()
    msg.setText('То дуже добре')
    msg.exec()

def p2_2():
    msg = QMessageBox()
    msg.setText('Ясно')
    msg.exec()

def p3_3():
    msg = QMessageBox()
    msg.setText('О я також)')
    msg.exec()

main_line.addLayout(main_line4)

p1.clicked.connect(p1_1)
p2.clicked.connect(p2_2)
p3.clicked.connect(p3_3)


window.setLayout (main_line)

window.show()
app.exec()