number_of_lines = int ( input () )
balanced = True
open_bracket_found = False

for _ in range ( number_of_lines ) :
    line = input ().strip ()

    for char in line :
        if char == '(' :
            if open_bracket_found :
                balanced = False
            open_bracket_found = True
        elif char == ')' :
            if not open_bracket_found :
                balanced = False
            else :
                open_bracket_found = False

if open_bracket_found :  
    balanced = False

if balanced :
    print ( "BALANCED" )
else :
    print ( "UNBALANCED" )
