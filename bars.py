import json, math, os

def load_from_json(filepath):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    bars_file = current_dir + '\\' + filepath
    with open(bars_file, "r", encoding="utf-8") as bars_file:
        return json.loads(bars_file.read())


def get_biggest_bar(bars):
    max_priced_item = max(bars, key=lambda x: x['Cells']['SeatsCount'])
    return max_priced_item['Cells']['Name']

def get_smallest_bar(bars):
    min_priced_item = min(bars, key=lambda x: x['Cells']['SeatsCount'])
    return min_priced_item['Cells']['Name']

def get_input(message):
    try:
        coordinates = float(input(message))

    except ValueError:
        coordinates = None

    if coordinates is None:
        print('Извините, данные не верны')

    return coordinates


def get_closest_bar(bars):

    latitude = get_input('Введите широту: ')
    longitude = get_input('Введите долготу: ')

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

