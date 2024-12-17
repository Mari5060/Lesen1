from PyQt6.QtWidgets import *
import requests

app = QApplication([])

window = QWidget()
window.resize(500, 500)
window.move(500, 100)

kod = QLineEdit('Видіть код:')
data = QLineEdit('Видіть дату:')
ckilku = QLineEdit('Видіть кількість вашої валюти:')
resylt = QLineEdit('')
otpumatu = QPushButton('Отримати дані')

def fsff():
    valcode = kod.text()
    ddd = data.text()
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode{valcode}&date=20{ddd}0302&json"
    respons = requests.get(url)
    dataa = respons.json()
    resylt.setText(str(dataa[0]['rate']))

line = QVBoxLayout()
otpumatu.clicked.connect(fsff)
line.addWidget(kod)
line.addWidget(data)
line.addWidget(resylt)
line.addWidget(ckilku)
line.addWidget(otpumatu)




window.setLayout(line)

window.show()
app.exec()