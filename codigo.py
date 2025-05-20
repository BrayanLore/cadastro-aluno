def cadastro_aluno(nome, turma, cgm):
  print("O aluno foi cadastrado!")
  print("Seu nome é: ")
  print("Sua turma:")
  print("CGM: ")
  opcao = input ("Deseja ver o cadastro? Digite 'S' p/ ver: ")
  if opcao == 's' or opcao == 'S':
    print (f"{nome}, {turma}, {cgm}")
  else:
    print("Obrigado por fazer o cadastro!")

nome = input("Seu nome: ")
cgm = input("Insira CGM: ")
turma = input("Sua turma: ")
cadastro_aluno(nome, turma, cgm)
