origin = input()
after = ''

for i in origin:
	if (i >= 'A' and i <= 'M') or (i >= 'a' and i <= 'm'):
		after += chr(ord(i)+13)
	elif (i >'M' and i <= 'Z') or (i > 'm' and i <= 'z'):
		after += chr(ord(i)-13)
	else:
		after += i

print(after)
