from tkinter import *
from COFICHEPERSO.GUI import GUI, GUI_Intro
from COFICHEPERSO.Character_Class import Character
import json
from random import randint
from pathlib import Path
from reportlab.pdfgen import canvas


def pdf_genrator(pdf):
    """ create a pdf with the value from player's selection"""

    image = Path("Images/fiche_perso.png")
    pdf.drawImage(image, 0, 0)
    pdf.drawString(400, 668, str(player.player_name), )
    pdf.drawString(145, 668, str(player.character_name))
    pdf.drawString(50, 623, str(player.profile_name))

    pdf.drawString(220, 623, str(player.race))
    pdf.drawString(342, 623, player.gender)
    pdf.drawString(430, 623, str(player.size) + "cm")
    pdf.drawString(388, 623, str(player.age) + "ans")
    pdf.drawString(470, 623, str(player.weight) + "Kg")

    pdf.drawString(80, 560, str(player.attribut["for"]))
    pdf.drawString(80, 538, str(player.attribut["dex"]))
    pdf.drawString(80, 515, str(player.attribut["con"]))
    pdf.drawString(80, 492, str(player.attribut["int"]))
    pdf.drawString(80, 470, str(player.attribut["sag"]))
    pdf.drawString(80, 450, str(player.attribut["cha"]))

    pdf.drawString(112, 560, str(player.attribut_modification["fom"]))
    pdf.drawString(112, 538, str(player.attribut_modification["dem"]))
    pdf.drawString(112, 515, str(player.attribut_modification["com"]))
    pdf.drawString(112, 492, str(player.attribut_modification["itm"]))
    pdf.drawString(112, 470, str(player.attribut_modification["sam"]))
    pdf.drawString(112, 450, str(player.attribut_modification["cam"]))

    pdf.drawString(427, 560, str(player.life_dice))
    pdf.drawString(175, 623, str(player.level))
    pdf.drawString(310, 538, str(player.level))
    pdf.drawString(310, 515, str(player.level))
    pdf.drawString(310, 492, str(player.level))

    pdf.drawString(270, 560, str(player.attribut_modification["dem"]))
    pdf.drawString(270, 538, str(player.attribut_modification["fom"]))
    pdf.drawString(270, 515, str(player.attribut_modification["dem"]))

    pdf.drawString(40, 400, str(player.racial_capacity))


def attribut_modification(player_attribut):
    """fonction who calcul the player bonus attribut"""
    table = {
        1: -4, 2: -4, 3: -4,
        4: -3, 5: -3, 6: -2,
        7: -2, 8: -1, 9: -1,
        10: 0, 11: 0, 12: 1,
        13: 1, 14: 2, 15: 2,
        16: 3, 17: 3, 18: 4,
        19: 4, 20: 5, 21: 5
    }

    for table_attribut_key, modification_value in table.items():
        if table_attribut_key == player_attribut:
            return modification_value


# loading Characters_race
characters_race_list = []
with open("json files/races_list.json", "r") as write_file:
    characters_race_list = json.load(write_file)

# loading Characters_profile
characters_profile_list = []
with open("json files/profiles_list.json", "r") as write_file:
    characters_profile_list = json.load(write_file)

window_intro = Tk()
image_intro = PhotoImage(file=Path("Images/Persos.png")).subsample(2)
IGU_intro = GUI_Intro(window_intro, image_intro)
window_intro.mainloop()

window = Tk()
roll = [randint(3, 18) for r in range(6)]
GUI_player_selection = GUI(window, roll, characters_race_list, characters_profile_list)
window.mainloop()

# race selected via GUI
race_user_selection = GUI_player_selection.lb_race.get(first=ANCHOR)
profile_user_selection = GUI_player_selection.lb_profile.get(first=ANCHOR)

# race's selection
for race in characters_race_list:
    if race_user_selection == race["race_name"]:
        race_selection = race

# character's selection
for profile in characters_profile_list:
    if profile_user_selection == profile["profile_name"]:
        profile_selection = profile

# player's creation
player = Character()
player.player_name = GUI_player_selection.player_name_entry.get()
player.character_name = GUI_player_selection.hero_name_entry.get()
player.race = race_user_selection
player.profile_name = profile_user_selection
player.life_dice = profile_selection["life_dice"]
player.racial_capacity = race_selection["capacite raciale"]

player.age = randint(race_selection["age"]["min"], race_selection["age"]["max"])
player.weight = randint(race_selection["taille"]["min"], race_selection["taille"]["max"])
player.size = randint(race_selection["taille"]["min"], race_selection["taille"]["max"])

player.attribut["for"] = int(GUI_player_selection.Str_Value.get()) + race_selection["modif"]["for"]
player.attribut["dex"] = int(GUI_player_selection.Dex_Value.get()) + race_selection["modif"]["dex"]
player.attribut["con"] = int(GUI_player_selection.Con_Value.get()) + race_selection["modif"]["con"]
player.attribut["int"] = int(GUI_player_selection.Dex_Value.get()) + race_selection["modif"]["int"]
player.attribut["sag"] = int(GUI_player_selection.Sag_Value.get()) + race_selection["modif"]["sag"]
player.attribut["cha"] = int(GUI_player_selection.Con_Value.get()) + race_selection["modif"]["cha"]
player.attribut_modification["fom"] = attribut_modification(player.attribut["for"])
player.attribut_modification["dem"] = attribut_modification(player.attribut["dex"])
player.attribut_modification["com"] = attribut_modification(player.attribut["con"])
player.attribut_modification["itm"] = attribut_modification(player.attribut["int"])
player.attribut_modification["sam"] = attribut_modification(player.attribut["sag"])
player.attribut_modification["cam"] = attribut_modification(player.attribut["cha"])

if GUI_player_selection.get_gender_value.get() == 4:
    player.gender = "Homme"
elif GUI_player_selection.get_gender_value.get() == 7:
    player.gender = "femme"
else:
    player.gender = "Autre"

# pdf's creation
name_pdf = str(player.player_name) + "_" + str(player.character_name) + ".pdf"
pdf = canvas.Canvas(name_pdf)
pdf_genrator(pdf)
pdf.showPage()
pdf.save()

print(player.attribut_modification)
print(player.attribut)