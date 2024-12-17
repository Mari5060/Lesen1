from My1game import start_gameee
from moneytytyty import gpohi_tyt
from PyQt6.QtWidgets import *

app = QApplication([])

window = QWidget()
window.setWindowTitle('Killing_spirits!')
window.resize(500,500)
window.move(500,100)

main_line = QHBoxLayout()
start_ = QPushButton("Відкрити гру")
gpoh_ = QPushButton("Перевести гроші")

main_line.addWidget(start_)
main_line.addWidget(gpoh_)

app.setStyleSheet("""
QWidget { 
    background-color : #FFDAB9;

}
QPushButton:hover { 
    background-color : #EE8262;
    color: 	#CD3333;

}

QPushButton { 
    background-color : #AF4035;
    color: 	#490206;

}

    """)

window.setLayout (main_line)

start_.clicked.connect(start_gameee)
gpoh_.clicked.connect(gpohi_tyt)

window.show()
app.exec()
