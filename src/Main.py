import MlpPima as mlp

print("Olá! para calcular a probabilide de desenvolver diabetes, precisamos realizar algumas perguntas...\n\n")

sexo = float(input("Qual seu gênero biológico? \n1 - Feminino\n2 - Masculino\n"))

if sexo <= 0 or sexo > 2:
    print("Erro ao processar entrada")
    exit(1)

if sexo == 1:
    gravidezes = float(input("Digite quantas gravidezes: "))
else:
    gravidezes = float(0)

glicose = float(input("Digite o nível de glicose: "))
pressaoSanguinea = float(input("Digite o nível da pressão sanguínea: "))
pele = float(input("Digite a densidade pele: "))
insulina = float(input("Digite a quantidade de insulina: "))

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura (em cm): "))

indiceMassaCorporal = peso / (int(altura / 100) ^ 2)

funcaoLinhagemDiabetes = float(input("Digite a função de linhagem de diabetes: "))

idade = float(input("Digite a sua idade: "))

valores = [gravidezes, glicose, pressaoSanguinea, pele, insulina, indiceMassaCorporal, funcaoLinhagemDiabetes, idade]

result = mlp.ModelPredict([valores])

print(f'Resultado: {result[0]}')
