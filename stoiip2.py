 # TTOWG

area  = float(input("What is the area?"))
poro = float(input("What is the porosity?"))
h = float(input("What is the thickness?"))
swi = float(input("What is the initial water saturation?"))
boi = float(input("What is the oil formation volume factor?"))

N = (7758*area*h*poro*(1-swi))/boi
print('The stock tank oil in place is ', round(N))
