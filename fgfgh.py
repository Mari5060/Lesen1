import requests


url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcodeUSA&date=20120302&json"
requests = requests.get(url)
if requests.status_code == 200:
    data = requests.json()
    print(data[0])




