import collections

def solution(genres, plays):
    answer = []
    count = collections.Counter() ## 장르 : 재생수 
    album = collections.defaultdict(list) ## 장르 : [(재생수, 고유번호),...]
    
    for i in range(len(genres)):
        count[genres[i]] += plays[i] ## 장르 재생수 합산
        
        album[genres[i]].append((plays[i],i)) ## (재생수, 고유번호)
        album[genres[i]] = sorted(album[genres[i]], key=lambda x:-x[0]) ##재생수 큰순서 + 고유번호 작은순
        album[genres[i]] = album[genres[i]][:2] ## 두개까지만 저장

    for i in count.most_common(): ## 총 재생수가 많은 장르 순
        for x in album[i[0]]: ## 고유번호만 출력하기 위해 
            answer.append(x[1])
        
    return answer
