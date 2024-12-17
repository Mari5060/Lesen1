from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *

from skin import *


#def showDialog():
   #msgBox = QMessageBox()
   #msgBox.setIcon(QMessageBox.Information)
   #msgBox.setText("Оу! У тебе не вистачає грошей!")
   #msgBox.setWindowTitle("Shooter message")
   #msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

   #returnValue = msgBox.exec()


def shop_window():
    window = QDialog()
    window.setWindowTitle('Shop "Shooter"')
    window.resize(500, 500)
    window.move(500, 100)

    rocket_ldl = QLabel("Ракееета!")
    rocket_px = QPixmap("rooooo.png")
    rocket_px = rocket_px.scaledToWidth(100)
    rocket_ldl.setPixmap(rocket_px)
    rocket_dggd = QPushButton("Купити")
    rockee = QLabel('50 монеток')

    rocket_ldl2 = QLabel("Ракеета!")
    rocket_px2 = QPixmap("roooocket.png")
    rocket_px2 = rocket_px2.scaledToWidth(100)
    rocket_ldl2.setPixmap(rocket_px2)
    rocket_dggd2 = QPushButton("Купити")
    rocke = QLabel('100 монеток')

    def buy_func():
        player_info = read_from_file()
        if player_info["кількість монет"] >= 100:
            player_info["кількість монет"] -= 100
            player_info["скін"] = "roooocket.png"
            write_in_file(player_info)

        #else:
            #showDialog()

    def buy_func2():
        player_info = read_from_file()
        if player_info["кількість монет"] >= 50:
            player_info["кількість монет"] -= 50
            player_info["скін"] = "rooooo.png"
            write_in_file(player_info)


    rocket_dggd.clicked.connect(buy_func)
    rocket_dggd2.clicked.connect(buy_func2)
    main_line2 = QVBoxLayout()
    main_line3 =QVBoxLayout()
    main_line = QHBoxLayout()
    main_line.addWidget(rocket_ldl2)
    main_line2.addWidget(rockee)
    main_line2.addWidget(rocket_dggd2)
    main_line.addWidget(rocket_ldl)
    main_line3.addWidget(rocke)
    main_line3.addWidget(rocket_dggd)
    main_line.addLayout(main_line2)
    main_line.addLayout(main_line3)
    window.setLayout(main_line)
    window.show()
    window.exec()



