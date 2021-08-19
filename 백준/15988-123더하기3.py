arr = [0,1,2,4]

def solution(num):
    if num > 1000001: return 0 
    elif len(arr) <= num: ##arr길이보다 큰 수이면 새로 구
        for i in range(len(arr),num+1):
            arr.append((arr[i-1] + arr[i-2] + arr[i-3])%1000000009)

    return arr[num]

if __name__ == '__main__':
    for i in range(int(input())):
        print(solution(int(input())))
