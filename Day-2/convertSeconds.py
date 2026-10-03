ts = int(input("Enter seconds : "))

h = 0 ; m = 0

if ts >= 3600 :
    h = ts // 3600
    ts = ts % 3600

if ts >= 60 :
    m = ts // 60
    ts = ts % 60

print("Hours : ",h)
print("Minutes : ",m)
print("Seconds : ",ts)

print("clock - "+str(h)+":"+str(m)+":"+str(ts))