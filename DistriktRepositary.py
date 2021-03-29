from Distrikt import Distrikt
import pickle


# noinspection SpellCheckingInspection,PyUnresolvedReferences
class Distrikten:
    """
    Klasse die eine Liste von Objekte von Typ Distrikt speichert.

    Attributes:
        distrikten (list): Eine Liste mit Instanzen der Klasse Distrikt
    """

    def __init__(self):
        """
        Konstruktor der Klasse Distrikten.
        Hier wird die Liste mit Distrikten gebaut. Die Daten fur jedes Distrikt werden aus einem Text Datei gelesen.
        """

        self.__distrikten = []

        # Die Datei mit alle Distrikte und Daten uber diese wird geoffnet und dem Text in die "text" Variable gespichert
        try:
            with open("housing.txt", "r") as txtfile:
                text = txtfile.readlines()
        except FileNotFoundError or FileExistsError as e:
            print(str(e))

        # Ein neues Binares Datei wird gebaut und in diese werden die Daten gepseichert
        try:
            outfile = open("distrikte", "wb")
            pickle.dump(text, outfile)
            outfile.close()
        except UnboundLocalError as e:
            print(str(e))

        # Aus dem Binaren Datei werden die neuen Daten gelesen und in dem Variable "new_text" gespeichert
        try:
            infile = open("distrikte", "rb")
            new_text = pickle.load(infile)
            infile.close()
            new_text = [line.split(",") for line in new_text]  # new_text ist eine Liste, jedes Element der Liste ist eine Reihe aus dem Text Datei

            # Hier wird die Liste populiert
            nr = 0  # Nr fur den Distrikten
            for atr in new_text:  # Jedes "atr" entspricht ein Element von jedem Linie, also eine Information
                try:  # Wenn es Information fur jeden Attribut des Distriktes gibt
                    distrikt = Distrikt(atr[0], atr[1], atr[2], atr[3], atr[4], atr[5], atr[6], atr[7], atr[8], atr[9], nr)
                    self.add_distrikt(distrikt)
                except ValueError:  # Wenn es keine Information fur jeden Attribut des Distriktes gibt, dann wird diese Distrikt nicht eingefugt
                    pass
                nr += 1
        except UnboundLocalError as e:
            print(str(e))
        except EOFError as e:
            print(str(e))

    def add_distrikt(self, distrikt):
        """
        Funktion um einen Objekt von Typ Distrikt in der Liste einzufugen

        Parameters:
            distrikt (Distrikt): Eine Instanz der Klasse Distrikt
        """

        self.__distrikten.append(distrikt)

    def get_distrikt(self, index):
        """
        Funktion um einen Objekt von Typ Distrikt in der Liste einzufugen

        Parameters:
            index (int): Ein index der Liste

        Returns:
             distrikt (Distrikt): Ein Element der Liste, der ein Objekt von Typ Distrikt ist
        """

        return self.__distrikten[index]

    @property
    def distrikten(self):
        return self.__distrikten

    @distrikten.setter
    def distrikten(self, new_distrikten):
        self.__distrikten = new_distrikten
