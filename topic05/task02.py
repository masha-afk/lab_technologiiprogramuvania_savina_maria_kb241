import requests

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

def get_data():
    return requests.get(URL).json()

def exchange(data, currency):
    for elem in data:
        if elem["cc"] == currency:
            amount = float(input(f"Введіть суму в {currency}: "))
            print(f"{amount} {currency} = {round(amount * elem['rate'], 2)} UAH")
            return

while True:
    choice = input("\nВведіть валюту (EUR/USD/PLN) або 'exit' для виходу: ").lower()
    data = get_data()

    match choice:
        case "eur" | "usd" | "pln":
            exchange(data, choice.upper())
        case "exit":
            print("Вихід...")
            break
