import utils


class PlacesData:
    def __init__(self):
        self.transformed_data = utils.read_json('data/places_transformed.json')
        self.data = utils.read_json('data/places.json')

    def get_activity_list(self):
        return self.transformed_data['activity_list']

    def get_places_by_activity(self, activity):
        places = list()
        for id in self.transformed_data['places'][activity]:
            p = self.data['places'][id]
            places.append(Place(p['name'], p['url'], p['address']['street'],
                                p['address']['zipCode'],
                                p['address']['city']))
        return places


class Place:
    def __init__(self, name, url, street, zipcode, city):
        self.name = name
        self.url = url
        self.street = street
        self.zipcode = zipcode
        self.city = city


if __name__ == '__main__':
    # kinda unit test
    data = PlacesData()
    print(data.get_activity_list())
    for pl in data.get_places_by_activity('kick box'):
        print(pl.name)
        print(pl.url)
        print(pl.street)
        print(pl.zipcode)
        print(pl.city)
