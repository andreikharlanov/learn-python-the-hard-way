# assign the value of the variable "cars" to 100
cars = 100
# assign the value of the variable "space_in_a_car" to 4.0
space_in_a_car = 4.0
# assign the value of the variable "drivers" to 30
drivers = 30
# assign the value of the variable "passengers" to 90
passengers = 90
# assign the value of the variable "cars_not_driven" to the result of the addition operation of the value of the variable "cars" minus the value of the variable  "drivers"
cars_not_driven = cars - drivers
# assign the value of variable "passengers" to the value of variable "drivers"
cars_driven = drivers
# assign the value of the variable "carpool_capacity" to the result of the operation of multiplying the value of the variable "cars_driven" by * the value of the variable "space_in_a_car"
carpool_capacity = cars_driven * space_in_a_car
# assign the value of the variable "average_passengers_per_car" to the result of the operation of dividing the value of the variable "passengers" by * the value of the variable "cars_driven"
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transfer", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
