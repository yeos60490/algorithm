
def solution(text):
	answer = ''
	for i in text:
		if i.upper() >= 'A' and i.upper() <= 'M':
			answer += chr(ord(i)+13)
		elif i.upper() >'M' and i.upper() <= 'Z':
			answer += chr(ord(i)-13)
		else:
			answer += i

	return answer


if __name__ == '__main__':
	print(solution(input()))
