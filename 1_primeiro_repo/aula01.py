print("Exercício de Faturamento: ")

faturamento = 1200
custo = 700
imposto = faturamento * 0.1

lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento
novas_vendas = faturamento + 100

mensagemF = "O faturamento foi: "
mensagemC = "O custo foi: "
mensagemL = "O lucro foi de: "
mensagemM = "A margem de lucro foi: "
mensagemI = "O valor á pagar de imposto é: "
mensagemVF = "A soma com vendas atualizadas é: "

print(mensagemF, faturamento)
print(mensagemC, custo)
print(mensagemL, lucro)
print(mensagemM, margem_lucro)
print(mensagemI, imposto)
print(mensagemVF, novas_vendas)

teve_lucro = True
