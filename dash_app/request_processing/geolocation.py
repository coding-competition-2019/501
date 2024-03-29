from request_processing import get_service
from typing import Tuple, Optional, Union
from placesdata import Place
from haversine import haversine, Unit


class Geolocation(object):

    _travel_modes = {"walking", "bicycling", "driving", "transit"}
    _dist_modes = {'google', 'haversine'}

    def __init__(self, find_me: bool = True):
        self.gmap = get_service()
        self._me = self.get_my_location() if find_me else None

    @property
    def me(self):
        if self._me is None:
            self._me = self.get_my_location()
        return self._me

    def get_my_location(
        self, specific_address: Optional[str] = None
    ) -> Tuple[float, float]:

        if specific_address is None:
            result = self.gmap.geolocate()["location"]
            coords = (result["lat"], result["lng"])
        else:
            coords = self.get_place(specific_address)

        return coords

    def get_place(self, place: Union[Place, str]) -> Tuple[float, float]:

        if isinstance(place, str):
            address = place
        else:
            address = ", ".join([place.street, place.city, place.zipcode])
        result = self.gmap.geocode(address)[0]["geometry"]["location"]

        return result["lat"], result["lng"]

    def get_distance(self, destination: Tuple[float, float],
                     method: str = 'haversine') -> float:

        assert method in self._dist_modes

        if method == 'google':
            result = self.gmap.distance_matrix(
                self.me,
                destination,
                mode="walking"
            )[
                "rows"
            ][0]["elements"][0]["distance"]["value"]

        else:
            result = haversine(self.me, destination, unit=Unit.METERS)

        return result

    def get_navigations(
        self, destination: Tuple[float, float], travel_mode: str = "driving"
    ):

        assert travel_mode in self._travel_modes

        link = (
            f"https://www.google.com/maps/dir/?api=1&"
            f'origin={",".join([str(item) for item in self.me])}&'
            f'destination={",".join([str(item) for item in destination])}&'
            f"travelmode={travel_mode}"
        )

        return link


if __name__ == "__main__":
    import os
    print(os.getcwd())
    gl = Geolocation(find_me=True)
    coordinates = gl.get_place(Place("", "", "NTK", "", "Prague", ''))
    print(f"My coordinates: {gl.me}")
    print(f"NTK coordinates: {coordinates}")
    print(f"Distance to NTK: {gl.get_distance(coordinates)}")
    print(f"Directions to NTK: {gl.get_navigations(destination=coordinates)}")
