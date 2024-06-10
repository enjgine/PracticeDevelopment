from os import system
def rocketequation_deltav(exhaust: float, startmass: float,finalmass: float):
	deltav = exhaust * numpy.log( startmass / finalmass )
	return(deltav)

def rocketequation_startmass(deltav: float,exhaust: float,finalmass: float):
	startmass = finalmass * numpy.exp( deltav / exhaust )
	return(startmass)

def rocketequation_finalmass(deltav: float,exhaust: float,startmass: float):
	finalmass = startmass * numpy.exp(-( deltav / exhaust ))
	return(finalmass)


while True:
	match int(input("Find:\n 1: Delta-V \n 2: Starting Mass \n 3: Final Mass \n 4: Exit \n")):
		case 1:
			print(rocketequation_deltav(float(input("Exhaust Speed:")), float(input("Starting Mass:")), float(input("Final Mass:"))))
			input()
		case 2:
			print(rocketequation_startmass(float(input("Delta-V:")), float(input("Exhaust Speed:")), float(input("Final Mass:"))))
			input()
		case 3:
			print(rocketequation_finalmass(float(input("Delta-V:")), float(input("Exhaust Speed:")), float(input("Start Mass:"))))
			input()
		case _:
			input("The code has ended")
			break