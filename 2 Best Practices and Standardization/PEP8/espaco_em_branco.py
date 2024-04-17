"""Bad:
my_list = ( dog[ 2 ] , 5 , { "year": 1980 } , "string" )
if 5 in my_list : print( "Hello!" ) ; print( "Goodbye!" )
"""

# Good
my_list = ([2], 5, {"year": 1980}, "string")
if 5 in my_list:
    print("hello!")
print("Goodbye")
