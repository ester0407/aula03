nome= input("digite seu nome")
idade= int (input("digite sua idade"))
salario= float (input("digite seu salario"))
percentual=float(input("digite o percentual de aumento"))
valoraumento= salario*percentual/100
novosalario= salario+valoraumento

print(f" nome {nome} \nsua idade {idade} \nsalario { salario:.2f} \ne {valoraumento} \ne seu novo salario {novosalario:.2f}")
