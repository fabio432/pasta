soma =0
cont_mulheres = 0
media = 0
maior = 0
nomeHomemMais_velho = '_'

for cont in range(1,4):
  nome = input('Digite seu nome: ')
  sexo = input('Masculino ou Feminino  [M/F]').upper()[0]
  idade = int(input('Digite sua idade: '))
  print('-' *20)
# number 1
  soma = soma + idade
  media = soma / cont

  if sexo == 'M' and idade > maior:
    maior = idade
    nomeHomemMais_velho = nome

  if sexo == 'F' and idade < 20:
    cont_mulheres += 1

print('Media das idades e de  {}'.format(media))
print('Nome do mais velho e {}'.format(nomeHomemMais_velho))

if cont_mulheres == 0:
  print('Nao temos mulhres no grupo !')

else:
  print('A todos temos {} mulheres com menor de 20 anos'.format(cont_mulhres))


lista = [item*1 for item in range(4)]
print(lista)

tuple = (['fabio', 'mentorama', '10', '100'])
x,t,b,z = tuple
print(tuple)

setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])

print(setx, sety, setz)

intercessao = setx & setz
print(intercessao)

print(setx.issubset(setz))

if 'x' in (setx & sety):
  print(x)

  DicionarioOrdenado = ([('color1','Red'),('color2','Green'),('color3','Blue')])
print(DicionarioOrdenado)
DicionarioOrdenado.insert(0,[('color4','Orange')])
print(DicionarioOrdenado)

s = 'hello'
print(s.rjust(70))

print(type(s.rjust(70)))

print(s.rjust(70))

s = 'hello'

print(s.rjust(70, '0'))

print(s.rjust(70))

def do_twice(func, arg):
  func(arg)
  func(arg)

def print_twice(arg):
  print(arg)
  print(arg)

def do_four(func, arg):
  do_twice(func, arg)
  do_twice(func, arg)

  do_twice(print, 'spam', '42')
  print('')

  do_four(print, 'spam', '42')
  print('')

  def sum(s, d):
  s = mensagem
  d = num1, num2
  return(s, d)
  print("imprime a mensagem {}\n, soma de dois numero {}")
  mensagem = float(input("Digite a mensagem: "))
  num1 = int(input("Digite um numero: "))
  num2 = int(input("Digite outro numero: "))

  print("")
  print("Digite a mensagem {}\n, o resultado da soma e %d {}" %sum(mensagem, num, num2))

  nome = input('Digite o seu nome:').upper()
print("parametro um: ",nome[::-1])

print("parametro dois: ",nome[::-2])
print("parametro tres: ",nome[::-3])

numero = input("Entre com o numero")
print("numero informado",numero[::-1])

print("numero invertido:",numero[::-2])
print("O numeroIvertido:",numero[::-3])
