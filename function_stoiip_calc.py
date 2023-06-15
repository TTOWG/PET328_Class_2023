# TTOWG!!!

########  A function to compute Stock Tank Oil Initially In-Place (STOIIP), N ########
def stoiip(area, thickness, poro, sw, boi):
    N = (7758*area*thickness*poro*(1-sw))/boi
    N = round(N, 2)
    return N 
