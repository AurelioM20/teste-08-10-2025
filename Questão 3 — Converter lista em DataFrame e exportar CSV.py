import pandas as pd

def criar_pessoa(nome, idade, id):
    return {'nome': nome, 'idade': idade, 'id': id}

def adicionar_gostos(pessoas: list, gostos: list):
    mapa_gostos = {g['id']: g['gostos'] for g in gostos}
    resultado = []
    for pessoa in pessoas[:5]:
        pessoa_com_gostos = pessoa.copy()
        pessoa_com_gostos['gostos'] = mapa_gostos.get(pessoa['id'], [])
        resultado.append(pessoa_com_gostos)
    return resultado

def exportar_csv(pessoas: list, nome_arquivo: str):
    df = pd.DataFrame(pessoas)
    df.to_csv(nome_arquivo, index=False)
    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

# Dados de exemplo
pessoas = [
    criar_pessoa("Marcos", 28, 1),
    criar_pessoa("Ana", 24, 2),
    criar_pessoa("Carlos", 30, 3),
    criar_pessoa("Julia", 22, 4),
    criar_pessoa("Pedro", 27, 5),
    criar_pessoa("Laura", 26, 6)
]

gostos = [
    {"id": 1, "gostos": ["Música", "Futebol"]},
    {"id": 2, "gostos": ["Leitura", "Cinema"]},
    {"id": 3, "gostos": ["Viagem"]},
    {"id": 4, "gostos": ["Dança", "Esportes"]},
    {"id": 5, "gostos": ["Tecnologia", "Culinária"]},
    {"id": 6, "gostos": ["Moda"]}
]

resultado = adicionar_gostos(pessoas, gostos)

# Mostra as pessoas com gostos, pulando linhas para melhor organização
for pessoa in resultado:
    print(pessoa)
    print()

exportar_csv(resultado, "pessoas.csv")
