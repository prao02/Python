#permutations
from itertools import permutations
list,n=input().split()
print(*[''.join(i) for i in permutations(sorted(list),int(n))],sep='\n')

#combinations
from itertools import combinations
a,b = input().split()
print(*[''.join(j) for i in range(1,int(b)+1) for j in combinations(sorted(a),i)],sep='\n')

#combinations with replacement

from itertools import combinations_with_replacement
list,n=input().split()
print(*[''.join(i) for i in combinations_with_replacement(sorted(list),int(n))],sep = '\n')
