import random
import string

perguntas = [
    {"pergunta": "Qual é a principal função de um sistema operacional?",
     "opcoes": ["Gerenciar hardware e software", "Executar planilhas", "Editar imagens", "Navegar na internet"],
     "resposta": "Gerenciar hardware e software"},
    {"pergunta": "Qual desses NÃO é um sistema operacional?",
     "opcoes": ["Linux", "Windows", "Android", "Oracle"],
     "resposta": "Oracle"},
    {"pergunta": "O que significa a sigla 'GUI'?",
     "opcoes": ["Graphical User Interface", "General User Instruction", "Global Utility Interaction", "General Unit Interface"],
     "resposta": "Graphical User Interface"},
    {"pergunta": "Qual sistema operacional é baseado em código aberto?",
     "opcoes": ["Linux", "Windows", "macOS", "iOS"],
     "resposta": "Linux"},
    {"pergunta": "O Windows utiliza qual sistema de arquivos por padrão?",
     "opcoes": ["NTFS", "EXT4", "FAT16", "XFS"],
     "resposta": "NTFS"},
    {"pergunta": "Qual comando do Linux é usado para listar arquivos em um diretório?",
     "opcoes": ["ls", "dir", "list", "show"],
     "resposta": "ls"},
    {"pergunta": "Qual desses sistemas é utilizado em smartphones?",
     "opcoes": ["Android", "Debian", "Ubuntu Server", "FreeBSD"],
     "resposta": "Android"},
    {"pergunta": "Qual parte do sistema operacional é responsável pela comunicação com o hardware?",
     "opcoes": ["Kernel", "Shell", "Aplicativo", "Driver"],
     "resposta": "Kernel"},
    {"pergunta": "Em sistemas multitarefa, o que o SO faz?",
     "opcoes": ["Gerencia a execução de múltiplos processos", "Executa apenas um processo por vez", "Impede paralelismo", "Desativa a memória virtual"],
     "resposta": "Gerencia a execução de múltiplos processos"},
    {"pergunta": "Qual comando no Windows mostra os processos em execução?",
     "opcoes": ["tasklist", "ps", "ls", "jobs"],
     "resposta": "tasklist"},
]

random.shuffle(perguntas)
acertos = 0

for i, q in enumerate(perguntas, 1):
    print(f"\nPergunta {i}: {q['pergunta']}")
    opcoes = q['opcoes'][:]
    random.shuffle(opcoes)

    letras = list(string.ascii_uppercase)[:len(opcoes)]
    mapa = dict(zip(letras, opcoes))

    for letra, opcao in mapa.items():
        print(f"  {letra}) {opcao}")

    while True:
        escolha = input("Sua resposta (letra): ").strip().upper()
        if escolha in mapa:
            break

    if mapa[escolha] == q['resposta']:
        acertos += 1

print("\n=== RESULTADO ===")
print(f"Acertos: {acertos}")
