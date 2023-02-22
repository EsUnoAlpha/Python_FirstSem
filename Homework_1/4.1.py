string = '3254543 79324234111000'
space = string.find (' ')
result1 = string[:8:]
result2 = string[8::]
result = result2 + string[7] + result1
print(result)

