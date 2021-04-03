from models.family_travel import FamilyTravel
from models.enum.cities import Cities


class EgyptTravel(FamilyTravel):
    def __init__(self, visa: bool, visiting_cities: Cities, with_kids, kids_zone, country, producer, price, category):
        self.visa = visa
        self.visiting_cities = visiting_cities
        FamilyTravel.__init__(self,with_kids, kids_zone, country, producer, price, category)

    def __repr__(self):
        return f'Category : {self.category}, price: {self.price}, producer: {self.producer}, country: {self.country},' \
               f'kids zone: {self.with_kids}, visiting cities: {self.visiting_cities}, category: {self.category}, ' \
               f'with kids: {self.with_kids}\n'
