rm = input("Infome seu RM:")
idade = input("Informe sua idade: ")
if int (idade) >= 18:
    print(f"Sua participação foi autorizada, aluno de RM {rm}")
    print("Mais informações serão enviadas para seu e-mail cadastrado? ")
else:
    print("Sua participação não foi autorizada por causa da idade")