import tkinter
from random import randint

class Interface_graphique_perso(tkinter.Frame):

    def __init__(self, fenetre):
        tkinter.Frame.__init__(self, fenetre)
        self.grid()

        self.nom_joueur = tkinter.Label(self, text="Nom du joueur")
        self.nom_joueur.grid(column=0, row=0, padx=20)

        self.entree_joueur = tkinter.StringVar()
        self.joueur = tkinter.Entry(self, textvariable=self.entree_joueur)
        self.joueur.grid(column=1, row=0)

        self.nom_perso = tkinter.Label(self, text="Nom du Hero")
        self.nom_perso.grid(column=2, row=0, padx=20)

        self.entree_nom_perso = tkinter.StringVar()
        self.nom_perso = tkinter.Entry(self, textvariable=self.entree_nom_perso)
        self.nom_perso.grid(column=3, row=0)

        self.genre_choix = tkinter.IntVar()
        self.radio_genre_1 = tkinter.Radiobutton(self, text="Homme", value=1, variable=self.genre_choix)
        self.radio_genre_2 = tkinter.Radiobutton(self, text="Femme", value=2, variable=self.genre_choix)
        self.radio_genre_3 = tkinter.Radiobutton(self, text="Autre", value=3, variable=self.genre_choix)
        self.radio_genre_1.grid(column=4, row=0, padx=100, sticky="W")
        self.radio_genre_2.grid(column=4, row=1, padx=100, sticky="W")
        self.radio_genre_3.grid(column=4, row=2, padx=100, sticky="W")

        self.race_label = tkinter.Label(self, text="Choix de la race")
        self.race_label.grid(column=0, row=3)

        self.race_choix = tkinter.IntVar()
        self.radio_DE = tkinter.Radiobutton(self, text="Demi-Elfe", value=1, variable=self.race_choix)
        self.radio_DO = tkinter.Radiobutton(self, text="Demi-Orque", value=2, variable=self.race_choix)
        self.radio_EH = tkinter.Radiobutton(self, text="Elfe Haut", value=3, variable=self.race_choix)
        self.radio_ES = tkinter.Radiobutton(self, text="Elfe Sylvain", value=4, variable=self.race_choix)
        self.radio_Gn = tkinter.Radiobutton(self, text="Gnome", value=5, variable=self.race_choix)
        self.radio_Ha = tkinter.Radiobutton(self, text="Halfelin", value=6, variable=self.race_choix)
        self.radio_Hu = tkinter.Radiobutton(self, text="Humain", value=7, variable=self.race_choix)
        self.radio_Na = tkinter.Radiobutton(self, text="Nain", value=8, variable=self.race_choix)
        self.radio_DE.grid(column=0, row=4, sticky="W")
        self.radio_DO.grid(column=0, row=5, sticky="W")
        self.radio_EH.grid(column=0, row=6, sticky="W")
        self.radio_ES.grid(column=0, row=7, sticky="W")
        self.radio_Gn.grid(column=0, row=8, sticky="W")
        self.radio_Ha.grid(column=0, row=9, sticky="W")
        self.radio_Hu.grid(column=0, row=10, sticky="W")
        self.radio_Na.grid(column=0, row=11, sticky="W")

        # Sortie de la boucle
        self.Btn = tkinter.Button(self, text="Valider", width=5, height=2, command=self.quit)
        self.Btn.grid(column=2, row=12, sticky="se")



class Interface_Graphique_attribut(tkinter.Frame):

    roll = [randint(3, 18) for r in range(6)]  # Dés lancées pour la valeurs des caractériqtiques du personnage
    def __init__(self,fenetre):
        tkinter.Frame.__init__(self, fenetre)
        self.grid()


        self.roll_label = tkinter.Label(self,text="Génération alléatoire du lancé de dé:")
        self.roll_label.grid(column=1, row=1)
        self.roll = tkinter.Label(self, text=Interface_Graphique_attribut.roll,font=",25")
        self.roll.grid(column=2, row=1)
        self.force_label =tkinter.Label(self,text="Force:")
        self.force_label.grid(column=1, row=4)
        self.dext_label =tkinter.Label(self,text="Dexterité:")
        self.dext_label.grid(column=1, row=5)
        self.cons_label =tkinter.Label(self,text="Consitution:")
        self.cons_label.grid(column=1, row=6)
        self.intel_label =tkinter.Label(self,text="Intelligence:")
        self.intel_label.grid(column=1, row=7)
        self.sag_label =tkinter.Label(self,text="Sagesse:")
        self.sag_label.grid(column=1, row=8)
        self.char_label = tkinter.Label(self,text="Charisme:")
        self.char_label.grid(column=1, row=9)


class Interface_Graphique_Fiche(tkinter.Frame):
    pass



