from request_processing import get_service
from typing import Tuple, Optional, Union
from dash_app.placesdata import Place


class Geolocation(object):

    def __init__(self, find_me: bool = True):
        self.gmap = get_service()
        self.me = self.get_my_location() if find_me else None

    def get_my_location(
            self,
            specific_address: Optional[str] = None
    ) -> Tuple[float, float]:

        if specific_address is None:
            result = self.gmap.geolocate()['location']
            coords = (result['lat'], result['lng'])
        else:
            coords = self.get_place(specific_address)

        return coords

    def get_place(self, place: Union[Place, str]) -> Tuple[float, float]:

        if isinstance(place, Place):
            address = ', '.join([place.street, place.city, place.zipcode])
        else:
            address = place
        result = self.gmap.geocode(address)[0]['geometry']['location']

        return result['lat'], result['lng']

    def get_distance(self, destination: Tuple[float, float]) -> float:
        
        if self.me is None:
            self.me = self.get_my_location()
        
        result = self.gmap.distance_matrix(
                self.me,
                destination,
                mode='walking'
            )["rows"][0]["elements"][0]["distance"]["value"]

        return result


if __name__ == '__main__':
    import os
    os.chdir('..')
    gl = Geolocation(find_me=True)
    coordinates = gl.get_place(Place('', '', 'NTK', '', 'Prague'))
    dist = gl.get_distance(coordinates)
