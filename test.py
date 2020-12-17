"""
このファイルに解答コードを書いてください
"""

with open('input.txt') as f:
    s = f.read()
    s = s.split('\n')
    m = float(s[-2]) #floatだと30ケタまで表示されていない？
    s = s[:-2]
    s.sort()

dict_is = {}
for i in s:
    key = i.split(':')[0]
    key = int(key)
    value = i.split(':')[1]
    dict_is[key] = value

answer = ''
for i, s in dict_is.items():
    if m%i == 0:
        answer += s

if answer == '':
    answer = m

print(answer)