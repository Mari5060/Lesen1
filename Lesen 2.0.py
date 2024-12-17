import json
from PyQt6.QtWidgets import*
notes = {}

def read_data():
    global notes
    with open('notes.json','r', encoding = 'utf-8') as f:
        notes = json.load(f)

read_data()
app = QApplication([])
window = QWidget()
main_line = QHBoxLayout()
window_width, window_height = 800, 500
window.resize(window_width, window_height)
window.move(0,0)

v1 = QVBoxLayout()
v2 = QVBoxLayout()
v3 = QHBoxLayout()
v4 = QHBoxLayout()



#Створення віджитів
window.setWindowTitle("Розумні замітки")
qqq = QTextEdit()
www = QLineEdit()
label_w = QLabel('Список заміток')
label_e = QLabel('Список тегів')
www.setPlaceholderText("Підказка")
btn_1 = QPushButton("Створити замітку")
btn_2 = QPushButton("Видалити замітку")
btn_3 = QPushButton("Зберегти замітку")
btn_4 = QPushButton("Додати до тегу")
btn_5 = QPushButton("Відкріпити від тегу")
btn_6 = QPushButton("Шукати замітки по тегу")
list_1 = QListWidget()
list_2 = QListWidget()
list_1.addItems(notes)



#Показ  віджетів на екрані
v2.addWidget(qqq)
v1.addWidget(label_w)
v1.addWidget(list_1)
v1.addLayout(v3)
v3.addWidget(btn_1)
v3.addWidget(btn_2)
v1.addWidget(btn_3)
v1.addWidget(label_e)
v1.addWidget(list_2)
v1.addWidget(www)
v1.addLayout(v4)
v4.addWidget(btn_4)
v4.addWidget(btn_5)
v1.addWidget(btn_6)
v1.addWidget(label_w)

def create_note_funs():
    note_name, ok = QInputDialog.getText(window, "Створення", "Введіть назву")
    if ok == True:
        notes[note_name] = {
            "text": "",
            "tags": []
        }
        list_1.clear()
        list_1.addItems(notes)
        with open("notes.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)

def change_note_func():
    key = list_1.selectedItems()[0].text()
    notes[key]["text"] = qqq.toPlainText()
    with open("notes.json", "w", encoding = "utf-8") as file:
        json.dump(notes,file, ensure_ascii=False, indent=4)

def change_note_func_2():
    key = list_1.selectedItems()[0].text()
    notes[key]["tags"].append(www.text())
    list_2.addItem(www.text())
    with open("notes.json", "w", encoding = "utf-8") as file:
        json.dump(notes,file, ensure_ascii=False, indent=4)


def note_show():
    key = list_1.selectedItems()[0].text()
    qqq.setText(notes[key]["text"])
    list_2.clear()
    list_2.addItems(notes[key]["tags"])

def delete_note():
    kkk = list_1.selectedItems()
    if kkk:
        key = kkk[0].text()
        del notes[key]
        list_1.addItems(notes)
        list_1.clear()
        list_1.addItems(notes)
        with open("notes.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)

def delete_tags():
    rrr = list_1.selectedItems()
    if rrr:
        key = rrr[0].text()
        stag = list_2.selectedItems()[0].text()
        notes[key]['tags'].remove(stag)

        list_2.clear()
        list_2.addItems(notes[key]['tags'])
        with open("notes.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)


app.setStyleSheet("""
QPushButton { 
    background-color : #7B68EE;
    
}
QLabel {
    background-color : #6495ED;
}
QListWidget{
    background-color : #4682B4;
}
QLineEdit{
    background-color : #CCCCFF;
}
QWidget{
    background-color : #87CEEB;
    """)

def eine():
    search_element = www.text()
    print(search_element)
    if search_element == '':
        list_1.clear()
        list_1.addItems(notes)
        return
    korzunka = {}
    for kruvetka in notes:
        if search_element in notes[kruvetka]['tags']:
            korzunka[kruvetka] = notes[kruvetka]
        list_1.clear()
        list_1.addItems(korzunka)

btn_6.clicked.connect(eine)
btn_5.clicked.connect(delete_tags)
btn_2.clicked.connect(delete_note)
list_1.itemClicked.connect(note_show)
btn_1.clicked.connect(create_note_funs)
btn_3.clicked.connect(change_note_func)
btn_4.clicked.connect(change_note_func_2)
main_line.addLayout(v2)
main_line.addLayout(v1)
window.setLayout(main_line)
window.show()
app.exec()











