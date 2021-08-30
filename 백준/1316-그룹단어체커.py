def solution(text):
    arr = [text[0]]

    for i in text[1:]:
        if i == arr[-1]: pass
        elif i not in arr: arr.append(i)
        elif i in arr: return False

    return True

if __name__ == '__main__':
    answer = 0
    for i in range(int(input())):
        answer += solution(input())

    print(answer)
