from models.travel import Travel
from models.enum.sport import Sport


class SportTravel(Travel):
    def __init__(self, age_limit: int, kind_of_sport: Sport, country, producer, price, category):
        self.age_limit = age_limit
        self.kind_of_sport = kind_of_sport
        Travel.__init__(self, country, producer, price, category)

    def __repr__(self):
        return f'Category : {self.category}, price: {self.price}, producer: {self.producer}, country: {self.country},' \
               f'Kind of sport: {self.kind_of_sport}, age limit: {self.age_limit}\n'
