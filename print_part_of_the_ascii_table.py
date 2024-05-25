start_index = int(input())
last_character = int(input())
ascii_code = ""
for char in range(start_index, last_character+1):
    # if char == last_character:
        #print(chr(char))
    # else:
        # print(chr(char), end=" ")

    ascii_code += chr(char) + " "
print(ascii_code)
