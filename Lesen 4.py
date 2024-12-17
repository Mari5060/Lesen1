from PyQt6.QtWidgets import*
from PyQt6.QtCore import  Qt

app = QApplication([])

window = QWidget()

window.setWindowTitle('Memory Card')

window_width, window_height = 600,500

window.resize(window_width, window_height)

window.move(0,0)

main_line = QVBoxLayout()
main_line0 = QHBoxLayout()
main_line2 = QHBoxLayout()

kj = QPushButton('Меню')
gh = QPushButton('Відпочити')
hg = QSpinBox()
hg.setValue(30)
df = QPushButton('Відповісти')
rh = QLabel('Скільки буде 27+3+40?')
rt = QLabel('хвилин')

main_line0.addWidget(rh,alignment =(Qt.AlignHCenter | Qt.AlignVCenter))

main_line0.addWidget(kj)
main_line0.addStretch(1)
main_line0.addWidget(gh)
main_line0.addWidget(hg)

main_line.addLayout(main_line0)

RadioGroupBox = QGroupBox('Варіанти відповідей')
RadioGroup = QButtonGroup()

main_line.addWidget(rh)

p1 = QRadioButton('22')
p2 = QRadioButton('70')
p3 = QRadioButton('79')

main_line2.addWidget(p1)
main_line2.addWidget(p2)
main_line2.addWidget(p3)

def p1_1():
    msg = QMessageBox()
    msg.setText('Неправильно!')
    msg.exec()

def p2_2():
    msg = QMessageBox()
    msg.setText('Правильно')
    msg.exec()

def p3_3():
    msg = QMessageBox()
    msg.setText('Неправильно')
    msg.exec()

p1.clicked.connect(p1_1)
p2.clicked.connect(p2_2)
p3.clicked.connect(p3_3)




















main_line.addLayout(main_line2)

window.setLayout (main_line)

window.show()
app.exec()