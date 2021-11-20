#Free chlorine should read between 2 to 10
#Ph should read between 7.2 to 7.8
#If chemical readings are outside of these ranges then adjustments will be suggested

nuværendepH = 7
nuværendeFritKlor = 1
nuværendeBundetKlor = 0

def CheckWater(førpH, førFritKlor, førBundetKlor):
    global nuværendepH
    nuværendepH = round(random.uniform(førpH - 0.1, førpH + 0.1), 2)
    print("Nuværende pH værdi er: " + str(nuværendepH))

	global nuværendeFritKlor
	nuværendeFritKlor = round(random.uniform(førFritKlor - 0.1, førFritKlor + 0.1), 2)
	if nuværendeFritKlor <= 0:
		nuværendeFritKlor = 0
	print("Nuværende frit klor mængde er: " + str(nuværendeFritKlor) + " mg/L")

	
	global nuværendeBundetKlor
	nuværendeBundetKlor = round(random.uniform(førBundetKlor - 0.1, førBundetKlor + 0.1), 2)
	if nuværendeBundetKlor <= 0:
		nuværendeBundetKlor = 0
	print("Nuværende bundet klor mængde er: " + str(nuværendeBundetKlor) + " mg/L")                                                                 

def CheckData(pH, fritKlor, bundetKlor):
	if pH >=7.4:
	    while pH >= 7.4:
                pH -= 0.2
	global nuværendepH
	nuværendepH = round(pH, 2)
	print("Vi recirkulerer vandet, for at fjerne noget af kloret. \npH'en er nu: " + str(nuværendepH))
	if pH < 7:
	    while pH < 7:
	        pH += 0.2
	    nuværendepH = round(pH, 2)
	print("Vi tilføjer klor for at hæve pH værdien. \npH'en er nu: " + str(nuværendepH))
		
	if fritKlor >=3:
	    while fritKlor >= 3:
		    fritKlor -= 0.2
	global nuværendeFritKlor
	nuværendeFritKlor = fritKlor
	print("\nVi recirkulerer vandet, for at fjerne noget af kloret. \nfritKlor koncentrationen er nu: " + str(fritKlor) + " mg/L")
	if fritKlor < 0.5:
		while fritKlor < 0.5:
			fritKlor += 0.2
		nuværendeFritKlor = fritKlor
		print("\nVi tilsætter lidt klor. \nfritKlor koncentrationen er nu: " + str(fritKlor) + " mg/L")

	if bundetKlor >=1:
		while bundetKlor >= 1:
			bundetKlor -= 0.2
		global nuværendeBundetKlor
		nuværendeBundetKlor = bundetKlor
		print("Vi filtrere vand ud.\n bundetKlor koncentrationen er nu er nu: " + str(bundetKlor) + " mg/L")


	
while True: 
	CheckWater(nuværendepH,nuværendeFritKlor,nuværendeBundetKlor)
	CheckData(nuværendepH,nuværendeFritKlor,nuværendeBundetKlor)
	print("-------------------------------------------------------")
	print("\n\n")


