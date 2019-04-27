import json
import argparse
import os


def load_data(filepath):
    with open(filepath) as file:
        try:
            return json.loads(file.read())['features']
        except json.JSONDecodeError:
            return None


def get_biggest_bar(bars):
    return max(bars,  key=lambda item: item['properties']['Attributes']['SeatsCount'])

def get_smallest_bar(bars):
    return min(bars, key=lambda item: item['properties']['Attributes']['SeatsCount'])


def get_closest_bar(bars, longitude, latitude):
    return min(bars,
               key=lambda item: (item['geometry']['coordinates'][0] - longitude) ** 2 +
                                (item['geometry']['coordinates'][1] - latitude) ** 2
               )

def get_name_adress_bar(data_bar):
    bar_attributes = data_bar['properties']['Attributes']
    return bar_attributes['Name'], bar_attributes['Address']

def get_consol_params():
    parser = argparse.ArgumentParser()
    parser.add_argument('pathfile', help='File with data about bars in json format')
    parser.add_argument('longitude', type=float, help='Longitude of current user gps coordinates')
    parser.add_argument('latitude', type=float, help='Latitude of current user gps coordinates')
    return parser.parse_args()

def main():

    params = get_consol_params()

    filepath = params.pathfile
    longitude = params.longitude
    latitude = params.latitude

    if not os.path.isfile(filepath):
        exit('File not found')


    bars = load_data(filepath)

    if not bars:
        exit('File data is not in json format.')

    biggest_bar = get_biggest_bar(bars)
    smallest_bar = get_smallest_bar(bars)
    closest_bar = get_closest_bar(bars, longitude, latitude)

    print('Biggest bar:  {} по адресу {}'.format(*get_name_adress_bar(biggest_bar)))
    print('Smallest bar: {} по адресу {}'.format(*get_name_adress_bar(smallest_bar)))
    print('Closest bar:  {} по адресу {}'.format(*get_name_adress_bar(closest_bar)))


if __name__ == '__main__':
    main()
