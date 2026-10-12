class Coordinates():

    defaults = {
        "absolu" : {
            "name" : "origin",
            "x" : 0,
            "y" : 0,
            "z" : 0,
            "description" : "origine absolue"
        }
    }

    def __init__(self, name, origin, x, y, z, description):
        self.name = self.defaults["absolu"]["name"]
        self.origin = self.defaults["absolu"],
        self.x = self.defaults["absolu"]["x"],
        self.y = self.defaults["absolu"]["y"],
        self.z = self.defaults["absolu"]["z"],
        self.description = self.defaults["absolu"]["description"], 

    @classmethod
    def __new__(cls):
        name = input("Enter a name :")
        origin = input("Change origin, default : 'absolu' (Y/N) ?")
        x = int(input("Enter a number :"))
        y = int(input("Enter a number :"))
        z = int(input("Enter a number :"))
        coordinates = (origin,x,y,z)
        description = input("Enter a description :")
        return cls(name, coordinates, description)


    @classmethod
    def __get__(cls, instance, name):
        if instance[name]:
            return cls(instance["coordinates"])
        else:
            raise KeyError("No object with that name")


    def __str__(self):
        return f"Coordinates of {self.name}, {self.description} : ({self.x}, {self.y}, {self.z})"


class Location(Coordinates):

    LOCATION_NATURES = {
        "Point" : ["", "", ""],
        "Espace" : ["", "", ""],
        "Environnement" : ["", "", ""],
    }

    LOCATION_TYPES = {
        "Reelle" : ["", "", ""],
        "Fictive" : ["", "", ""],
        "Virtuel" : ["", "", ""],
    }

    LOCATION_CATEGORIES = {
        "Univers" : ["", "", ""],
        "Astre" : ["", "", ""],
        "Territoire" : ["", "", ""],
        "Habitat" : ["", "", ""],
        "Propriété" : ["", "", ""],
    }

    limites = [
        {"A", "coordinates", "description"},
        {"B", "coordinates", "description"},
        {"C", "coordinates", "description"},
    ]

    def __init__(self, name, description, limites, nature, type, categorie):
        super.__init__(name, description)
        self.limites = limites
        self.nature = nature
        self.type = type
        self.categorie = categorie

    @classmethod
    def __new__(cls):
        A = Coordinates.__new__("A")
        B = Coordinates.__new__("B"),
        C = Coordinates.__new__("C")
        limites = [
            Coordinates.__get__(A, "A"),
            Coordinates.__get__(B,"B"),
            Coordinates.__get__(C, "C"),
        ]
        name = input("Enter a name :")
        description = input("Enter a description :")
        nature= input("Select nature")
        type = input("Select type")
        categorie = input("Select type")
        return cls(name, description, limites, nature, type, categorie)

    @classmethod
    def __get__(cls, instance, attribute):
        locations = []
        for i in instance[i]:
            if i == attribute:
                locations.append(cls(instance["name"]))
                return locations
            else:
                raise KeyError("No object with that name")      



class Position():
    ...
