
def solution(arr):
	pair = sum(arr) - 100

	for i in arr:
		if pair - i in arr and pair -i != i:
			arr.remove(pair-i)
			arr.remove(i)
			return sorted(arr)

	return arr


if __name__ == '__main__':
	arr = [int(input()) for i in range(9)] 
	arr = solution(arr)
	for i in arr: print(i)
