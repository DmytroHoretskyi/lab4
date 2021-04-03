from manager.TravelManager import TravelManager
from models.enum.cities import Cities
from models.egypt_travel import EgyptTravel
from models.enum.sport import Sport
from models.enum.country import Country
from models.enum.category import Category
from models.sport_travel import SportTravel
from models.enum.sortorder import SortOrder


class Test:
    def main(self):
        manager = TravelManager()
        sport_travel = SportTravel(18, Sport.skiing.name, Country.Ukraine.name, "sportko", 1700, Category.sport.name)
        sport_travel1 = SportTravel(16, Sport.snowboarding.name, Country.Egypt.name, "SAnd", 1900, Category.sport.name)
        egypt_travel = EgyptTravel(True, Cities.Taba.name, True, False, Country.Egypt.name, "EgyptTravels", 155.50,
                                   Category.family.name)
        manager.add_travel(sport_travel)
        manager.add_travel(sport_travel1)
        manager.add_travel(egypt_travel)

        manager1 = TravelManager([SportTravel])
        sorted_by_price_asc = manager.sort_by_price(SortOrder.ASC)
        sorted_by_price_desc = manager.sort_by_price(SortOrder.DESC)

        print(sorted_by_price_asc)
        print(sorted_by_price_desc)
    