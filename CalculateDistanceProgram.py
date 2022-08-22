numberOfBuildings = int(input("Enter number of buildings in the society:"))
numberOfFloorsInEachBuilding = int(input("Enter number of floors in each building:"))
totalNumberOfParcels = int(input("Enter total number of parcels to be delivered:"))
listOfLocations = []
print("Enter delivery location for each parcel:(use format a-b where a is the building number & b is the floor number)")
for i in range(1,totalNumberOfParcels + 1):
    loc = input("location: ")
    listOfLocations.append(loc)

totalDistance = 0
#now apply formula for each location
for loc in listOfLocations:
    splitted = loc.split("-")
    buildingNumber = int(splitted[0])
    floorNumber = int(splitted[1])
    distPerParcel = int(2*(buildingNumber + floorNumber)) # twice of the distance required to reach from gate till floor
    totalDistance = totalDistance + distPerParcel

print("Total distance to be delivered by Delivery Boy (considering 1 unit distance between each building, floor & gate and building) is: %d Units" %(totalDistance))
