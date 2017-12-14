import json


def load_data(filepath):
    with open(filepath) as f:
        return json.loads(f.read())


def get_biggest_bar(json_data):
    return max(json_data['features'],
               key=lambda item: item['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(json_data):
    return min(json_data['features'],
               key=lambda item: item['properties']['Attributes']['SeatsCount'])


def get_closest_bar(json_data, longitude, latitude):
    return min(json_data['features'],
               key=lambda item: (
               item['geometry']['coordinates'][0] - longitude) ** 2 +
               (item['geometry']['coordinates'][1] - latitude) ** 2)


if __name__ == '__main__':

    filepath = input('Path to file: ')
    longitude = float(input('Longitude: '))
    latitude = float(input('Latitude: '))

    json_data = load_data(filepath)

    biggest_bar = get_biggest_bar(json_data)
    smallest_bar = get_smallest_bar(json_data)
    closest_bar = get_closest_bar(json_data, longitude, latitude)

    print('Biggest bar:  ', biggest_bar)
    print('Smallest bar: ', smallest_bar)
    print('Closest bar:  ', closest_bar)
