from PyQt6.QtWidgets import *
from gpohi import *
from grohickikubtebe import *

import requests

def gpohi_tyt():
    player_inf = read_from_file()


    window = QDialog()
    window.setWindowTitle('Money transfer:')
    window.resize(500, 500)
    window.move(500, 100)

    kob_text = QLabel("Назва валюти:")
    kod = QLineEdit("CNY")
    data_text = QLabel("Рік валюти:")
    data = QLineEdit('24')
    ckilku_text = QLabel("Всього кількість монеток:")
    ckilku = QLineEdit(str(player_inf['зароблено монеток']))
    resylt_text = QLabel("Ваш результата в гривнях:")
    resylt = QLineEdit('')
    otpumatu = QPushButton('Перевести в гривні')

    def fsff():
        valcode = kod.text()
        ddd = data.text()
        url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode{valcode}&date=20{ddd}0302&json"
        respons = requests.get(url)
        dataa = respons.json()
        kilkict = player_inf['зароблено монеток']
        #resylt.setText(str(dataa[0]['rate'] * kilkict))
        ckicugrohi(ckilku.text(), str(dataa[0]['rate'] * kilkict))

    window.setStyleSheet("""
    QDialog { 
        background-color : #FFDAB9;
        color: 	#CD3333;

    }
    
    QLineEdit { 
        background-color : #FFF5EE;
        color: 	#CD3333;

    }
        
    QLebel { 
        background-color : #8B1A1A;

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

     #ДЗ : Доробити це + зайти на 30 минут до уроку, намалювати приведів і меч щоб не різати жаб, головне не забути!
    line = QVBoxLayout()
    otpumatu.clicked.connect(fsff)
    line.addWidget(kob_text)
    line.addWidget(kod)
    line.addWidget(data_text)
    line.addWidget(data)
    line.addWidget(resylt_text)
    line.addWidget(resylt)
    line.addWidget(ckilku_text)
    line.addWidget(ckilku)
    line.addWidget(otpumatu)

    window.setLayout(line)

    window.show()
    window.exec()