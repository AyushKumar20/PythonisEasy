# Function to compare 3 inputs whether they are equal or not
def Compare(N1,N2,N3):
    # comparing if any 2 or all 3 inputs are equal
    if N1 == N2 or N1 == N3 or N2 == N3:
        return True
    else:
        return False

# Comparing string and integer values using in-build function int() below
def Comp(x,y):
    if x == int(y):
        return True
    else:
        return False

def main():
    # Passing different values to function with arguments
    print(Compare(0, 0, 1))
    print(Comp(5,"5"))

# Calling main function
main()