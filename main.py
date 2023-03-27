"""
Zoptymalizuj kod z poprzedniego zadania z pogodą.

Utwórz klasę WeatherForecast, która będzie służyła do odczytywania i zapisywania pliku,
 a także odpytywania API.

Obiekt klasy WeatherForecast dodatkowo musi poprawnie implementować cztery metody:

 __setitem__
 __getitem__
 __iter__
 items

Wykorzystaj w kodzie poniższe zapytania:

weather_forecast[date] da odpowiedź na temat pogody dla podanej daty
weather_forecast.items() zwróci generator tupli w formacie (data, pogoda) dla już
zapisanych rezultatów przy wywołaniu
weather_forecast to iterator zwracający wszystkie daty, dla których znana jest pogoda
"""
import requests
import pprint

MIESIACE = {
    "01": [31],
    "02": [28],
    "03": [31],
    "04": [30],
    "05": [31],
    "06": [30],
    "07": [31],
    "08": [31],
    "09": [30],
    "10": [31],
    "11": [30],
    "12": [31],

}
def sprawdz_date(dstr: str) -> bool:
    dstr = dstr.strip()
    parts = dstr.split('-')
    if len(parts) != 3:
        return False
    year, month, day = parts
    year = [e for e in year if e.isdigit()]
    month = [e for e in month if e.isdigit()]
    day = [e for e in day if e.isdigit()]
    if len(year) != 4:
        return False
    if len(month) != 2:
        return False
    if len(day) != 2:
        return False
    if not (2000 <= int("".join(year)) <= 2023):
        return False
    month = "".join(month)
    if month not in MIESIACE:
        return False
    day = "".join(day)
    dni_miesiaca = MIESIACE[month][0]
    mozliwe_dni = [str(d) if d > 9 else f"0{str(d)}" for d in range(1,dni_miesiaca)]
    if day not in mozliwe_dni:
        return False
    return True
def data_istnieje_w_pliku():
    data_jest_juz_w_wpliku = False
    with open("output.txt", "r") as file:
         for line in file.readlines():
             if searched_date:
                data_jest_juz_w_wpliku = True
                return data_jest_juz_w_wpliku



latitude = '52.237049'
longitude = '21.017532'
searched_date = input("Podaj Date: ")

if not data_istnieje_w_pliku():

    URL = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}' \
          f'&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2F' \
          f'London&start_date={searched_date}' \
          f'&end_date={searched_date}'
    zapytanie = requests.get(URL)
    dane = zapytanie.json()

else:
    URL = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}' \
          f'&longitude={longitude}' \
          f'&hourly=rain&daily=rain_sum&timezone=Europe%2F' \
          f'London&start_date={searched_date}' \
          f'&end_date={searched_date}'
    zapytanie = requests.get(URL)
    dane = zapytanie.json()

pprint.pprint(dane)




if not zapytanie.ok:
    print(f"Blad API {zapytanie.status_code}")
    quit()
pogoda = []
time = []
for p in zapytanie.json()['daily']['rain_sum']:
    pogoda.append(float(p))
    print(pogoda)
    if p == 0.0:
        print(f"Nie Padalo w Tym Dniu ")
    if p > 0.0:
        print(f"Padalo w Tym Dniu")
    if p < 0.0:
        print('Blad')
    with open('output.txt','a') as plik:
        if True:
            plik.write(f"Opady deszczu {p} ml,W {searched_date}\n")
class WeatherForecast:
    def __init__(self, pogoda, searched_date):
        self.pogoda = pogoda
        self.searched_date = searched_date
    def __setitem__(self, item, value):
        self.pogoda[item] = value

    def __float__(self):
        return f'<opad deszczu: {self.pogoda}, w dniu: {self.searched_date}>'
    def __getitem__(self, item):
        return self.pogoda[item]
    def __iter__(self):
        with open('output.txt','r'):
            if True:
                for s in self.searched_date:
                    yield s


for s in searched_date:
    print(s)
