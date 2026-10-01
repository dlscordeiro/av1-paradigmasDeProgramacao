
#Atividade avaliatva P1 - Paradgmas de programação
#Nomes: Dorivan Cunha de Morais, David Lucas Sá Cordeiro

def cadastrar(alunos):
    chamada = int(input("\nNumero da chamada: "))
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    aluno = [chamada, nome, nota]
    alunos.append(aluno)

    print("Aluno cadastrado!")

def media(turma): 
    return sum(a['nota'] for a in turma) / len(turma) if turma else 0

def status(nota): 
    return "Aprovado" if nota >= 6 else "Reprovado"

turma = []
while True:
    op = input("\n1. Cadastrar | 2. Listar | 3. Sair\nOpcao: ")
    
    if op == '1':
        turma.append({
            'id': int(input("Chamada: ")),
            'nome': input("Nome: "),
            'nota': float(input("Nota: "))
        })

    elif op == '2' and turma:
        for a in turma:
            print(f"ID: {a['id']} | {a['nome']} | {a['nota']} | {status(a['nota'])}")
        print(f"Media: {media(turma):.1f} | Maior: {max(a['n']['nota'] for a in turma):.1f}" if False else 
              f"Media: {media(turma):.1f} | Maior: {max(a['nota'] for a in turma):.1f} | Menor: {min(a['nota'] for a in turma):.1f}")
    elif op == '3':
        break    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
    