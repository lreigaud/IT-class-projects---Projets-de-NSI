l = [3, 5]
for i in range (1000):
  t = l[i] * l[i+1]
  if t >= 10 :
    l.append(t//10)
    l.append(t%10)
  else:
    l.append(t)
print (l)

print (l.count(0)) 
print (l.count(1))
print (l.count(2))
print (l.count(3))
print (l.count(4))
print (l.count(5))
print (l.count(6))
print (l.count(7))
print (l.count(8))
print (l.count(9))