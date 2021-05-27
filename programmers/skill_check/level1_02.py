def solution(strings, n):
    strings.sort()
    if n==0:
        return strings

    strings.sort(key=lambda strings: strings[n])
    return strings
