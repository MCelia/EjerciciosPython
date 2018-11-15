#AbstractFactory.py

class Dog:
    """A simple dog class"""

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"

class Cat:
    """A simple cat class"""

    def speak(self):
        return "Meow!"

    def __str__(self):
        return "Cat"
class CatFactory:
    """Concrete Factory"""
    def get_pet(self):
        """Return a Cat"""
        return Cat()

    def get_food(self):
        """Returns a Dog food object"""
        return "Wiskas"
    
class DogFactory:
    """Concrete Factory"""
    def get_pet(self):
        """Return a Dog"""
        return Dog()

    def get_food(self):
        """Returns a Dog food object"""
        return "DogChown"

class PetStore:
    """PetStore houses our Abstract Factory"""
    def  __init__(self, pet_factory=None):
        """pet_factory is our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects returned by the factory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        
        print("Our pet is '{}'".format(pet))
        print("Our pet say hello by '{}'".format(pet.speak()))
        print("Its food is '{}'".format(pet_food))

    def set_factory(self, pet_factory):
        self._pet_factory = pet_factory


#Create a Concrete Factory
dog_factory = DogFactory()
#Create a pet storehousing our  abstract factory
shop = PetStore(dog_factory)
shop.show_pet()
#Creae a Cat Factory
cat_factory = CatFactory()
shop.set_factory(cat_factory)
shop.show_pet()
