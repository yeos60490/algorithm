## https://www.acmicpc.net/problem/14405

def solution(text):
    text = text.replace("pi", "1").replace("ka", "1").replace("chu", "1").replace("1", "")

    return "NO" if text else "YES"

if __name__ == '__main__':
    print(solution(input()))
