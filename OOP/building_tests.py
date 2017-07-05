import unittest
from building import Building, SkyScrapper, Bungalow

class BuildingTests(unittest.TestCase):
    """ Tests for the building class """

    def test_subclass_is_superclass(self):
        skyscrapper = SkyScrapper(50)
        bungalow = Bungalow()
        assert(isinstance(skyscrapper, Building))
        assert(isinstance(bungalow, Bungalow))

    def test_inheritance(self):
        bungalow = Bungalow()
        self.assertEquals(6, bungalow.foundation_depth,
                          msg='foundation depth should be 6')

if __name__ == '__main__':
    unittest.main()
