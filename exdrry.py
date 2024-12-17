import requests

valcode = str(input('Введіть код валюти'))
ddd = int(input('Введіть рік валюти'))
fff = int(input('Скільки у вас валюти?'))

url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode{valcode}&date=20{ddd}0302&json"
requests = requests.get(url)
if requests.status_code == 200:
    data = requests.json()
    print('курс: ', data[0]['rate'])

    print('Валюта: ', data[0]['txt'])
    print('Кількість: ', fff * data[0]['rate'])


#Дз ^ось це доробити + ще треба отрамти код валюти, дату, кількісь тої валюти що є в тебе
    # , потім вивести це в гривлю