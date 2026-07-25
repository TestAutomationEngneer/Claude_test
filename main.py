import sys

import requests

sys.stdout.reconfigure(encoding="utf-8")

NBP_API_URL = "https://api.nbp.pl/api/exchangerates/rates/a/{code}/?format=json"
CURRENCIES = {
    "USD": "Dolar amerykański",
    "EUR": "Euro",
    "GBP": "Funt brytyjski",
}


def get_rate(code: str) -> float:
    response = requests.get(NBP_API_URL.format(code=code), timeout=10)
    response.raise_for_status()
    data = response.json()
    return data["rates"][0]["mid"]


def main() -> None:
    print("Kursy walut (NBP, tabela A)\n")
    for code, name in CURRENCIES.items():
        rate = get_rate(code)
        print(f"{code} ({name}): {rate:.4f} PLN")


if __name__ == "__main__":
    main()
