from TODOs import TODOs
from DistriktRepositary import Distrikten


class Tests:

    def __init__(self):
        d = Distrikten()
        t = TODOs(d)
        self.__testlist = t

    def test_bauen_distrikt(self):
        distrikt2 = self.__testlist.DistriktenRepo.distrikten[2]
        assert distrikt2.longitude == -122.24
        assert distrikt2.latitude == 37.85
        assert distrikt2.housing_median_age == 52
        assert distrikt2.total_rooms == 1467
        assert distrikt2.total_bedrooms == 190
        assert distrikt2.population == 496
        assert distrikt2.households == 177
        assert distrikt2.median_income == 7.2574
        assert distrikt2.median_house_value == 352100
        assert distrikt2.ocean_proximity == "NEAR BAY"
        assert distrikt2.nr == 2

    def test_preis_erhohen_distrikt_am_ozean(self):
        self.__testlist.preis_erhohen_distrikt_am_ozean()
        assert self.__testlist.DistriktenRepo.distrikten[1850].median_house_value != 428600
        assert self.__testlist.DistriktenRepo.distrikten[1851].median_house_value != 357600
        assert self.__testlist.DistriktenRepo.distrikten[20421].median_house_value != 325900


Test = Tests()
Test.test_bauen_distrikt()
Test.test_preis_erhohen_distrikt_am_ozean()
