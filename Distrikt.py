# noinspection SpellCheckingInspection
class Distrikt:
    """
    Klasse fur ein Objekt von Typ Distrikt.

    Attributes:
         longitude (float): Longitude Koordinate des Distriktes
         latitude (float): Latitude Koordinate des Distriktes
         housing_median_age (float): Durchsnittliches Alter der Bevolkerung
         total_rooms (float): Anzahl der Zimmern in einem Distrikt
         total_bedrooms (float): Anzahl der Schlafzimmern in einem Distrikt
         population (float): Bevolkerung eines Distrikts
         households (float): Anzahl der Haushalte in einem Distrikt
         median_income (float): Durchschnittliches Einkommen in einem Distrikt
         median_house_value (float): Durchsnittliches Preis der Hauser in einem Distrikt
         ocean_proximity (string): Wo im Verglecih zu dem Ozean der Distrikt sich befindet
         nr (int): Nr des Distrikts
    """
    def __init__(self, longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households,
                 median_income, median_house_value, ocean_proximity, nr):
        """
        Konstruktor der Klasse Distrikt.
        Alle Attribute ausser ocean_proximity(string) und nr(int) sind float und werden hier geparset.

        Parameters:
             longitude (float): Longitude Koordinate des Distriktes
             latitude (float): Latitude Koordinate des Distriktes
             housing_median_age (float): Durchsnittliches Alter der Bevolkerung
             total_rooms (float): Anzahl der Zimmern in einem Distrikt
             total_bedrooms (float): Anzahl der Schlafzimmern in einem Distrikt
             population (float): Bevolkerung eines Distrikts
             households (float): Anzahl der Haushalte in einem Distrikt
             median_income (float): Durchschnittliches Einkommen in einem Distrikt
             median_house_value (float): Durchsnittliches Preis der Hauser in einem Distrikt
             ocean_proximity (string): Wo im Verglecih zu dem Ozean der Distrikt sich befindet
             nr (int): Nr des Distrikts
        """
        self.__longitude = float(longitude) - 2 * float(longitude)
        self.__latitude = float(latitude)
        self.__housing_median_age = float(housing_median_age)
        self.__total_rooms = float(total_rooms)
        self.__total_bedrooms = float(total_bedrooms)
        self.__population = float(population)
        self.__households = float(households)
        self.__median_income = float(median_income)
        self.__median_house_value = float(median_house_value)
        self.__ocean_proximity = ocean_proximity[:-1]
        self.__nr = int(nr)

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, long):
        self.__longitude = long

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, lati):
        self.__latitude = lati

    @property
    def housing_median_age(self):
        return self.__housing_median_age

    @housing_median_age.setter
    def housing_median_age(self, house):
        self.__housing_median_age = house

    @property
    def total_rooms(self):
        return self.__total_rooms

    @total_rooms.setter
    def total_rooms(self, total):
        self.__total_rooms = total

    @property
    def total_bedrooms(self):
        return self.__total_bedrooms

    @total_bedrooms.setter
    def total_bedrooms(self, total):
        self.__total_bedrooms = total

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, popul):
        self.__population = popul

    @property
    def households(self):
        return self.__households

    @households.setter
    def households(self, house):
        self.__households = house

    @property
    def median_income(self):
        return self.__median_income

    @median_income.setter
    def median_income(self, inc):
        self.__median_income = inc

    @property
    def median_house_value(self):
        return self.__median_house_value

    @median_house_value.setter
    def median_house_value(self, val):
        self.__median_house_value = val

    @property
    def ocean_proximity(self):
        return self.__ocean_proximity

    @ocean_proximity.setter
    def ocean_proximity(self, ocean):
        self.__ocean_proximity = ocean

    @property
    def nr(self):
        return self.__nr

    @nr.setter
    def nr(self, numar):
        self.__nr = numar

    def __str__(self):
        """
        Funktion die die print Methode fur einem Objekt von Typ Distrikt uberschreibt.

        Returns:
                Ein text der alle Daten eines Distrikt enthalt.
        """
        return "Das Distrikt mit dem Nr: " + str(self.__nr) + " von dem Koordinaten: " + str(self.__longitude) + ", " + \
               str(self.__latitude) + " hat folgende Eigenschaften:" + "\n" + "housing_median_age: " + \
               str(self.__housing_median_age) + "\n" + "total_rooms: " + str(self.__total_rooms) + "\n" + "total_bedrooms: " + \
               str(self.__total_bedrooms) + "\n" + "population: " + str(self.__population) + "\n" + "households: " + \
               str(self.__households) + "\n" + "median_income: " + str(self.__median_income) + "\n" + "median_house_value: " + \
               str(self.__median_house_value) + "\n" + "ocean_proximity: " + str(self.__ocean_proximity)
