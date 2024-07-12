import matplotlib.pyplot as plt
from datetime import datetime
import os

def calcular_porcentagens(nome_curso):
    # Perguntas e alternativas
    perguntas = [
        "Você considera o conteúdo abordado na capacitação relevante?",
        "O conteúdo estava apropriado para participantes com seu nível de experiência?",
        "Considerando suas responsabilidades atuais e/ou futuras, as informações foram valiosas para você?",
        "O material didático utilizado facilitou seu aprendizado?",
        "A metodologia utilizada foi adequada para a fixação do conteúdo?",
        "Você ficou satisfeito de um modo geral com o curso?",
        "A infraestrutura utilizada foi adequada na plataforma EAD?",
        "O conteúdo foi transmitido de forma clara e objetiva?",
        "Foi evidenciado domínio técnico do assunto pelo(s) instrutor(es)?",
        "Os recursos audiovisuais utilizados foram satisfatórios quanto à qualidade?",
        "A plataforma EAD apresentou praticidade de navegação e acesso a informações?",
        "Você adquiriu novos conhecimentos?",
        "Como você avalia a carga horária atribuída à capacitação?"
    ]
    
    # Definindo os critérios e suas respectivas perguntas
    criterios = {
        "Quanto à Metodologia, Conteúdo e Material Didático": perguntas[:9],
        "Quanto ao Ambiente de Aprendizado": perguntas[9:11],
        "Autoavaliação": [perguntas[11]],
        "Carga Horária": [perguntas[12]]
    }

    # Listas para armazenar as respostas de cada critério
    respostas_crit = {crit: [] for crit in criterios}

    # Leitura dinâmica das respostas
    for crit, perguntas in criterios.items():
        print(f"Critério: {crit}")
        respostas_crit[crit] = []
        for i, pergunta in enumerate(perguntas):
            print(f"Pergunta {i + 1}: {pergunta}")
            resposta_sim = int(input("Quantas respostas SIM? "))
            resposta_parcialmente = int(input("Quantas respostas PARCIALMENTE? "))
            resposta_nao = int(input("Quantas respostas NÃO? "))
            respostas_crit[crit].append([resposta_sim, resposta_parcialmente, resposta_nao])
            print()

    # Configuração dos gráficos de pizza para cada critério
    for crit, respostas in respostas_crit.items():
        sim = [r[0] for r in respostas]
        parcialmente = [r[1] for r in respostas]
        nao = [r[2] for r in respostas]

        # Calculando porcentagens
        total_respostas = sum(sim) + sum(parcialmente) + sum(nao)
        porcentagem_sim = [100 * s / total_respostas for s in sim]
        porcentagem_parcialmente = [100 * p / total_respostas for p in parcialmente]
        porcentagem_nao = [100 * n / total_respostas for n in nao]

        # Configuração do gráfico de pizza
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis('equal')  # Garantindo que o gráfico de pizza seja circular

        # Cores para cada categoria
        cores = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Adicionar mais cores se necessário

        # Plotando o gráfico de pizza
        explode = (0.1, 0, 0)  # Explodir a primeira fatia (opcional)
        total_por_pergunta = [sum(sim), sum(parcialmente), sum(nao)]
        wedges, texts, autotexts = ax.pie(total_por_pergunta, explode=explode, labels=['Sim', 'Parcialmente', 'Não'], colors=cores,
                                          autopct='%1.1f%%', shadow=True, startangle=140, wedgeprops={'edgecolor': 'black'})

        # Estilizando os textos dentro das fatias
        for text, autotext in zip(texts, autotexts):
            text.set_fontsize(10)
            autotext.set_fontsize(10)
            autotext.set_color('white')

        ax.set_title(f'Porcentagens de aceitação para o critério: {crit}', pad=20)  # Título do gráfico

        # Criando os diretórios se não existirem
        resultados_dir = 'resultados'
        respostas_dir = os.path.join(resultados_dir, 'respostas')
        graficos_dir = os.path.join(resultados_dir, 'graficos')
        os.makedirs(respostas_dir, exist_ok=True)
        os.makedirs(graficos_dir, exist_ok=True)

        # Salvando o gráfico em arquivo
        data_hora = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        nome_arquivo_grafico = f'{nome_curso}_{crit.replace(" ", "_")}_resultados_{data_hora}.png'
        caminho_arquivo_grafico = os.path.join(graficos_dir, nome_arquivo_grafico)
        plt.savefig(caminho_arquivo_grafico)

        # Registrando os resultados em um arquivo de texto específico para cada critério
        nome_arquivo_txt = f'{nome_curso}_{crit.replace(" ", "_")}_resultados_{data_hora}.txt'
        caminho_arquivo_txt = os.path.join(respostas_dir, nome_arquivo_txt)
        with open(caminho_arquivo_txt, 'a') as arquivo:
            arquivo.write(f'Resultados gerados em {data_hora} para o critério "{crit}":\n')
            for i, pergunta in enumerate(criterios[crit]):
                arquivo.write(f'{pergunta}\n')
                arquivo.write(f'SIM: {sim[i]} ({porcentagem_sim[i]:.1f}%)\n')
                arquivo.write(f'PARCIALMENTE: {parcialmente[i]} ({porcentagem_parcialmente[i]:.1f}%)\n')
                arquivo.write(f'NÃO: {nao[i]} ({porcentagem_nao[i]:.1f}%)\n\n')

        # Exibindo o gráfico
        plt.show()

# Solicitando o nome do curso ao usuário
nome_curso = input("Digite o nome do curso: ")

# Chamada da função principal com o nome do curso
calcular_porcentagens(nome_curso)
