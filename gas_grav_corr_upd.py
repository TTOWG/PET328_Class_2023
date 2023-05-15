# input statements
co2_comp = input("What is the co2 composition? ")
n2_comp = input("What is the n2 compostition? ")
h2s_comp = input("What is the h2s composition?")
h20_comp = input("What is the h20 composition?")
gas_gravity = input("What is the measured gas gravity?")

#convert inputs to numerals
co2_comp = float(co2_comp)
n2_comp = float(n2_comp)
h2s_comp = float(h2s_comp)
h20_comp = float(h20_comp)
gas_gravity = float(gas_gravity)

#the if statement

if co2_comp < 0.12 or n2_comp < 0.03 or h2s_comp < 0:
    gas_gravity = (gas_gravity - (1.1767*h2s_comp) -\
                   (1.5196*co2_comp) - (0.9672*n2_comp) - \
                   (0.622*h20_comp))/(1 - h2s_comp - co2_comp - n2_comp -h20_comp)
    print("The corrected gas gravity is {0:.4f}". format(gas_gravity))

#continuing after the if block


#computing pseudo-critical pressure and temperature of the entire hydrocarbon mixture

p_pch = 756.8 - (131*gas_gravity)-(3.6*gas_gravity**2)
          
t_pch = 169.2 + (349.5*gas_gravity) - (74.0*gas_gravity**2)
          
P_pc = (1 - h2s_comp - co2_comp - n2_comp - h20_comp)*p_pch + 1306*h2s_comp \
      +1071*co2_comp + 493.1*n2_comp + 3200.1*h20_comp
          
T_pc = (1 - h2s_comp -co2_comp - n2_comp - h20_comp)*t_pch + 672.35*h2s_comp \
                                                      + 547.58*co2_comp + 227.16*n2_comp + 1164.9*h20_comp

#displaying the results
print("The hydrocarbon pseudo-critical pressure is {0:.1f} psia". format(p_pch))
print("The hydrocarbon pseudo-critical temperature is {0:.1f} deg Rankine". format(t_pch))
print("The hydrocarbon pseudo-reduced pressure is {0:.1f} psia". format(P_pc))
print("The hydrocarbon pseudo-reduced temperature is {0:.1f} deg Rankine". format(T_pc))
      
                                                      

                                                      

      


          
