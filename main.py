import sys

n = 4  # toplam 4 iş
m = 2  # her iş 2 farklı makinede yapılabiliyor

# Her işin her makinede ne kadar sürede tamamlandığı
processing = [
    [3, 6],   # 0. iş
    [4, 7],   # 1. iş
    [8, 4],   # 2. iş
    [5, 6]    # 3. iş
]

# Makineden makineye geçerken oluşan maliyetler
transition = [
    [0, 2],  # makine 0'dan → makine 0: 0, makine 1: 2
    [2, 0],   # makine 1'den → makine 0: 2, makine 1: 0
]

def printDP():
    for a in range(len(dp)):
        print(dp[a])
    print()

#DP tablosu oluşturma
dp = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(sys.maxsize)
    dp.append(row)

# İlk işler
for j in range(m):
    dp[0][j] = processing[0][j]  # ilk iş için herhangi bir geçiş yok

# Diğer işler
for i in range(1, n):            # 1. işten sonuncuya kadar
    for j in range(m):           # şu anki işin yapılacağı makine
        for k in range(m):       # bir önceki işin yapıldığı makine
            cost = dp[i-1][k] + transition[k][j] + processing[i][j]  # toplam süre
            if cost < dp[i][j]:  # daha kısa bir yol bulunursa güncellenir
                dp[i][j] = cost
                printDP()

# Minimum süre
min_total_time = min(dp[n-1])  # son satırdaki en küçük değer

print("Minimum toplam süre:", min_total_time)

