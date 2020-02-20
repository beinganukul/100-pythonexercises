class Car:
    name="Car"

    def __init__(self,name=None):
        self.name=name

honda=Car("Honda")
print("%s name is %s"%(Car.name,honda.name))

toyata=Car()
toyata.name="Toyata"
print("%s name is %s"%(Car.name,toyata.name))

