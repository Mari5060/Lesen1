from Gamebb import start_game
from gameshooop import shop_window
from PyQt6.QtWidgets import *

app = QApplication([])

window = QWidget()
window.setWindowTitle('Shooter')
window.resize(500,500)
window.move(500,100)

main_line = QHBoxLayout()
start_ = QPushButton("Відкрити гру")
shop_ = QPushButton("Магазин")

main_line.addWidget(start_)
main_line.addWidget(shop_)




window.setLayout (main_line)

start_.clicked.connect(start_game)
shop_.clicked.connect(shop_window)

window.show()
app.exec()