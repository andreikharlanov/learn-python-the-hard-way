print "How many cubic meters of wood do we need for the floor replacement?"
print "The area of the floor that we need to replace is 13.34 meters by 4.18 meters."
print "So the square area is", 13.34 * 4.18, "square meters."

print "Lets assume that we'll need a beam every 50 cm."
print "Than we'll need 13.32 / 0.5 beams. It will be", 13.32 / 0.5, "beams."

print "Every beam is 4.18 + 0.4 meters long. That's", 4.18 + 0.4, "meters."

print "The other dimentions of the beam is 0.05 and 0.2 meters."
print "So the cubic volume of one beam is", (4.18 + 0.4) * 0.05 * 0.2, "cubic meters."
print "The cubic volumes of all the beams is", (4.18 + 0.4) * 0.05 * 0.2 * (13.32 / 0.5), "cubic meters."

print "If we use mango tree wood that costs 350 USD per cubic meter, than the price for the beams will be", (4.18 + 0.4) * 0.05 * 0.2 * (13.32 / 0.5) * 350, "USD."

print "If we use 5 cm thick wood for the floor, the cubic volume of wood for the floor will be 13.34 * 4.18 * 0.05. That's", 13.34 * 4.18 * 0.05, "cubic meters."
print "If we use 3 cm thick wood for the floor, the cubic volume of wood for the floor will be 13.34 * 4.18 * 0.03. That's", 13.34 * 4.18 * 0.03, "cubic meters."
print "If we use 2 cm thick wood for the floor, the cubic volume of wood for the floor will be 13.34 * 4.18 * 0.02. That's", 13.34 * 4.18 * 0.02, "cubic meters."

print "So, maximum cubic volume of wood that we'll need (assuming we use 5 cm thick wood) is", 13.34 * 4.18 * 0.05 + (4.18 + 0.4) * 0.05 * 0.2 * (13.32 / 0.5), "cubic meters."
print "Medium estimation (assuming we use 3 cm thick wood) is", 13.34 * 4.18 * 0.03 + (4.18 + 0.4) * 0.05 * 0.2 * (13.32 / 0.5), "cubic meters."
print "Minumum estimation (assuming we use 2 cm thick wood) is", 13.34 * 4.18 * 0.02 + (4.18 + 0.4) * 0.05 * 0.2 * (13.32 / 0.5), "cubic meters."

print "So, if we use mango wood (350 USD per cubic meter), the maximum, medium and minimum estinations are:"
print (13.34 * 4.18 * 0.05 + ((4.18 + 0.4) * 0.05 * 0.2 * (13.32 / 0.5))) * 350, "USD"
print (13.34 * 4.18 * 0.03 + ((4.18 + 0.4) * 0.05 * 0.2 * (13.32 / 0.5))) * 350, "USD"
print (13.34 * 4.18 * 0.02 + ((4.18 + 0.4) * 0.05 * 0.2 * (13.32 / 0.5))) * 350, "USD"

print "If we use hard wood (500 USD per cubic meter), the maximum, medium and minimum estinations are:"
print (13.34 * 4.18 * 0.05 + ((4.18 + 0.4) * 0.05 * 0.2 * (13.32 / 0.5))) * 500, "USD"
print (13.34 * 4.18 * 0.03 + ((4.18 + 0.4) * 0.05 * 0.2 * (13.32 / 0.5))) * 500, "USD"
print (13.34 * 4.18 * 0.02 + ((4.18 + 0.4) * 0.05 * 0.2 * (13.32 / 0.5))) * 500, "USD"
