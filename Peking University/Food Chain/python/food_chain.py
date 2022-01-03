# Reference
# 1. https://procon-nenuon61.hatenablog.com/entry/2017/03/01/030338
# 2. http://dminor11th.blogspot.com/2011/11/union-find.html

# Input
N, K = map(int, input().split())
T = list(map(int, input().split()))
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

# Union Find/Disjoint Set
class UnionFind():
    
    def __init__(self, n):
        self.n = n
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[x]:
                self.rank[x] += 1
            
    def same(self, x, y):
        return self.find(x) == self.find(y)

# Initializing Union Find
# x, x + N, x + 2 * N are the elements of x-A, x-B and x-C
UF = UnionFind(N * 3)

ans = 0
for i in range(K):
    
    t = T[i]
    x = X[i] - 1
    y = Y[i] - 1
    
    if x < 0 or N <= x or y < 0 or N <= y:
        ans += 1
        continue
    
    if t == 1:
        # 同じなのに違う種類だったら矛盾
        if UF.same(x, y + N) or UF.same(x, y + 2 * N):
            ans += 1
        # 矛盾がなかったら情報を更新
        else:
            UF.unite(x, y)
            UF.unite(x + N, y + N)
            UF.unite(x + N * 2, y + N * 2)
    # 弱肉強食xがyを食う
    else:
        # xがyを食うんだからx_Aとy_Aが同じグループだとダメ
        # x_Aとy_Cが同じグループだと強弱が逆だからダメ
        if UF.same(x, y) or UF.same(x, y + 2 * N):
            ans += 1
        # 矛盾がなかったら情報を更新
        else:
            UF.unite(x, y + N)
            UF.unite(x + N, y + 2 * N)
            UF.unite(x + 2 * N, y)
    
print(ans)