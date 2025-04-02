h1= 3
m1= 45
h2= 14
m2= 20
hora_total= h1+h2
minuto_total= m1+m2
if minuto_total>=60:
    hora_total+=1
    minuto_total-=60
    
if hora_total>=24:
    hora_total-=24
else:
    hora_total-=12
print(hora_total,minuto_total)




