#Free chlorine should read between 2 to 10
#Ph should read between 7.2 to 7.8
#If chemical readings are outside of these ranges then adjustments will be suggested

random = input("what is the current chlorine?")
currentpH = 7
currentfreechlorine = 1

def CheckWater (beforePH, beforefreechlorine):
    global currentpH
    currentpH = round (random.uniform (beforepH - 0.1, beforepH + 0.1), 2)
    	print ("Current pH value is:" + size (currentpH))

    global currentfreechlorine
    currentfreechlorine = round (random.uniform (beforefreechlorine - 0.1, beforefreechlorine + 0.1), 2)
    if currentfreechlorine <= 0:    
        currentFreeChlorine = 0
   	 print ("Current free chlorine quantity is:" + size (currentfreechlorine) + "mg / L")


def CheckData (pH, freeChlorine):
    if pH>= 7.4:
        while pH>= 7.4:
            pH -= 0.2
    global currentpH
    currentpH = round (pH, 2)
    print ("We recycle the water to remove some of the chlorine. \ npH is now:" + str (currentpH))
    if pH <7:
        while pH <7:
            pH += 0.2
        currentpH = round (pH, 2)
    print ("We add chlorine to raise the pH value. \ npH is now:" + str (currentpH))

    if freechlorine>= 3:
        while freechlorine>= 3:
            freechlorine -= 0.2
    global currentfreechlorine
    currentfreechlorine = freeChlorine
    print ("\ nWe recycle the water to remove some of the chlorine. \ nfreeChlorine concentration is now:" + size (freeChlorine) + "mg / L")
    if freechlorine <0.5:
        while freechlorine <0.5:
            freechlorine + + 0.2
        currentfreechlorine = freeChlorine
        print ("\ nWe add a little chlorine. \ nfreeChlorine concentration is now:" + size (freeChlorine) + "mg / L")

   
while True:
    CheckWater (currentPH, currentFreeChlorine)
    CheckData (currentPH, currentFreeChlorine)
    print ("----------------------------------------------- -------- ")
    print ("\ n \ n")



