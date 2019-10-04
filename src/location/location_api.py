from geopy.geocoders import Nominatim


class countyConverter:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="I_dont_know_what_this_is_supposed_to_be")

    def get_ll(self, county, state):
        _location = self.geolocator.geocode(self._format(county, state))
        return (_location.latitude, _location.longitude)

    def _format(self, county, state):
        return county + ", " + state + " US"
