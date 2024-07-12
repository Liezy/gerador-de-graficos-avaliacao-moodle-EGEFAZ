# Gerador de Gráficos

## Descrição
Se trata de um programa Python que facilita a análise de feedbacks de cursos através da geração automática de gráficos e relatórios a partir das respostas coletadas.

## Funcionalidades
- Coleta dinâmica de respostas para diversas perguntas de avaliação de cursos.
- Cálculo automático de porcentagens de respostas SIM, PARCIALMENTE e NÃO.
- Geração de gráficos de pizza para cada critério de avaliação.
- Salvamento dos resultados em arquivos de texto e gráficos para fácil referência.

## Como usar
1 **Bibliotecas:**
   - Matplotlib: Para criação de gráficos.
   - Datetime: Para manipulação de datas e horas.
   - OS: Para manipulação de arquivos e diretórios no sistema operacional.

2. **Execução do Programa:**
   - Execute o programa digitando o seguinte comando no terminal:
     ```bash
     python graficospesquisa.py
     ```
   - Siga as instruções para inserir o nome do curso e as respostas para cada pergunta.

3. **Resultados Gerados:**
   - Os gráficos de pizza e os relatórios em texto serão salvos automaticamente na pasta `resultados`.
   - Cada gráfico corresponde a um critério específico de avaliação do curso.

## Exemplo de Estrutura de Diretórios
```
Programa/
│
├── programa.py # Código fonte principal
├── resultados/ # Diretório de resultados
│ ├── graficos/ # Gráficos de pizza gerados
  └── respostas/ # Relatórios em texto das respostas
```
## Autor
- Eliézer Alencar
