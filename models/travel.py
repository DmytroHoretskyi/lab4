from models.enum.country import Country
from models.enum.category import Category


class Travel:
    def __init__(self, country: Country, producer: str, price: float, category: Category):
        self.country = country
        self.producer = producer
        self.price = price
        self.category = category
