import json
import math


def load_from_json(bars_file):

    with open(bars_file, "r", encoding="utf-8") as bars_file:
        return json.loads(bars_file.read())


def get_biggest_bar(bars):
    max_priced_item = max(bars, key=lambda x: x['Cells']['SeatsCount'])
    return max_priced_item['Cells']['Name']


def get_smallest_bar(bars):
    min_priced_item = min(bars, key=lambda x: x['Cells']['SeatsCount'])
    return min_priced_item['Cells']['Name']


def validate_input(message):
    try:
        coordinates = float(input(message))

    except ValueError:
        coordinates = None

    if coordinates is None:
        print('Извините, данные не верны')

    return coordinates


def get_closest_bar(bars, latitude, longitude):

    bars_geo = {}

    for bar in bars:
        bars_geo.update([(math.sqrt((bar['Cells']['geoData']['coordinates'][0] - longitude) *
                               (bar['Cells']['geoData']['coordinates'][0] - longitude) +
                               (bar['Cells']['geoData']['coordinates'][1] - latitude) *
                               (bar['Cells']['geoData']['coordinates'][1] - latitude)), bar['Cells']['Name'])])

    return bars_geo.get(min(bars_geo.keys()))


if __name__ == '__main__':

    try:
        bars = load_from_json(input('Укажите путь к json файлу с барами: '))
    except FileNotFoundError:
        print('Файла с таким названием не существует в директории с программой')
        exit()

    print('Самый крупный бар: ' + get_biggest_bar(bars))
    print('Самый маленький бар: ' + get_smallest_bar(bars))
    print('=========================================================')

    latitude = validate_input('Введите широту: ')
    longitude = validate_input('Введите долготу: ')

    print('Ближайший бар: ' + get_closest_bar(bars, latitude, longitude))
