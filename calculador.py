tipo_pneu = "Preto"
creditos = 4

preco_pneu = 0
preco_final = 0
if tipo_pneu == "tipoX":
    preco_pneu = 20.90
elif tipo_pneu == "Preto":
    preco_pneu = 31.45
else:
    tipo_pneu = 18
print("Preço do pneu: ")
print(preco_pneu)

if creditos > 0 :
    preco_final = preco_pneu - creditos

print("Preço final:")
print(preco_final)