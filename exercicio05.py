nota1=int(input("digite a primeira nota"))
nota2=int(input("digite a segunda nota"))
nota3=int(input("digite a terceira nota"))
media= (nota1 + nota2 +nota3) /3
if media>=7:
    print(f" aprovado {media} ")
else:
    if media<4:
        print(f"reprovado{media}")
    else:
        print(f"recuperacao{media}")