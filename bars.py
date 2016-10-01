import json, math, os

def load_from_json(filepath):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    bars_file = current_dir + '\\' + filepath
    file = open(bars_file, "r", encoding="utf-8")

    return json.loads(file.read())


def get_biggest_bar(bars):
    maxPricedItem = max(bars, key=lambda x: x['Cells']['SeatsCount'])
    print('Самый крупный бар: ' + maxPricedItem['Cells']['Name'])

def get_smallest_bar(bars):
    minPricedItem = min(bars, key=lambda x: x['Cells']['SeatsCount'])
    print('Самый маленький бар: ' + minPricedItem['Cells']['Name'])

def get_closest_bar(bars):
    print('=========================================================')

    try:
        latitude = float(input('Введите ширину:  '))

    except ValueError:
        latitude = None

    if latitude is None:
        print('Извините, данные не верны')
        exit()

    try:
        longitude = float(input('Введите долготу: '))
    except ValueError:
        latitude = None

    if longitude is None:
        print('Извините, данные не верны')
        exit()

    tmp = {}

    for bar in bars:
        tmp.update([(math.sqrt((bar['Cells']['geoData']['coordinates'][0] - longitude) *
                               (bar['Cells']['geoData']['coordinates'][0] - longitude) +
                               (bar['Cells']['geoData']['coordinates'][1] - latitude) *
                               (bar['Cells']['geoData']['coordinates'][1] - latitude)), bar['Cells']['Name'])])


    print(min(tmp.keys()))
    print(tmp.get(min(tmp.keys())))


if __name__ == '__main__':
    bars = load_from_json('bars.json')
    get_biggest_bar(bars)
    get_smallest_bar(bars)
    get_closest_bar(bars)
