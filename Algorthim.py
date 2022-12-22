
genre = input("What genre do you like? Use , to sepreate when you are listing mutiple genres") # Data Collecting
favmovies = input("What are instant classics for you? Use , to sepreate when you are listing mutiple movies") # Data Collecting
actors = input("What actors you wanna see more of Use , to sepreate when you are listing mutiple genres") # Data Collecting
moviestudiodata = input("What do you not like about the movies") # Data collecting
moviesholes = input("What stuff you like about movies?") # Data Collecting
favoritegenres = genre.split(',')# data stored in arrays
favoriteactors = actors.split(',')# data stored in arrays
favoritemovies = favmovies.split(',')# data stored in arrays
moviestudiosurvery = moviestudiodata.split(',')# data stored in arrays
movieholessurvery = moviesholes.split(',')# data stored in arrays
christmasmoviegenre = ["Christmas","Snowy","Spooky"] # Input data about the movie here
christmasmovieactors = ["DJ","KH","AK-47"] # Input data about the movie here
christmasmoviedoes = ["Cliche things","Kids movie","Bad"] # input data about the movie here
directorby = ['Movie2','Movie1','Movie3'] # input data about the movie here
goodthingsbaoutmovie = ['For kids','Singing','Good'] # input data about the movie here
christmasmoviecomparsion = any(elem in christmasmoviegenre  for elem in favoritegenres) # comparsion code
christmasmoviecomparsionall = all(elem in christmasmoviegenre  for elem in favoritegenres) # comparsion code
christmasmoviecomparsion2 = any(elem in christmasmovieactors  for elem in favoriteactors) # comparsion code
christmasmoviecomparsionall2 = all(elem in christmasmovieactors  for elem in favoriteactors) # comparsion code
christmasmoviecomparsion3 = any(elem in christmasmoviedoes  for elem in moviestudiosurvery) # comparsion code
christmasmoviecomparsionall3 = all(elem in christmasmoviedoes  for elem in moviestudiosurvery) # comparsion code
christmasmoviecomparsion4 = any(elem in directorby  for elem in favoritemovies) # comparsion code
christmasmoviecomparsionall4 = all(elem in directorby  for elem in favoritemovies) # comparsion code
christmasmoviecomparsion5 = any(elem in goodthingsbaoutmovie  for elem in movieholessurvery) # comparsion code
christmasmoviecomparsionall5 = all(elem in goodthingsbaoutmovie  for elem in movieholessurvery)# comparsion code
algorthimrecomendationtowardschristmasmovie = 0
doublerecomendinggenre=0 # double checking too not award too many points
doublerecomendingactors=0 # double checking not to award too many points
doublechecknegatives=0 # double checking not to award too many points
doublecheckdirectorbys=0 # double checking not to award too many points
doublecheckmoviegoodstuff=0 # double checking not to award too many points
if(christmasmoviecomparsionall == True):
    algorthimrecomendationtowardschristmasmovie+=1
    doublerecomendinggenre=1
else:
    algorthimrecomendationtowardschristmasmovie+=0
if(christmasmoviecomparsion == True and doublerecomendinggenre == 0):
    algorthimrecomendationtowardschristmasmovie+=0.5
else:
    algorthimrecomendationtowardschristmasmovie+=0
if(christmasmoviecomparsionall2 == True):
    algorthimrecomendationtowardschristmasmovie+=1
    doublerecomendingactors=1
else:
    algorthimrecomendationtowardschristmasmovie+=0
if(christmasmoviecomparsion2 == True and doublerecomendingactors == 0):
    algorthimrecomendationtowardschristmasmovie+=0.5
    doublerecomendingactors=0
else:
    algorthimrecomendationtowardschristmasmovie+=0
if(christmasmoviecomparsionall3 == True):
    algorthimrecomendationtowardschristmasmovie-=3
    doublechecknegatives=1
else:
    algorthimrecomendationtowardschristmasmovie+=0
if(christmasmoviecomparsion3 == True and doublechecknegatives == 1):
    algorthimrecomendationtowardschristmasmovie-=1.5
else:
    algorthimrecomendationtowardschristmasmovie+=0
if(christmasmoviecomparsionall4 == True):
    algorthimrecomendationtowardschristmasmovie+=1
    doublecheckdirectorbys=1
else:
    algorthimrecomendationtowardschristmasmovie+=0
if(christmasmoviecomparsion4 == True and doublecheckdirectorbys == 0):
    algorthimrecomendationtowardschristmasmovie+=1
else:
    algorthimrecomendationtowardschristmasmovie+=0
if(christmasmoviecomparsionall5 == True):
    algorthimrecomendationtowardschristmasmovie+=3
    doublecheckmoviegoodstuff=1
else:
    algorthimrecomendationtowardschristmasmovie+=0
if(christmasmoviecomparsion5 == True and doublecheckmoviegoodstuff == 0):
    algorthimrecomendationtowardschristmasmovie+=1

if(algorthimrecomendationtowardschristmasmovie > 6):
    print("We think you would love this title: Christmas Movie")
elif(algorthimrecomendationtowardschristmasmovie < 2):
    print("We think you would hate this title: Christmas Movie")
elif(algorthimrecomendationtowardschristmasmovie < 3):
    print("We think you would be meh with this title: Christmas Movie")
elif(algorthimrecomendationtowardschristmasmovie < 4):
    print("We think you would be fine with this title: Christmas Movie")
