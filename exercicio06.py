litros= float(input("quantos litro?:"))
tipos= input("gasolina (g) ou etanol (e)?:")
valor_da_gasolina= 5.80
valor_do_etanol= 4.90
valor_total=0

if tipos== "g"
    print(f"voce escolheu gasolina {litros}")
    valor_total= valor_da_gasolina*litros
    print(f"valor total de: R$ {valor_total}")
else:

    print(f"voce escolheu etanol {litros}")
    valor_total= valor_do_etanol*litros
    print(f"seu valor_total de R$ {valor_total}")
