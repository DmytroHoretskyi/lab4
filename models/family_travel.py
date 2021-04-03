from models.travel import Travel


class FamilyTravel(Travel):
    def __init__(self, with_kids: bool, kids_zone: bool, country, producer, price, category):
        self.with_kids = with_kids
        self.kids_zone = kids_zone
        Travel.__init__(self, country, producer, price, category)