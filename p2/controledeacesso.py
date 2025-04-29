print('Controle de Acesso\n')
nome = input('Qual seu nome?: ')
cargo = input('Qual seu cargo?: ')
cargo_minusculo = cargo.lower()
destino = input('Qual seu destino?: ')
destino_minusculo = destino.lower()
horario = int(input('Qual o horário de acesso?: '))

if(cargo_minusculo != "gerente" and cargo_minusculo != "supervisor" and cargo_minusculo != "operador"):
    print('Cargo inválido!')
if(destino_minusculo != "data center" and destino_minusculo != "backup room"):
    print('Destino inválido!')
if(destino_minusculo == "data center"):
  if(cargo_minusculo == "gerente"):
    print('Acesso Liberado!')
  elif(cargo_minusculo == "supervisor"):
      if (horario >=9 and horario <=18):
        print('Acesso Liberado!')
      else:
        print('Acesso Proibido!')
  elif(cargo_minusculo == "operador"):
      if (horario >=9 and horario <=17):
        print('Acesso Liberado!')
      else:
        print('Acesso Proibido!')
if(destino_minusculo == "backup room"):
  if(cargo_minusculo == "gerente"):
      if (horario >=9 and horario <=18):
        print('Acesso Liberado!')
      else:
        print('Acesso Proibido!')
  elif(cargo_minusculo == "supervisor"):
      if (horario >=10 and horario <=16):
        print('Acesso Liberado!')
      else:
        print('Acesso Proibido!')
  elif(cargo_minusculo == "operador"):
      if (horario >=10 and horario <=14):
        print('Acesso Liberado!')
      else:
        print('Acesso Proibido!')