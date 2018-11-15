class Borg:
    """Borg class making class attributes global"""
    #Attribute dictionary
    _shared_state = {}

    def __init__(self):
        #Make it an attribute dictionary
        self.__dict__=self._shared_state

class Singleton(Borg): #Inherits from the Borg Class
    """This class now share all its attributes among its various instances"""
    #This essenstially makes the singleton objects an object-oriented global variable
    def __init__(self, **kwargs):
        Borg.__init__(self)
        #Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        #Returns the attribute dictionary for printing
        return str(self._shared_state)

#Let's create a singleton object and add our firts acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")

#Print the object
print(x)

#Let's create another singleton object if it refers to the same attribute dictionary by adding another acronym}
y = Singleton(FTP="File Transfer Protocol")
#Print the object
print(y)
print(x)
