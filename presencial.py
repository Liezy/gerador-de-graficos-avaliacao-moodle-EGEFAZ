import os
import datetime
import matplotlib.pyplot as plt

# Função para calcular as porcentagens e gerar os gráficos
def calcular_porcentagens(nome_curso):
    # Critérios e suas respectivas perguntas
    criterios = {
        "Quanto ao Conteúdo": [
            "O programa do curso foi cumprido?",
            "O material didático fornecido foi satisfatório quanto à qualidade?",
            "Os recursos audiovisuais, caso tenham sido utilizados, foram satisfatórios quanto à quantidade e à qualidade?"
        ],
        "Quanto ao Instrutor": [
            "Demonstrou completo domínio do conteúdo da disciplina?",
            "Abordou adequadamente os assuntos do programa?",
            "Criou clima favorável à participação dos alunos?",
            "Foi objetivo em suas explicações?",
            "Empregou técnicas didáticas favoráveis à fixação da matéria?",
            "Esclareceu dúvidas dos alunos?",
            "Cumpriu os horários estabelecidos?"
        ],
        "Quanto ao Espaço Físico e Organização do Evento": [
            "As instalações foram adequadas (salas de aulas, banheiros, restaurante, etc.)?",
            "O processo de comunicação da inscrição foi satisfatório?",
            "O atendimento feito pela Egefaz foi satisfatório?",
            "A carga horária foi satisfatória?"
        ],
        "Quanto ao Desempenho do Discente (Autoavaliação)": [
            "Sinto-me seguro quanto à assimilação do conteúdo?",
            "Cumpri os compromissos de trabalho?",
            "Participei da aula?",
            "Interagi com os colegas?"
        ],
        "Avaliação Geral do Curso": [
            "Marque com X uma nota de 1 a 10 para avaliar o curso:"
        ]
    }

    # Inicialização das contagens
    respostas_por_pergunta = {criterio: {pergunta: [0] * (10 if pergunta == "Marque com X uma nota de 1 a 10 para avaliar o curso:" else 5) for pergunta in perguntas} for criterio, perguntas in criterios.items()}

    # Coleta das respostas dos alunos
    for criterio, perguntas in criterios.items():
        print(f"\nCritério: {criterio}")
        for pergunta in perguntas:
            numero_opcoes = 10 if pergunta == "Marque com X uma nota de 1 a 10 para avaliar o curso:" else 5
            for i in range(1, numero_opcoes + 1):
                resposta = input(f"Quantos alunos deram nota {i} para '{pergunta}'? ")
                if resposta.isdigit():
                    respostas_por_pergunta[criterio][pergunta][i-1] = int(resposta)
                else:
                    print("Entrada inválida. Por favor, digite um número inteiro.")

    # Gerar nome do arquivo
    data_hora = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo_txt = f"resultados/respostas/{nome_curso}_{data_hora}.txt"
    nome_arquivo_grafico_geral = f"resultados/graficos/{nome_curso}_{data_hora}_geral.png"
    
    # Criação das pastas de resultados se não existirem
    os.makedirs("resultados/respostas", exist_ok=True)
    os.makedirs("resultados/graficos", exist_ok=True)

    # Calcular e salvar as porcentagens de notas para cada pergunta
    with open(nome_arquivo_txt, 'w') as arquivo:
        arquivo.write(f"Data e Hora da Avaliação: {data_hora}\n\n")
        arquivo.write(f"Respostas Detalhadas:\n")
        for criterio, perguntas in respostas_por_pergunta.items():
            arquivo.write(f"{criterio}:\n")
            for pergunta, respostas in perguntas.items():
                arquivo.write(f"   {pergunta}:\n")
                for i in range(1, len(respostas) + 1):
                    arquivo.write(f"      Nota {i}: {respostas[i-1]}\n")

    # Gerar gráfico de pizza para a avaliação geral do curso
    notas_avaliacao_geral = respostas_por_pergunta["Avaliação Geral do Curso"]["Marque com X uma nota de 1 a 10 para avaliar o curso:"]
    labels = [f"Nota {i+1}" for i in range(10)]

    plt.figure(figsize=(10, 6))
    plt.pie(notas_avaliacao_geral, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f"Avaliação Geral do Curso: {nome_curso}")
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Salvar gráfico de pizza
    plt.savefig(nome_arquivo_grafico_geral)
    plt.show()
    
    # Gerar gráficos de pizza por critério com a média das porcentagens das respostas de suas perguntas
    for criterio, perguntas in respostas_por_pergunta.items():
        if criterio != "Avaliação Geral do Curso":
            total_respostas_criterio = [0] * 5
            num_perguntas = len(perguntas)
            for pergunta, respostas in perguntas.items():
                for i in range(len(respostas)):
                    total_respostas_criterio[i] += respostas[i]
            media_respostas_criterio = [resposta / num_perguntas for resposta in total_respostas_criterio]

            plt.figure(figsize=(10, 6))
            labels = [f"Nota {i+1}" for i in range(5)]
            plt.pie(media_respostas_criterio, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.title(f"Média das Respostas por Critério: {criterio}")
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            # Substituir caracteres especiais por sublinhados nos nomes dos arquivos
            nome_arquivo_grafico_criterio = f"resultados/graficos/{nome_curso}_{data_hora}_{criterio.replace(' ', '_').replace('?', '').replace(':', '').replace('/', '_')}_media.png"
            plt.savefig(nome_arquivo_grafico_criterio)
            plt.show()

    # Exibir mensagem de sucesso
    print(f"\nResultados salvos em:\n- {nome_arquivo_txt}\n- {nome_arquivo_grafico_geral}")
    for criterio, perguntas in respostas_por_pergunta.items():
        if criterio != "Avaliação Geral do Curso":
            nome_arquivo_grafico_criterio = f"resultados/graficos/{nome_curso}_{data_hora}_{criterio.replace(' ', '_').replace('?', '').replace(':', '').replace('/', '_')}_media.png"
            print(f"- {nome_arquivo_grafico_criterio}")

# Exemplo de uso do programa
if __name__ == "__main__":
    nome_curso = input("Digite o nome do curso: ")
    calcular_porcentagens(nome_curso)
