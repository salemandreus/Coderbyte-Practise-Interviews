def FindIntersection(strArr):

    # Format into int sets
    mystrings = strArr.strip('"]["').replace(" ","").split('","')
    first, second = [set(map(int, mystring.split(","))) for mystring in mystrings]

    # Get intersection
    return list(first & second)

print(FindIntersection(input()))

# Test Input:
# ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]

# TODO:
# This works locally running Python 3.8!
# But somehow this doesn't work on the Coderbyte site - test cases and possibly running the code seems to
# do a list conversion in the background when using Python 3 - this should not be happening 🤔
