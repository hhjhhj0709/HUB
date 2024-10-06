h, m =map(int, input().split())
time = int(input())

if m + time < 60 :
  m = m + time
elif m + time == 60 :
  h += 1
  m = 0
elif m + time > 60 :
  h  =  h + (m + time) // 60
  m = (m + time) % 60

if h >= 24 :
  h = h - 24

print(h, m)