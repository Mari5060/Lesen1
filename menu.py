from PyQt6.QtWidgets import *

import database

def menu_window():
    window = QDialog()
    quest_list = QListWidget()
    quest_lbl = QLabel("Питання")
    quest_input = QLineEdit()
    true_ans_lbl = QLabel("Правильна відповідь")
    true_ans_input = QLineEdit()
    false_ans_lbl1 = QLabel("Не правильна відповідь")
    false_ans_input1 = QLineEdit()
    false_ans_lbl2 = QLabel("Не правильна відповідь")
    false_ans_input2 = QLineEdit()
    false_ans_lbl3 = QLabel("Не правильна відповідь")
    false_ans_input3 = QLineEdit()
    add_quest_btn = QPushButton("Додати запитання")
    update_quest_lbl = QPushButton("Оновити запитання")

    layout_res = QVBoxLayout()
    h8 = QHBoxLayout()
    gt = QVBoxLayout()

    layout_res.addLayout(h8)
    h8.addWidget(quest_list)
    h8.addLayout(gt)
    gt.addWidget(quest_lbl)
    gt.addWidget(quest_input)
    gt.addWidget(true_ans_lbl)
    gt.addWidget(true_ans_input)
    gt.addWidget(false_ans_lbl1)
    gt.addWidget(false_ans_input1)
    gt.addWidget(false_ans_lbl2)
    gt.addWidget(false_ans_input2)
    gt.addWidget(false_ans_lbl3)
    gt.addWidget(false_ans_input3)

    layout_res.addWidget(add_quest_btn)
    layout_res.addWidget(update_quest_lbl)

    for element in database.questions:
        quest_list.addItem(element["Запитання"])
    selected_quest = 0
    def on_item_clicked(item):
        global selected_quest
        index = quest_list.row(item)
        selected_quest = index
        question = database.questions[index]
        quest_input.setText(question["Запитання"])
        true_ans_input.setText(question["Правильна відповідь"])
        false_ans_input1.setText(question["Неправильна відповідь1"])
        false_ans_input2.setText(question["Неправильна відповідь2"])
        false_ans_input3.setText(question["Неправильна відповідь3"])

    def add_quest_funs():
        database.questions.append(
            {
                "Запитання": quest_input.text(),
                "Правильна відповідь": true_ans_input.text(),
                "Неправильна відповідь1": false_ans_input1.text(),
                "Неправильна відповідь2": false_ans_input2.text(),
                "Неправильна відповідь3": false_ans_input3.text(),
            }
        )
        quest_list.addItem(quest_input.text())


    def update_quest():
        global selected_quest
        database.questions[selected_quest] = {
                "Запитання": quest_input.text(),
                "Правильна відповідь": true_ans_input.text(),
                "Неправильна відповідь1": false_ans_input1.text(),
                "Неправильна відповідь2": false_ans_input2.text(),
                "Неправильна відповідь3": false_ans_input3.text(),
        }

    update_quest_lbl.clicked.connect(update_quest)
    add_quest_btn.clicked.connect(add_quest_funs)
    quest_list.itemClicked.connect(on_item_clicked)
    window.setLayout(layout_res)
    window.show()
    window.exec()

