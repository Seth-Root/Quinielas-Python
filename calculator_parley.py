monto = int(input("escriba monto a jugar: \n"))
if (len (monto) < 1):
  print "Nada que hacer"
log1=log2=log3=log4=log5=log6=log7=log8=0
log1 = int(input("escriba el primer logro: \n"))
log2 = int(input("escriba el segundo logro: \n"))
log3 = int(input("escriba el tercer logro: \n"))
log4 = int(input("escriba el cuarto logro: \n"))
log5 = int(input("escriba el quinto logro: \n"))
log6 = int(input("escriba el sexto logro: \n"))
log7 = int(input("escriba el septimo logro: \n"))
log8 = int(input("escriba el octavo logro: \n"))
logros=[log1,log2,log3,log4,log5,log6,log7,log8]
num=[]
cantidad_de_logros = len(logros)
i = 0
for i in range(0,cantidad_de_logros):
  if logros[i]<= 0:
    LOG=(1+(logros[i]/100.0000))
    num.append(LOG)
  else:
    logros[i]= logros[i]*(-1)
    LOG=(1+(100.0000/logros[i]))
    num.append(LOG)
  i+=1
premio=monto*(num[0])*(num[1])*(num[2])*(num[3])*(num[4])*(num[5])*(num[6])*(num[7])
print premio