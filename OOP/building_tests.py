import unittest
from building, import Building, SkyScrapper, Bungalow

class BuildingTests(unittest.TestCase):
    """ Tests for the building class """

    def test_subclass_is_superclass(self):
        skyscrapper = SkyScrapper(50)
        bungalow = Bungalow()
        assert(isinstance(skyscrapper, Building), msg='skyscrapper should be a building')
        assert(isinstance(bungalow, Bungalow), msg='bungalow should be a building')

    def test_inheritance(self):
        bungalow = Bungalow()
        self.assertEquals(6, bungalow.foundation_depth,
                          msg='foundation depth should be 6')
