

nome = input("Digite o seu nome: ")
valor_salario = float(input("Digite o valor do seu salário mensal: "))
percentual_bonus = float(input("Digite o percentual do bônus recebido: "))

bonus_recebido = ((valor_salario * percentual_bonus) + 1000)
print(f"Olá {nome}, seu bônus recebido foi: {bonus_recebido:.2F}.")
