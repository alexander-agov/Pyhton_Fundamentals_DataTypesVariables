
key = int(input())
num_lines = int(input())
str = ""
for i in range(1, num_lines+1):
    char = input()
    code = key + ord(char)
    str += chr(code)
print(str)
