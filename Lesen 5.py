
import database
from PyQt6.QtWidgets import *
from PyQt6.QtCore import*
import random
import time

from menu import menu_window

app = QApplication([])

window = QWidget()
window_width, window_height = 600, 500
window.resize(window_width, window_height)
window.move(500, 500)


window.setWindowTitle("Memory Card")

window.move(0,0)

btn_Menu = QPushButton('Меню')
btn_Sleep = QPushButton('Відпочити')
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
btn_OK = QPushButton('Відповісти')
hfhf = QPushButton('Наступне питання')
lb_Question = QLabel('2+2?')

RadioGroupBox = QGroupBox("Варіанти відповіді")
RadioGroup = QButtonGroup()

rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('Правильно')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignmentFlag.AlignLeft))
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()
layout_line5 = QHBoxLayout()
layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('хвилин'))

layout_line2.addWidget(lb_Question)
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2)
layout_line5.addWidget(hfhf)
layout_line4.addStretch(1)

def set_quest():
    random.shuffle(answers)
    cur_quest = database.questions[database.now_quest]
    lb_Question.setText(cur_quest["Запитання"])
    answers[0].setText(cur_quest["Правильна відповідь"])
    answers[1].setText(cur_quest["Неправильна відповідь1"])
    answers[2].setText(cur_quest["Неправильна відповідь2"])
    answers[3].setText(cur_quest["Неправильна відповідь3"])

def answer_func():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    if answers[0].isChecked():
        lb_Result.setText("Правильно")
    else:
        lb_Result.setText("Не правильно")

set_quest()

def next_quest():
    database.now_quest += 1
    RadioGroupBox.show()
    AnsGroupBox.hide()
    set_quest()

hfhf.clicked.connect(next_quest)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addLayout(layout_line5, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)



def show_menu():
    menu_window()


def hide_1():
    window.hide()
    time.sleep(box_Minutes)
    window.show()


btn_Sleep.clicked.connect(hide_1)
btn_Menu.clicked.connect(show_menu)
btn_OK.clicked.connect(answer_func)
window.setLayout(layout_card)

window.show()
app.exec()
