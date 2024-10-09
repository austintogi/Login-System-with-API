from typing import Any
from dataclasses import dataclass
import json

@dataclass
class Geo:
    lat: str
    lng: str

    @staticmethod
    def from_dict(obj: Any) -> 'Geo':
        _lat = str(obj.get("lat"))
        _lng = str(obj.get("lng"))
        return Geo(_lat, _lng)
    
@dataclass
class Address:
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo

    @staticmethod
    def from_dict(obj: Any) -> 'Address':
        _street = str(obj.get("street"))
        _suite = str(obj.get("suite"))
        _city = str(obj.get("city"))
        _zipcode = str(obj.get("zipcode"))
        _geo = Geo.from_dict(obj.get("geo"))
        return Address(_street, _suite, _city, _zipcode, _geo)

@dataclass
class Company:
    name: str
    catchPhrase: str
    bs: str

    @staticmethod
    def from_dict(obj: Any) -> 'Company':
        _name = str(obj.get("name"))
        _catchPhrase = str(obj.get("catchPhrase"))
        _bs = str(obj.get("bs"))
        return Company(_name, _catchPhrase, _bs)

@dataclass
class User:
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        _id = int(obj.get("id"))
        _name = str(obj.get("name"))
        _username = str(obj.get("username"))
        _email = str(obj.get("email"))
        _address = Address.from_dict(obj.get("address"))
        _phone = str(obj.get("phone"))
        _website = str(obj.get("website"))
        _company = Company.from_dict(obj.get("company"))
        return User(_id, _name, _username, _email, _address, _phone, _website, _company)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = User.from_dict(jsonstring)
