# Function for printing song name
def SongName():
    Sname = "Kya Tum Naraaz Ho?"
    print(Sname)
# Function for printing artist name
def Artist():
    Aname = "Tanmaya Bhatnagar"
    print(Aname)
# Function for returning genre of the song
def Genre():
    Gname = "Rhythm and blues"
    return Gname
# Using  bool function for returning True/False
Sname = "Kya Tum Naraaz"
def boolean():
    if Sname == "Kya Tum Naraaz Ho?" :
        return True
    else :
        return False
# calling function SongName to print Sname
SongName()
# calling function Artist to print Aname
Artist()
# Calling function Genre inside a print statement to print the return value
print(Genre())
# Calling function boolean inside a print statement to print the return value
print(boolean())