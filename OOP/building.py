class Building:
    """ A building with the basic components """

    def __init__(self, kind = 'basic'):
        self.type = kind
        self.foundation_depth = 6
        self.walls = 4
        self.roof = 'iron sheets'
        self.doors = 2
        self.windows = 2

    def build(self):
        """ Builds the house """
        
        print('Laying foundation {} feet deep'.format(self.foundation_depth))
        print('Building {} walls'.format(self.walls))
        print('Placing {0} windows and {1} doors'.format(self.windows, self.doors))
        print('Placing a roof made of {}'.format(self.roof))

class SkyScrapper(Building):
    """ A skyscrapper building """

    def __init__(self, floors):
        self.kind = 'commercial'
        self.foundation_depth = 50
        self.walls = 400
        self.roof = 'concrete'
        self.doors = 650
        self.windows = 5000
        self.floors = floors

    def wash_windows(floors):
        print('Hiring labour to wash windows on {} floors'
              .format(floors if floors <= self.floors) else self.floors)

class Bungalow(Building):
    """ A residential bungalow """

    def __init__(self):
        self.kind = 'residential'
        super(Bungalow, self).__init__(self.kind)
        self.walls = 12
        self.doors = 6
        self.windows = 6
        self.bedrooms = 3

    def getNumberOfBedrooms(self):
        return self.bedrooms
    
