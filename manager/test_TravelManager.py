import unittest
from manager import TravelManager
from models.enum.category import Category
from models.enum.cities import Cities
from models.enum.country import Country
from models.enum.sport import Sport


class TestTravelManager(unittest.TestCase):
    def setUp(self):
        self.manager = TravelManager.TravelManager()
        self.manager.travel1 = TravelManager.SportTravel(18, Sport.skiing, Country.Ukraine, "sportko", 1700,
                                                         Category.sport)
        self.manager.travel2 = TravelManager.EgyptTravel(True, Cities.Taba, True, False, Country.Egypt, "EgyptTravels",
                                                         155.50, Category.family)
        self.manager.travel3 = TravelManager.EgyptTravel(True, Cities.Taba, True, False, Country.Egypt, "EgyptTravels",
                                                         2, Category.family)

    def test_add_travel(self):
        self.manager.add_travel(self.manager.travel1)
        print(self.manager.travels)
        self.assertEqual(self.manager.travels, [self.manager.travel1])
        self.manager.add_travel(self.manager.travel2)
        print(self.manager.travels)
        self.assertEqual(self.manager.travels, [self.manager.travel1, self.manager.travel2])
        self.manager.add_travel(self.manager.travel3)
        print(self.manager.travels)
        self.assertEqual(self.manager.travels, [self.manager.travel1, self.manager.travel2, self.manager.travel3])

    def test_sort_by_price(self):
        self.manager.add_travel(self.manager.travel1)
        self.manager.add_travel(self.manager.travel2)
        self.manager.add_travel(self.manager.travel3)
        sorted_by_price_asc = self.manager.sort_by_price(TravelManager.SortOrder.ASC)
        self.assertEqual(sorted_by_price_asc, [self.manager.travel3, self.manager.travel2, self.manager.travel1])
        sorted_by_price_desc = self.manager.sort_by_price(TravelManager.SortOrder.DESC)
        self.assertEqual(sorted_by_price_desc, [self.manager.travel1, self.manager.travel2, self.manager.travel3])


if __name__ == "__main__":
    unittest.main()