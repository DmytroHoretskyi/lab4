from models.enum.cities import Cities
from models.egypt_travel import EgyptTravel
from models.enum.sport import Sport
from models.enum.country import Country
from models.enum.category import Category
from models.sport_travel import SportTravel
from models.enum.sortorder import SortOrder
from operator import attrgetter


class TravelManager:
    def __init__(self, travels=None):
        if travels is None:
            self.travels = []
        else:
            self.travels = travels

    def add_travel(self, travel):
        if travel not in self.travels:
            self.travels.append(travel)

    def sort_by_price(self, sort_order):
        if sort_order == SortOrder.ASC:
            return sorted(self.travels, key=attrgetter('price'))
        if sort_order == SortOrder.DESC:
            return sorted(self.travels, key=attrgetter('price'), reverse=True)


def main():
    manager = TravelManager()
    sport_travel = SportTravel(18, Sport.skiing, Country.Ukraine, "sportko", 1700, Category.sport)
    sport_travel1 = SportTravel(16, Sport.snowboarding, Country.Egypt, "SAnd", 1900, Category.sport)
    egypt_travel = EgyptTravel(True, Cities.Taba, True, False, Country.Egypt, "EgyptTravels", 155.50,
                               Category.family)
    manager.add_travel(sport_travel)
    manager.add_travel(sport_travel1)
    manager.add_travel(egypt_travel)

    manager1 = TravelManager([SportTravel])
    sorted_by_price_asc = manager.sort_by_price(SortOrder.ASC)
    sorted_by_price_desc = manager.sort_by_price(SortOrder.DESC)

    print(sorted_by_price_asc)
    print(sorted_by_price_desc)


if __name__ == '__main__':
    main()
