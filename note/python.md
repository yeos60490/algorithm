-----------
#### Note
- functools, sorted 

      import functools
      
      ## func 의 파라미터: (t1, t2) 리턴값: 1(t1이 클때), -1, 0
      sorted(array, key=functools.cmp_to_key(func)) 
      
      sorted(array, key=lambda x:x[1])
      

- collections 1 : counter (hash)

      import collections
      result = collections.Counter(list) 
      ##result = Counter({1: 개수, 2: 개수, 3: 개수})

- collections 2 : defaultdict

      from collections import defaultdict
      dict_a = defaultdict(list) ##list dict 로 init
      
- collections 3 : deque

      from collections import deque
      deq = deque()
      ##append, appendleft, pop, popleft, rotate, reserve, clear, remove, 
      
- collections 4 : OrderedDict

      from collections import OrderedDict
      dic = OrderedDict(zip(list1,list2)) ## zip은 두개의 리스트 key, value 로 합치기
      
      dic.popitem(last=True) ## 마지막 pop, False : 처음 pop
      dic.move_to_end(key, last=True) ## 마지막으로 이동, False : 처음으로 이동
      dic.update({key,value}) ## 새로운 것 삽입
          
- map, zip

      arr = list(map(int, str.split(" "))) ##str 을 int로 저장
      arr = list(zip(a,b)) ##a,b 는 arr
      arr = list(map(list, zip(*list))) ##행,열 뒤집기 
      arr = list(map(''.join(), arr))
      
- itertools

      import itertools
      arr = [1,2,3]
      list(itertools.combinations(arr, 3)) ## (1,2,3)
      list(itertools.permutations(arr,3)) ## (1,2,3) (2,1,3) (3,2,1) ...
      
- heapq (우선순위 큐 - 작은것)

      import heapq
      arr = [3,2,1,4]
      heapq.heapify(arr)
      heapq.heappush(arr, 2), heapq.heappop(arr)
      
- str

      str.startswith(str), str.endswith(str)
  
- deepcopy 
      
      import copy
      list2 = copy.deepcopy(list1) 
      
      
----------  
