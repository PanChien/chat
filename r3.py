# 對話記錄整理_03 (其它的狀況處理)
# 當時間跟人名合在一起時，使用清單分割法來提取指定的文字

lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as  f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5] # 拿到時間，[0]裡面的前五個文字
    name = s[0][5:] # 拿到人名，[0]裡面第五個文字(包含)到最後一個字
    print(name)