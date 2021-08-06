
def solution(text):
    answer = ''
    for i in text:
        if (i >= 'A' and i <= 'M') or (i >= 'a' and i <= 'm'):
            answer += chr(ord(i)+13)
        elif (i >'M' and i <= 'Z') or (i > 'm' and i <= 'z'):
            answer += chr(ord(i)-13)
        else:
            answer += i

    return answer


if __name__ == '__main__':
    print(solution(input()))
