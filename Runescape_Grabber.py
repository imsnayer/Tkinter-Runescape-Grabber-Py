from Tkinter import *
import ttk, urllib2, base64

#Tkinter Application
root = Tk()
root.title("RS Data Grabber")
root.minsize('650', '435')
root.maxsize('650', '435')

#Application Specifications
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Functions
def main(*args):
	global name
	name = nameVar.get()
	if " " in name:
		name = name.replace (" ", "_") #Swap Spaces with underscores for URL use
		setBlanks()
	else:
		setBlanks()

def setBlanks():
	errorValue.set("")
	attackValue.set("")
	defenseValue.set("")
	strengthValue.set("")
	constitutionValue.set("")
	rangeValue.set("")
	prayerValue.set("")
	magicValue.set("")
	cookingValue.set("")
	woodcuttingValue.set("")
	fletchingValue.set("")
	fishingValue.set("")
	firemakingValue.set("")
	craftingValue.set("")
	smithingValue.set("")
	miningValue.set("")
	herbloreValue.set("")
	agilityValue.set("")
	thievingValue.set("")
	slayerValue.set("")
	farmingValue.set("")
	runecraftingValue.set("")
	huntingValue.set("")
	constructionValue.set("")
	summoningValue.set("")
	dungeoneeringValue.set("")
	divinationValue.set("")
	grabPageStats()

def grabPageStats():
	global name
	global data
	url = "http://hiscore.runescape.com/index_lite.ws?player=%s" % (name)
	try:
		u = urllib2.urlopen(url)
		data = u.read()
		levelParse()
	except urllib2.HTTPError, error:
		contents = error.read()
		errorValue.set("Can't Find Player!")

def levelParse():
	global data
	data = data.split("\n")

	attack = data[1].split(",")
	attackValue.set(attack[1])
		
	defense = data[2].split(",")
	defenseValue.set(defense[1])

	strength = data[3].split(",")
	strengthValue.set(strength[1])
	
	constitution = data[4].split(",")
	constitutionValue.set(constitution[1])
	
	range = data[5].split(",")
	rangeValue.set(range[1])
	
	prayer = data[6].split(",")
	prayerValue.set(prayer[1])
	
	magic = data[7].split(",")
	magicValue.set(magic[1])

	cooking = data[8].split(",")
	cookingValue.set(cooking[1])

	woodcutting = data[9].split(",")
	woodcuttingValue.set(woodcutting[1])

	fletching = data[10].split(",")
	fletchingValue.set(fletching[1])

	fishing = data[11].split(",")
	fishingValue.set(fishing[1])

	firemaking = data[12].split(",")
	firemakingValue.set(firemaking[1])
	
	crafting = data[13].split(",")
	craftingValue.set(crafting[1])
	
	smithing = data[14].split(",")
	smithingValue.set(smithing[1])
	
	mining = data[15].split(",")
	miningValue.set(mining[1])
	
	herblore = data[16].split(",")
	herbloreValue.set(herblore[1])
	
	agility = data[17].split(",")
	agilityValue.set(agility[1])
	
	thieving = data[18].split(",")
	thievingValue.set(thieving[1])
	
	slayer = data[19].split(",")
	slayerValue.set(slayer[1])
	
	farming = data[20].split(",")
	farmingValue.set(farming[1])
	
	runecrafting = data[21].split(",")
	runecraftingValue.set(runecrafting[1])
	
	hunting = data[22].split(",")
	huntingValue.set(hunting[1])
	
	construction = data[23].split(",")
	constructionValue.set(construction[1])
	
	summoning = data[24].split(",")
	summoningValue.set(summoning[1])
	
	dungeoneering = data[25].split(",")
	dungeoneeringValue.set(dungeoneering[1])
	
	divination = data[26].split(",")
	divinationValue.set(divination[1])


#Values
dataVar = StringVar(mainframe)
nameVar = StringVar(mainframe)
attackValue = StringVar(mainframe)
defenseValue = StringVar(mainframe)
strengthValue = StringVar(mainframe)
constitutionValue = StringVar(mainframe)
rangeValue = StringVar(mainframe)
prayerValue = StringVar(mainframe)
magicValue = StringVar(mainframe)
cookingValue = StringVar(mainframe)
woodcuttingValue = StringVar(mainframe)
fletchingValue = StringVar(mainframe)
fishingValue = StringVar(mainframe)
firemakingValue = StringVar(mainframe)
craftingValue = StringVar(mainframe)
smithingValue = StringVar(mainframe)
miningValue = StringVar(mainframe)
herbloreValue = StringVar(mainframe)
agilityValue = StringVar(mainframe)
thievingValue = StringVar(mainframe)
slayerValue = StringVar(mainframe)
farmingValue = StringVar(mainframe)
runecraftingValue = StringVar(mainframe)
huntingValue = StringVar(mainframe)
constructionValue = StringVar(mainframe)
summoningValue = StringVar(mainframe)
dungeoneeringValue = StringVar(mainframe)
divinationValue = StringVar(mainframe)
errorValue = StringVar(mainframe)

#Value Labels
attackValueLabel = ttk.Label(mainframe, textvariable=attackValue)
defenseValueLabel = ttk.Label(mainframe, textvariable=defenseValue)
strengthValueLabel = ttk.Label(mainframe, textvariable=strengthValue)
constitutionValueLabel = ttk.Label(mainframe, textvariable=constitutionValue)
rangeValueLabel = ttk.Label(mainframe, textvariable=rangeValue)
prayerValueLabel = ttk.Label(mainframe, textvariable=prayerValue)
magicValueLabel = ttk.Label(mainframe, textvariable=magicValue)
cookingValueLabel = ttk.Label(mainframe, textvariable=cookingValue)
woodcuttingValueLabel = ttk.Label(mainframe, textvariable=woodcuttingValue)
fletchingValueLabel = ttk.Label(mainframe, textvariable=fletchingValue)
fishingValueLabel = ttk.Label(mainframe, textvariable=fishingValue)
firemakingValueLabel = ttk.Label(mainframe, textvariable=firemakingValue)
craftingValueLabel = ttk.Label(mainframe, textvariable=craftingValue)
smithingValueLabel = ttk.Label(mainframe, textvariable=smithingValue)
miningValueLabel = ttk.Label(mainframe, textvariable=miningValue)
herbloreValueLabel = ttk.Label(mainframe, textvariable=herbloreValue)
agilityValueLabel = ttk.Label(mainframe, textvariable=agilityValue)
thievingValueLabel = ttk.Label(mainframe, textvariable=thievingValue)
slayerValueLabel = ttk.Label(mainframe, textvariable=slayerValue)
farmingValueLabel = ttk.Label(mainframe, textvariable=farmingValue)
runecraftingValueLabel = ttk.Label(mainframe, textvariable=runecraftingValue)
huntingValueLabel = ttk.Label(mainframe, textvariable=huntingValue)
constructionValueLabel = ttk.Label(mainframe, textvariable=constructionValue)
summoningValueLabel = ttk.Label(mainframe, textvariable=summoningValue)
dungeoneeringValueLabel = ttk.Label(mainframe, textvariable=dungeoneeringValue)
divinationValueLabel = ttk.Label(mainframe, textvariable=divinationValue)
errorValueLabel = ttk.Label(mainframe, textvariable=errorValue)

#Skill Labels (Left Side)
attackLabel = ttk.Label(mainframe, text="Attack:" )
defenseLabel = ttk.Label(mainframe, text="Defense:" )
strengthLabel = ttk.Label(mainframe, text="Strength:" )
constitutionLabel = ttk.Label(mainframe, text="Constitution:" )
rangeLabel = ttk.Label(mainframe, text="Range:" )
prayerLabel = ttk.Label(mainframe, text="Prayer:" )
magicLabel = ttk.Label(mainframe, text="Magic:" )
cookingLabel = ttk.Label(mainframe, text="Cooking:" )
woodcuttingLabel = ttk.Label(mainframe, text="Woodcutting:" )
fletchingLabel = ttk.Label(mainframe, text="Fletching:" )
fishingLabel = ttk.Label(mainframe, text="Fishing:" )
firemakingLabel = ttk.Label(mainframe, text="Firemaking:" )
craftingLabel = ttk.Label(mainframe, text="Crafting:" )

#Skill Labels (Right Side)
smithingLabel = ttk.Label(mainframe, text="Smithing:" )
miningLabel = ttk.Label(mainframe, text="Mining:" )
herbloreLabel = ttk.Label(mainframe, text="Herblore:" )
agilityLabel = ttk.Label(mainframe, text="Agility:" )
thievingLabel = ttk.Label(mainframe, text="Thieving:" )
slayerLabel = ttk.Label(mainframe, text="Slayer:" )
farmingLabel = ttk.Label(mainframe, text="Farming:" )
runecraftingLabel = ttk.Label(mainframe, text="Runecrafting:" )
huntingLabel = ttk.Label(mainframe, text="Hunting:" )
constructionLabel = ttk.Label(mainframe, text="Construction:" )
summoningLabel = ttk.Label(mainframe, text="Summoning:" )
dungeoneeringLabel = ttk.Label(mainframe, text="Dungeoneering:" )
divinationLabel = ttk.Label(mainframe, text="Divination:" )

#Other Labels
titleLabel = ttk.Label(mainframe, text="RS Data Grabber")
spacer1Label = ttk.Label(mainframe, text="Spac")
spacer2Label = ttk.Label(mainframe, text="Spac")

#Buttons
grabButton = Button(mainframe, text="Grab Stats", command=main, foreground='#ff5346')

#Input
nameEntry = ttk.Entry(mainframe, width=20, textvariable=nameVar)

#Application Layout
titleLabel.grid(column=1, row=1, sticky=(W))
grabButton.grid(column=5, row=1, sticky=(W,E))
nameEntry.grid(column=3, row=1, sticky=(W,E))
spacer1Label.grid(column=2, row=1, sticky=(W,E))
spacer2Label.grid(column=4, row=1, sticky=(W,E))
errorValueLabel.grid(column=3, row=2, sticky=(W,E))

#Skills (Part 1) Layout
attackLabel.grid(column=1, row=2, sticky=(W))
defenseLabel.grid(column=1, row=3, sticky=(W))
strengthLabel.grid(column=1, row=4, sticky=(W))
constitutionLabel.grid(column=1, row=5, sticky=(W))
rangeLabel.grid(column=1, row=6, sticky=(W))
prayerLabel.grid(column=1, row=7, sticky=(W))
magicLabel.grid(column=1, row=8, sticky=(W))
cookingLabel.grid(column=1, row=9, sticky=(W))
woodcuttingLabel.grid(column=1, row=10, sticky=(W))
fletchingLabel.grid(column=1, row=11, sticky=(W))
fishingLabel.grid(column=1, row=12, sticky=(W))
firemakingLabel.grid(column=1, row=13, sticky=(W))
craftingLabel.grid(column=1, row=14, sticky=(W))

#Skills (Part 2) Layout
smithingLabel.grid(column=5, row=2, sticky=(W, E))
miningLabel.grid(column=5, row=3, sticky=(W, E))
herbloreLabel.grid(column=5, row=4, sticky=(W, E))
agilityLabel.grid(column=5, row=5, sticky=(W, E))
thievingLabel.grid(column=5, row=6, sticky=(W, E))
slayerLabel.grid(column=5, row=7, sticky=(W, E))
farmingLabel.grid(column=5, row=8, sticky=(W, E))
runecraftingLabel.grid(column=5, row=9, sticky=(W, E))
huntingLabel.grid(column=5, row=10, sticky=(W, E))
constructionLabel.grid(column=5, row=11, sticky=(W, E))
summoningLabel.grid(column=5, row=12, sticky=(W, E))
dungeoneeringLabel.grid(column=5, row=13, sticky=(W, E))
divinationLabel.grid(column=5, row=14, sticky=(W, E))

#Skills Number (Part 1) Layout
attackValueLabel.grid(column=2, row=2, sticky=(W))
defenseValueLabel.grid(column=2, row=3, sticky=(W))
strengthValueLabel.grid(column=2, row=4, sticky=(W))
constitutionValueLabel.grid(column=2, row=5, sticky=(W))
rangeValueLabel.grid(column=2, row=6, sticky=(W))
prayerValueLabel.grid(column=2, row=7, sticky=(W))
magicValueLabel.grid(column=2, row=8, sticky=(W))
cookingValueLabel.grid(column=2, row=9, sticky=(W))
woodcuttingValueLabel.grid(column=2, row=10, sticky=(W))
fletchingValueLabel.grid(column=2, row=11, sticky=(W))
fishingValueLabel.grid(column=2, row=12, sticky=(W))
firemakingValueLabel.grid(column=2, row=13, sticky=(W))
craftingValueLabel.grid(column=2, row=14, sticky=(W))

#Skills Number (Part 2) Layout
smithingValueLabel.grid(column=6, row=2, sticky=(W))
miningValueLabel.grid(column=6, row=3, sticky=(W))
herbloreValueLabel.grid(column=6, row=4, sticky=(W))
agilityValueLabel.grid(column=6, row=5, sticky=(W))
thievingValueLabel.grid(column=6, row=6, sticky=(W))
slayerValueLabel.grid(column=6, row=7, sticky=(W))
farmingValueLabel.grid(column=6, row=8, sticky=(W))
runecraftingValueLabel.grid(column=6, row=9, sticky=(W))
huntingValueLabel.grid(column=6, row=10, sticky=(W))
constructionValueLabel.grid(column=6, row=11, sticky=(W))
summoningValueLabel.grid(column=6, row=12, sticky=(W))
dungeoneeringValueLabel.grid(column=6, row=13, sticky=(W))
divinationValueLabel.grid(column=6, row=14, sticky=(W))


#Design
titleLabel.configure(font='sintony 18',foreground="#ff5346")
grabButton.configure(font='sintony 14',foreground="#ff5346")
spacer1Label.configure(font='sintony 14', foreground="#f0f0f0")
spacer2Label.configure(font='sintony 14', foreground="#f0f0f0")

#Label Design
attackLabel.configure(font='sintony 14', foreground="#ff5346")
defenseLabel.configure(font='sintony 14', foreground="#ff5346")
strengthLabel.configure(font='sintony 14', foreground="#ff5346")
constitutionLabel.configure(font='sintony 14', foreground="#ff5346")
rangeLabel.configure(font='sintony 14', foreground="#ff5346")
prayerLabel.configure(font='sintony 14', foreground="#ff5346")
magicLabel.configure(font='sintony 14', foreground="#ff5346")
cookingLabel.configure(font='sintony 14', foreground="#ff5346")
woodcuttingLabel.configure(font='sintony 14', foreground="#ff5346")
fletchingLabel.configure(font='sintony 14', foreground="#ff5346")
fishingLabel.configure(font='sintony 14', foreground="#ff5346")
firemakingLabel.configure(font='sintony 14', foreground="#ff5346")
craftingLabel.configure(font='sintony 14', foreground="#ff5346")
smithingLabel.configure(font='sintony 14', foreground="#ff5346")
miningLabel.configure(font='sintony 14', foreground="#ff5346")
herbloreLabel.configure(font='sintony 14', foreground="#ff5346")
agilityLabel.configure(font='sintony 14', foreground="#ff5346")
thievingLabel.configure(font='sintony 14', foreground="#ff5346")
slayerLabel.configure(font='sintony 14', foreground="#ff5346")
farmingLabel.configure(font='sintony 14', foreground="#ff5346")
runecraftingLabel.configure(font='sintony 14', foreground="#ff5346")
huntingLabel.configure(font='sintony 14', foreground="#ff5346")
constructionLabel.configure(font='sintony 14', foreground="#ff5346")
summoningLabel.configure(font='sintony 14', foreground="#ff5346")
dungeoneeringLabel.configure(font='sintony 14', foreground="#ff5346")
divinationLabel.configure(font='sintony 14', foreground="#ff5346")

#Value Label Design
attackValueLabel.configure(font='sintony 14', foreground="#ff5346")
defenseValueLabel.configure(font='sintony 14', foreground="#ff5346")
strengthValueLabel.configure(font='sintony 14', foreground="#ff5346")
constitutionValueLabel.configure(font='sintony 14', foreground="#ff5346")
rangeValueLabel.configure(font='sintony 14', foreground="#ff5346")
prayerValueLabel.configure(font='sintony 14', foreground="#ff5346")
magicValueLabel.configure(font='sintony 14', foreground="#ff5346")
cookingValueLabel.configure(font='sintony 14', foreground="#ff5346")
woodcuttingValueLabel.configure(font='sintony 14', foreground="#ff5346")
fletchingValueLabel.configure(font='sintony 14', foreground="#ff5346")
fishingValueLabel.configure(font='sintony 14', foreground="#ff5346")
firemakingValueLabel.configure(font='sintony 14', foreground="#ff5346")
craftingValueLabel.configure(font='sintony 14', foreground="#ff5346")
smithingValueLabel.configure(font='sintony 14', foreground="#ff5346")
miningValueLabel.configure(font='sintony 14', foreground="#ff5346")
herbloreValueLabel.configure(font='sintony 14', foreground="#ff5346")
agilityValueLabel.configure(font='sintony 14', foreground="#ff5346")
thievingValueLabel.configure(font='sintony 14', foreground="#ff5346")
slayerValueLabel.configure(font='sintony 14', foreground="#ff5346")
farmingValueLabel.configure(font='sintony 14', foreground="#ff5346")
runecraftingValueLabel.configure(font='sintony 14', foreground="#ff5346")
huntingValueLabel.configure(font='sintony 14', foreground="#ff5346")
constructionValueLabel.configure(font='sintony 14', foreground="#ff5346")
summoningValueLabel.configure(font='sintony 14', foreground="#ff5346")
dungeoneeringValueLabel.configure(font='sintony 14', foreground="#ff5346")
divinationValueLabel.configure(font='sintony 14', foreground="#ff5346")
errorValueLabel.configure(font='sintony 18', foreground="#ff5346")

nameEntry.focus()
root.bind('<Return>', main)

root.mainloop()