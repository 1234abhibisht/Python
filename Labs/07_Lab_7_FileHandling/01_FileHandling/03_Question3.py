#     3. Assume a file city.txt with details of 5 cities in given format (cityname population(in lakhs) area(in sq KM) ):
# Example:
# Dehradun 5.78 308.20
# Delhi 190 1484
# ……………
# Open file city.txt and read to:
#         a. Display details of all cities
#         b. Display city names with population more than 10Lakhs
#         c. Display sum of areas of all cities

f = open("city.txt","w+")
n = int(input("Enter number of cities to enter : "))
for i in range(n) :
    cityName = input("Enter city name : ")
    f.write(cityName + " ")
    cityPopulation = input("Enter city population : ")
    f.write(cityPopulation + " ")
    cityArea = input("Enter city area : ")
    f.write(cityArea + "\n")
f.seek(0)
data = f.readlines()
# now data = ['Dehradun 100000 1500\n', 'Delhi 200000 2000\n']

# remove \n from 
data = [i.strip() for i in data]
# data = ['Dehradun 100000 1500', 'Delhi 200000 2000']

# now we need to split whole string 'Dehradun 100000 1500', as it is a whole string and we 
# are unable to calculate sum

data = [i.split() for i in data]
# data = [['Dehradun','100000','1500'],['Delhi','200000','2000']]

# a)
print(data)

# b)
maxCityName = ""
for i in range(len(data)) : 
    if float(data[i][1]) > 1000000 :
        maxCityName = data[i][0]
print("City with max population : ",maxCityName)

# c)
sumAreas = 0
for i in range(len(data)) :
    sumAreas = sumAreas + float(data[i][2])
print("Sum of all areas of all cities : ",sumAreas)