import json
import argparse
import os


def load_data(filepath):
    with open(filepath) as f:
        try:
            return json.loads(f.read())['features']
        except json.JSONDecodeError:
            return None


def get_biggest_bar(list_data_bars):
    return max(list_data_bars,
               key=lambda item: item['properties']['Attributes']['SeatsCount']
               )

def get_smallest_bar(list_data_bars):
    return min(list_data_bars,
               key=lambda item: item['properties']['Attributes']['SeatsCount']
               )


def get_closest_bar(list_data_bars, longitude, latitude):
    return min(list_data_bars,
               key=lambda item: (item['geometry']['coordinates'][0] - longitude) ** 2 +
               (item['geometry']['coordinates'][1] - latitude) ** 2
               )

def get_name_adress_bar(data_bar):
    bar_attributes = data_bar['properties']['Attributes']
    return bar_attributes['Name'], bar_attributes['Address']

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('pathfile', help='File with data about bars in json format')
    parser.add_argument('longitude', type=float, help='Longitude of current user gps coordinates')
    parser.add_argument('latitude', type=float, help='Latitude of current user gps coordinates')

    params = parser.parse_args()

    filepath = params.pathfile
    longitude = params.longitude
    latitude = params.latitude

    if not os.path.isfile(filepath):
        exit('File not found')


    list_data_bars = load_data(filepath)

    if not list_data_bars:
        exit('File data is not in json format.')

    biggest_bar = get_biggest_bar(list_data_bars)
    smallest_bar = get_smallest_bar(list_data_bars)
    closest_bar = get_closest_bar(list_data_bars, longitude, latitude)

    print('Biggest bar:  {} по адресу {}'.format(*get_name_adress_bar(biggest_bar)))
    print('Smallest bar: {} по адресу {}'.format(*get_name_adress_bar(smallest_bar)))
    print('Closest bar:  {} по адресу {}'.format(*get_name_adress_bar(closest_bar)))


if __name__ == '__main__':
    main()
