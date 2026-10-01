# av1-paradigmasDeProgramacao
Nomes:
- David Lucas Sá Cordeiro
- Dorivan Cunha de Morais

Sistema de Gerenciamento de Alunos
Documentação resumida das funções e linhas do código
Linhas 1-3 — media
Calcula a média das notas de todos os alunos cadastrados.
Retorna 0 se a turma estiver vazia para evitar erros.

Linhas 5-6 — status
Avalia a nota e retorna:
"Aprovado" — se a nota for maior ou igual a 6.
"Reprovado" — se a nota for menor que 6.

Linha 8 — turma = []
Inicializa a lista vazia que armazena os dados dos alunos em memória.

Linhas 10-39 — while True
Controla o menu iterativo principal do sistema.

Linhas 13-19 — Opção 1
Cadastra novos alunos, solicitando:
ID
Nome
Nota
Os dados são inseridos em um dicionário dentro da lista turma.

Linhas 21-34 — Opção 2
Valida se há cadastros.
Em seguida, lista todos os alunos individualmente com seus respectivos status e exibe as estatísticas gerais
Média
Maior nota
Menor nota
As informações são formatadas para facilitar a visualização.

Linhas 35-37 — Opção 3
Encerra o loop e finaliza o programa.

Linhas 38-39 — Opção inválida

Exibe um aviso caso o usuário digite uma opção fora do menu.
