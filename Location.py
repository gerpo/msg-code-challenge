class Location:
    location_number: int
    name: str
    street: str
    house_number: str
    postal_code: str
    city: str
    latitude: float
    longitude: float

    def __init__(self, location_number: int, name: str, street: str, house_number: str, postal_code: str, city: str,
                 latitude: float, longitude: float):
        self.location_number = location_number
        self.name = name
        self.street = street
        self.house_number = house_number
        self.postal_code = postal_code
        self.city = city
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self) -> str:
        return f'Location {self.name}(num: {self.location_number}) is located on {self.street} {self.house_number} in {self.postal_code} {self.city} (lat: {self.latitude}, lon: {self.longitude}).'

    def __repr__(self) -> str:
        return f'Location {self.name}'
