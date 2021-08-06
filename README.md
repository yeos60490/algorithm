### algorithm study
-----------

- leetcode
- programmers
- 백준
- sql


-----------
#### Note
- functools, sorted 

      import functools
      
      ## func 의 파라미터: (t1, t2) 리턴값: 1(t1이 클때), -1, 0
      sorted(array, key=functools.cmp_to_key(func)) 
      
      sorted(array, key=lambda x:x[1])
      

- collections (hash)

      import collections
      result = collections.Counter(list) 
      ##result = Counter({1: 개수, 2: 개수, 3: 개수})


      from collections import defaultdict
      dict_a = defaultdict(list) ##list dict 로 init
      

- str

      str.startswith(str), str.endswith(str)
  
