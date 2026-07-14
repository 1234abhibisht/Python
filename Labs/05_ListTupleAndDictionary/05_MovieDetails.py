#  5. Store details of n movies in a dictionary by taking input from the user. 
#  Each movie must store details like name,  year, director name, production cost, collection made (earning) & perform the following :-
#  a) print all movie details
#  b) display name of movies released before 2015
#  c) print movies that made a profit.
#  d) print movies directed by a particular director.

movieDetails = {}
n = int(input("Enter number of movies : "))
for i in range(n) :
    name = input("Enter name : ")
    movieDetails[name] = {}
    director = input("Enter director name : ")
    year = int(input("Enter release year : "))
    movieDetails[name]["releaseYear"] = year
    movieDetails[name]["directorName"] = director
    production = input("Enter production cost : ")
    movieDetails[name]["productionCost"] = production
    earnings = input("Enter earnings : ")
    movieDetails[name]["earnings"] = earnings
    
# a) 
print(movieDetails)

# b)
for i in movieDetails : 
    if(movieDetails[i]["releaseYear"]) < 2015 :
        print(i)

# c)
for i in movieDetails :
    if(movieDetails[i]["productionCost"] < movieDetails[i]["earnings"]) :
        print(i)
        
# d) 
# method 1
for i in range(len(movieDetails)) : 
    for j in range(i + 1, len(movieDetails)):
         if(movieDetails[i]["directorName"] == movieDetails[j]["directorName"]) :
            print(i, "and", j, "have same directors")
        
# d) 
# method 2
directorMap = {}

for i in movieDetails:
    director = movieDetails[i]["directorName"]
    
    if director not in directorMap:
        directorMap[director] = []
    
    directorMap[director].append(i)

for director in directorMap:
    if len(directorMap[director]) > 1:
        print("Director:", director)
        print("Movies:", directorMap[director])
