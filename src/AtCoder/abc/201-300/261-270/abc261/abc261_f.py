import sys
class SortedList:
    def __init__(self,n=20):
        if not 1<=n<=20:#0~1,048,575
            print('Error: not 1<=n<=20', file=sys.stderr)
            sys.exit(1)
        self.n=n
        self.b=[]
        for i in range(self.n+1):
            self.b.append([0 for j in range(2**i)])
    def __len__(self):
        return self.b[0][0]
    def __contains__(self,x):
        if not 0<=x<2**self.n:
            print('Error: not 0<=x<2**n', file=sys.stderr)
            sys.exit(1)
        return 0!=self.b[self.n][x]
    def __getitem__(self,x):
        if not 0<=x<self.b[0][0]:
            print('Error: not 0<=x<len', file=sys.stderr)
            sys.exit(1)
        s=0
        a=0
        for i in range(1,self.n+1):
            if s+self.b[i][2*a]<=x:
                s+=self.b[i][2*a]
                a=2*a+1
            else:
                a=2*a
        return a
    def __iter__(self):
        self._a=-1
        return self
    def __next__(self):
        self._a+=1
        if self._a>=self.b[0][0]:
            raise StopIteration
        return self.__getitem__(self._a)
    def insert(self,x):
        if not 0<=x<2**self.n:
            print('Error: not 0<=x<2**n', file=sys.stderr)
            sys.exit(1)
        for i in range(self.n+1):
            self.b[i][x//(2**(self.n-i))]+=1
    def eject(self,x):
        if not 0<=x<2**self.n:
            print('Error: not 0<=x<2**n', file=sys.stderr)
            sys.exit(1)
        if not self.__contains__(x):
            print('Error: not x in', file=sys.stderr)
            sys.exit(1)
        for i in range(self.n+1):
            self.b[i][x//(2**(self.n-i))]-=1
    def pop(self,x=0):
        p=self.__getitem__(x)
        self.eject(p)
        return p
    def remove(self,x):
        a=self.b[self.n][x]
        for i in range(self.n+1):
            self.b[i][x//(2**(self.n-i))]-=a
    def min(self,x=None):
        if x==None:
            x=-1
        elif x>=2**self.n-1:
            return None
        elif x<0:
            x=-1
        for i in range(self.n):
            if self.b[self.n-i][x//(2**i)+1]:
                a=x//(2**i)+1
                for j in reversed(range(i)):
                    if self.b[self.n-j][2*a]:
                        a=2*a
                    else:
                        a=2*a+1
                return a
    def max(self,x=None):
        if x==None:
            x=2**self.n
        elif x<=0:
            return None
        elif 2**self.n<=x:
            x=2**self.n
        for i in range(self.n):
            if self.b[self.n-i][x//(2**i)-1]:
                a=x//(2**i)-1
                for j in reversed(range(i)):
                    if self.b[self.n-j][2*a+1]:
                        a=2*a+1
                    else:
                        a=2*a
                return a
    def bisect_left(self,x):
        if not 0<=x<2**self.n:
            print('Error: not 0<=x<2**n', file=sys.stderr)
            sys.exit(1)
        a=0
        for i in range(self.n):
            if x%2==1:
                a+=self.b[self.n-i][x-1]
            x=x//2
        return a
    def bisect_right(self,x):
        if not 0<=x<2**self.n:
            print('Error: not 0<=x<2**n', file=sys.stderr)
            sys.exit(1)
        return self.bisect_left(x)+self.b[self.n][x]

N = int(input())
C = list(map(int, input().split()))
X = list(map(int, input().split()))
dic = {}
lis = []
for i in range(N):
    if C[i] in dic:
        dic[C[i]].append(X[i])
    else:
        dic[C[i]] = [X[i]]
for i in dic:
    dic[i].sort()
for i in range()
