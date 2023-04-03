
class fruit:
    def __init__ (self, fresh, colour, shape):
        self.fresh = fresh
        self.colour = colour
        self.shape = shape

    def SetColour(self,colour):
        self.colour = colour

class banana(fruit):
    def __init__(self, fresh, colour, shape, ripe):
        super().__init__(fresh, colour, shape)
        self.ripe = ripe


banana_ripe = banana(True,"yellow","long, slightly curved", True)

print(banana_ripe.colour)

banana_ripe.SetColour("black")

print(banana_ripe.colour)