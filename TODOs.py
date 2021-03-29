from DistriktRepositary import Distrikten
from Interval import Interval


# noinspection SpellCheckingInspection,PyShadowingBuiltins,PyPep8Naming,PyShadowingNames,PyUnresolvedReferences
class TODOs:
    """
    Klasse die Funtkionen enthalt fur alle Wunsche des Kundes

    Attributes:
        DistriktenRepo (Distrikten): Eine Instanz der Klasse Distrikten
    """

    def __init__(self, distrikten_repo):
        """
        Konstruktor der Klasse TODOs

        Parameters:
            distrikten_repo (Distrikten): Ein Objekt von Typ Distrikten
        """

        self.__DistriktenRepo = distrikten_repo

    @property
    def DistriktenRepo(self):
        return self.__DistriktenRepo

    @DistriktenRepo.setter
    def DistriktenRepo(self, new_DistriktenRepo):
        self.__DistriktenRepo = new_DistriktenRepo

    def grosste_und_kleinste_bevolkerung(self):
        """
        Funktion, die den Distrikt mit der größten, bzw kleinster Bevölkerung findet und anschreibt

        """

        # Liste mit alle Daten des Distrikten uber Bevolkerung
        list_population = [distrikt.population for distrikt in self.__DistriktenRepo.distrikten]

        # Findet das Maximum aus der Liste mit Bevolkerung und den Index des Distrikts mit diesem Bevolkerung und schreibt diesen Distrikt an
        try:
            max_value = max(list_population)
            max_index = list_population.index(max_value)
            print(self.__DistriktenRepo.distrikten[max_index], "\nHAT DIE GROSSTE BEVOLKERUNG\n")

            # Findet das Minimum aus der Liste mit Bevolkerung und den Index des Distrikts mit diesem Bevolkerung und schreibt diesen Distrikt an
            min_value = min(list_population)
            min_index = list_population.index(min_value)
            print(self.__DistriktenRepo.distrikten[min_index], "\nHAT DIE KLEINSTE BEVOLKERUNG\n")
        except ValueError as e:
            print(str(e))

    def grosste_und_kleinste_anzahl_einwohner_pro_schlafzimmer(self):
        """
        Funktion, die den Distrikt mit der größten, bzw. kleinsten Anzahl von Einwohner pro Schlafzimmer findet und anschreibt

        """

        # Liste mit alle Daten des Distrikten uber Bevolkerung durch Anzahl der Schlafzimmern (also Liste mit Anzahl Einwohner pro Schalfzimmer in jedem Distrikt)
        list_eps = [distrikt.population / distrikt.total_bedrooms for distrikt in self.__DistriktenRepo.distrikten]

        try:
            # Findet das Maximum aus der Liste mit Anzahl Einwohner pro Schalfzimmer und den Index des Distrikts mit diesem Bevolkerung und schreibt diesen Distrikt an
            max_value = max(list_eps)
            max_index = list_eps.index(max_value)
            print(self.__DistriktenRepo.distrikten[max_index], "\nHAT DIE GROSSTE ANZAHL VON EINWOHNER PRO SCHLAFZIMMER:", max_value, "\n")

            # Findet das Minimum aus der Liste mit Anzahl Einwohner pro Schalfzimmer und den Index des Distrikts mit diesem Bevolkerung und schreibt diesen Distrikt an
            min_value = min(list_eps)
            min_index = list_eps.index(min_value)
            print(self.__DistriktenRepo.distrikten[min_index], "\nHAT DIE KLEINSTE ANZAHL VON EINWOHNER PRO SCHLAFZIMMER:", min_value, "\n")
        except ValueError as e:
            print(str(e))

    def durchschnittswert_anzahl_einwohner_pro_schlafzimmer(self):
        """
        Funktion, die den Durchsnitt der Anzahl von Einwohner pro Schlazimmern von jeden Distrikt findet und anschreibt

        """

        try:
            print("DURCHSNITTSWERT ANZAHL EINWOHNER PRO SCHLAFZIMMER:",
                  sum(distrikt.population / distrikt.total_bedrooms for distrikt in self.__DistriktenRepo.distrikten) / len(self.__DistriktenRepo.distrikten), "\n")
        except ZeroDivisionError as e:
            print(str(e))

    def durchschnittliche_alter_und_einkommen(self):
        """
        Funtkion, die dds durchschnittlichen Alter und den durchschnittlichen Einkommen der Einwohner findet und anschreibt

        """

        try:
            print("DURCHSNITTLICHE ALTER DER EINWOHNER:",
                  sum(distrikt.housing_median_age for distrikt in self.__DistriktenRepo.distrikten) / len(self.__DistriktenRepo.distrikten), "\n")

            print("DURCHSNITTLICHE EINKOMMEN DER EINWOHNER:",
                  sum(distrikt.median_income for distrikt in self.__DistriktenRepo.distrikten) / len(self.__DistriktenRepo.distrikten), "\n")
        except ZeroDivisionError as e:
            print(str(e))

    def ocean_proximity_attribute_und_anzahl_jedes_attribut(self):
        """
        Funtkion, die alle mogliche Werte des Attributes ocean_proximity und die Anzahl von Distrikte aus jeder Kategorie findet und anschreibt

        """

        # Baut ein set mit alle mogliche Werte (ausser lehre Spalte)
        try:
            set_attribute_ocean_proximity = set(distrikt.ocean_proximity for distrikt in self.__DistriktenRepo.distrikten if distrikt.ocean_proximity != '')

            # "counter" ist eine Liste und jedes Element ist die Anzahl von Distrikte aus diesem und entspricht einer Kategorie von den oberen gebauten set
            counter = []

            # Aus dem set wird eine Liste gemacht
            list_attribute_ocean_proximity = list(set_attribute_ocean_proximity)

            # Eine labmda Funktion fur vergleichen von zwei Werte
            ifequal = lambda atr1, atr2: atr1 == atr2

            # Fur jede Position aus dem "counter" liste wird die Summe aller Erscheinungen gespeichert
            s = sum(ifequal(list_attribute_ocean_proximity[0], distrikt.ocean_proximity) for distrikt in self.__DistriktenRepo.distrikten)
            counter.append(s)
            s = sum(ifequal(list_attribute_ocean_proximity[1], distrikt.ocean_proximity) for distrikt in self.__DistriktenRepo.distrikten)
            counter.append(s)
            s = sum(ifequal(list_attribute_ocean_proximity[2], distrikt.ocean_proximity) for distrikt in self.__DistriktenRepo.distrikten)
            counter.append(s)
            s = sum(ifequal(list_attribute_ocean_proximity[3], distrikt.ocean_proximity) for distrikt in self.__DistriktenRepo.distrikten)
            counter.append(s)
            s = sum(ifequal(list_attribute_ocean_proximity[4], distrikt.ocean_proximity) for distrikt in self.__DistriktenRepo.distrikten)
            counter.append(s)

            print("DIE 5 KATEGORISCHE ATTRIBUTE SIND:", ', '.join(set_attribute_ocean_proximity), "UND JEDES ERSCHEINT", counter, "MAL\n")
        except TypeError as e:
            print(str(e))
        except NameError as e:
            print(str(e))

    @staticmethod
    def change_preis(distrikt, new_preis):
        """
        Helper Funktion, um den Attribut median_house_value zu verandern

        Returns:
            distrikt (Distrikt): Instanz der Klasse Distrikt mit den veranderten Attribut median_house_value
        """
        try:
            distrikt.median_house_value = new_preis
            return distrikt
        except AttributeError as e:
            print(str(e))

    def preis_erhohen_distrikt_am_ozean(self):
        """
        Funktion, die den Preis für alle Häuser am Ozean um 10% erhoht

        """

        # Erhoht den Preis
        try:
            self.__DistriktenRepo.distrikten = list(map(lambda distrikt: self.change_preis(distrikt, distrikt.median_house_value + (0.1 * distrikt.median_house_value)) if distrikt.ocean_proximity == "NEAR OCEAN" else self.change_preis(distrikt, distrikt.median_house_value), self.__DistriktenRepo.distrikten))
        except AttributeError as e:
            print(str(e))

        # Schreibt alle Distrikte am Ozean, um zu sehen die gemachten Veranderungen
        try:
            with open("NewPreisAmOzean.txt", "w") as report:
                report.writelines([distrikt.__str__() + "\n\n" for distrikt in self.__DistriktenRepo.distrikten if distrikt.ocean_proximity == "NEAR OCEAN"])
        except AttributeError and UnboundLocalError as e:
            print(str(e))

    def report(self, interval_latitude, interval_longitude, interval_median_house_value):
        """
        Funktion, die einer Raport erstellt mit alle Distrikten, die sich in einigen bestimmten Intervalle von Werte befinden und diese in einem Text Datei schreibt.

        Parameters:
            interval_latitude (Interval): Objekt von Typ Interval fur latitude
            interval_longitude (Interval: Objekt von Typ Interval fur longitude
            interval_median_house_value (Interval: Objekt von Typ Interval fur median_house_value

        """

        # Baut eine neue Liste nur mit diejenigen distrikte, die sich in dem Interval befinden
        try:
            distrikte_im_interval = list(filter(lambda atr: interval_latitude.left < atr.latitude < interval_latitude.right and interval_longitude.left < atr.longitude < interval_longitude.right and interval_median_house_value.left < atr.median_house_value < interval_median_house_value.right, self.__DistriktenRepo.distrikten))

            with open("Report.txt", "w") as report:
                report.writelines([distrikt.__str__() + "\n\n" for distrikt in distrikte_im_interval])
        except AttributeError and UnboundLocalError as e:
            print("FEHLERMELDUNG\n" + str(e))

    def sort_median_house_value(self):
        """
        Funktion, die die Distrikte nach den Preis den Hausern steigend sortiert und schreibt die neue Liste in einem file, "Sorted_median_house_value" gennant

        """

        try:
            # Benutzt die definierte Funktion sorted, sortet nach median_house_value steigend
            self.__DistriktenRepo.distrikten = sorted(self.__DistriktenRepo.distrikten, key=lambda distrikt: distrikt.median_house_value)
            # Schreibt die veranderte Liste in dem file "Sorted_median_house_value.txt"
            with open("Sorted_median_house_value.txt", "w") as report:
                report.writelines([distrikt.__str__() + "\n\n" for distrikt in self.__DistriktenRepo.distrikten])
        except TypeError as e:
            print(str(e))

    def sort_ocean_proximity(self):
        """
        Funktion, die die Distrikte nach den Wert der Spalte ocean_proximity alphabetisch sortiert und schreibt die neue Liste in einem file, "Sorted_ocean_proximity" gennant

        """

        try:
            # Benutzt die definierte Funktion sort sortet nach ocean_proximity alphabetisch
            self.__DistriktenRepo.distrikten.sort(key=lambda d: d.ocean_proximity)
            # Schreibt die veranderte Liste in dem file "Sorted_ocean_proximity.txt"
            with open("Sorted_ocean_proximity.txt", "w") as report:
                report.writelines([distrikt.__str__() + "\n\n" for distrikt in self.__DistriktenRepo.distrikten])
        except TypeError as e:
            print(str(e))

    @staticmethod
    def get_kriterium():
        """
        Helper Funktion, die einem Kriterum nach denen zu filtern zuruck gibt

        Returns:
            kriterium : string
        """

        # Mogliche Kriterien
        kriterien = ["<", ">", "<=", ">=", "=", "Interval"]
        kriterium = input("Whalen sie einer der folgeden Kriterien: " + ", ".join(kriterien) + "\nIhre Wahl: ")

        # Wenn kriterium falsch gegeben wurde, wird dieses noch einmal gesuchen
        if kriterium not in kriterien:
            while kriterium not in kriterien:
                kriterium = input("Kriterium war nicht richtig gegeben\nWhalen sie einer der folgeden Kriterien: " + ", ".join(kriterien) + "\nIhre Wahl: ")

        return kriterium

    @staticmethod
    def get_spalte():
        """
        Helper Funktion, die eine Spalte nach welche gefiltern wird, zuruck gibt

        Returns:
            spalte : string
        """

        # Mogliche Spalten
        spalten = ["longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms", "population", "households",
                   "median_income", "median_house_value", "ocean_proximity", "nr"]
        spalte = input("Whalen sie eine der folgeden Spalten:\n" + ", ".join(spalten) + "\nIhre Wahl: ")

        # Wenn spalte falsch gegeben wurde, wird diese noch einmal gesuchen
        if spalte not in spalten:
            while spalte not in spalten:
                spalte = input("Spalte war nicht richtig gegeben\nWhalen sie eine der folgeden Spalten:\n" + ", ".join(spalten) + "\nIhre Wahl: ")

        return spalte

    def filter_nach_kriterum(self):
        kriterium = ""
        spalte = self.get_spalte()  # Spalte, nach welche gefiltern wird
        if spalte != "ocean_proximity":  # Kriterium nach denen zu filtern wenn die Spalte ocean_proximity ist kann nicht ein Vergleich Operator sein
            kriterium = self.get_kriterium()  # Kriterium, nach denen gefiltern wird und einen Wert "val" oder "interval" erzeugt
        new_filtered_list = []

        # val ist eine einzige float Variable wenn der kriterium kein "interval" ist und interval ist eine Instanz der Klasse Intervall wenn der kriterium "interval" ist
        try:
            if kriterium == "<" or kriterium == ">" or kriterium == "<=" or kriterium == ">=" or kriterium == "=":
                val = input("Geben sie ein Wert nach denen zu filtern: \nWert: ")
            elif kriterium == "Interval":
                interval = Interval(float(input("Wo der Interval beginnt: ")), float(input("\nWo der Interval endet: ")))
        except UnboundLocalError as e:
            print(str(e))
        except ValueError as e:
            print(str(e))

        # Wird die Funktion filter benutzt, jedes Filter hat eine entsprechende lambda Funktion, die das Wert von der Spalte mit gegeben Wert vergleicht
        # Mit .__dict__ wird das entsprechende Name der Spalte erhalten und vergleicht den Wert der Spalte mit das Wert val oder die Werte des Intervals
        try:
            if kriterium == "<":
                new_filtered_list = list(filter(lambda d: d.__dict__["_Distrikt__" + spalte] < float(val), self.__DistriktenRepo.distrikten))
            elif kriterium == ">":
                new_filtered_list = list(filter(lambda d: d.__dict__["_Distrikt__" + spalte] > float(val), self.__DistriktenRepo.distrikten))
            elif kriterium == "<=":
                new_filtered_list = list(filter(lambda d: d.__dict__["_Distrikt__" + spalte] <= float(val), self.__DistriktenRepo.distrikten))
            elif kriterium == ">=":
                new_filtered_list = list(filter(lambda d: d.__dict__["_Distrikt__" + spalte] >= float(val), self.__DistriktenRepo.distrikten))
            elif kriterium == "=":
                new_filtered_list = list(filter(lambda d: d.__dict__["_Distrikt__" + spalte] == float(val), self.__DistriktenRepo.distrikten))
            elif kriterium == "Interval":
                new_filtered_list = list(filter(lambda d: float(interval.left) < d.__dict__["_Distrikt__" + spalte] < float(interval.right), self.__DistriktenRepo.distrikten))
            elif spalte == "ocean_proximity":  # Wenn die Spalte kein float oder int hat, sondern ein string ist (also ocean_proximity)
                val = input("Geben sie ein Wert der Spalte ocean_proximity nach denen zu filtern: ")
                new_filtered_list = list(filter(lambda d: d.__dict__["_Distrikt__" + spalte] == val, self.__DistriktenRepo.distrikten))

            with open("Filtered_List.txt", "w") as report:
                report.writelines([distrikt.__str__() + "\n\n" for distrikt in new_filtered_list])
        except TypeError as e:
            print(str(e))
        except KeyError:
            print("Falsch gegebenen Namen der Spalte")
        except UnboundLocalError as e:
            print(str(e))

    def main(self):
        """
        Funtkion, die alle Methoden der Klasse TODOs benutzt

        """
        print("Die gescuchten Infos uber den Distrikten: \n")
        self.grosste_und_kleinste_bevolkerung()
        self.grosste_und_kleinste_anzahl_einwohner_pro_schlafzimmer()
        self.durchschnittswert_anzahl_einwohner_pro_schlafzimmer()
        self.durchschnittliche_alter_und_einkommen()
        self.ocean_proximity_attribute_und_anzahl_jedes_attribut()
        self.preis_erhohen_distrikt_am_ozean()
        interval_latitude = Interval(34, 36)
        interval_longitude = Interval(-118.54, -118.50)
        interval_median_house_value = Interval(5000, 600000)
        self.report(interval_latitude, interval_longitude, interval_median_house_value)
        self.sort_median_house_value()
        self.sort_ocean_proximity()
        print(self.filter_nach_kriterum())


d = Distrikten()
t = TODOs(d)
if __name__ == '__main__':
    t.main()
