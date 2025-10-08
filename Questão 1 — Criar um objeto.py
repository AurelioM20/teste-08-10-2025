def criar_pessoa(nome, idade, id):
    pessoa = {'nome': nome , 'idade': idade , "id": id}
    return pessoa
a1 = criar_pessoa("Aurelio", 19, 1)
a2 = criar_pessoa("Neymar", 30, 2)
a3 = criar_pessoa("Erick", 13, 3)
a4 = criar_pessoa("Brian", 22, 4)
a5 = criar_pessoa("Tonho", 20, 5)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
