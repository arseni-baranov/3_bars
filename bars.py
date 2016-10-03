import json, math, os

def load_from_json(filepath):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    bars_file = current_dir + '\\' + filepath
    file = open(bars_file, "r", encoding="utf-8")

    return json.loads(file.read())


def get_biggest_bar(bars):
    maxPricedItem = max(bars, key=lambda x: x['Cells']['SeatsCount'])
    return maxPricedItem['Cells']['Name']

def get_smallest_bar(bars):
    minPricedItem = min(bars, key=lambda x: x['Cells']['SeatsCount'])
    return minPricedItem['Cells']['Name']

def get_closest_bar(bars):

    try:
        latitude = float(input('Введите широту:  '))

    except ValueError:
        latitude = None

    if latitude is None:
        print('Извините, данные не верны')

    try:
        longitude = float(input('Введите долготу: '))

    except ValueError:
        latitude = None

    if longitude is None:
        print('Извините, данные не верны')

    bars_geo = {}

    for bar in bars:
        bars_geo.update([(math.sqrt((bar['Cells']['geoData']['coordinates'][0] - longitude) *
                               (bar['Cells']['geoData']['coordinates'][0] - longitude) +
                               (bar['Cells']['geoData']['coordinates'][1] - latitude) *
                               (bar['Cells']['geoData']['coordinates'][1] - latitude)), bar['Cells']['Name'])])

    return(bars_geo.get(min(bars_geo.keys())))


if __name__ == '__main__':

    try:
        bars = load_from_json(input('Введите название json файла с барами: '))
    except FileNotFoundError:
        print('Файла с таким названием не существует в директории с программой')
        exit()

    print('Самый крупный бар: ' + get_biggest_bar(bars))
    print('Самый маленький бар: ' + get_smallest_bar(bars))
    print('=========================================================')
    print('Ближайший бар: ' + get_closest_bar(bars))

