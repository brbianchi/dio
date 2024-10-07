'''
Descrição
    Neste desafio, você precisa processar uma lista de datas fornecida pelo usuário para extrair o ano de cada uma delas. A extração de anos pode ser útil para diversas aplicações, como a realização de análises anuais em grandes volumes de dados temporais.

Passo a Passo:
    Entrada de Dados: O usuário fornecerá uma sequência de datas no formato "YYYY-MM-DD", onde "YYYY" representa o ano, "MM" o mês, e "DD" o dia. Todas as datas serão fornecidas em uma única linha, separadas por vírgula e espaço. Por exemplo: "2024-01-15, 2023-11-22, 2024-05-10".
    Processamento dos Dados: O objetivo é isolar a parte correspondente ao ano de cada data. Isso pode ser feito dividindo cada string de data pelo caractere - e selecionando a primeira parte, que corresponde ao ano.
    Formatação da Saída: Após extrair os anos, você deve retorná-los como uma nova lista, onde os anos estão separados por vírgulas. É importante manter a ordem original das datas fornecidas pelo usuário.

Entrada
    Uma lista de datas no formato "YYYY-MM-DD" separados por vírgula.
Saída
    Uma lista com os anos extraídos.
Exemplos
    Entrada 	                                    Saída
    2024-01-01, 2023-07-19                       	2024, 2023
    2022-12-31, 2021-01-01, 2020-05-25 	            2022, 2021, 2020
    2025-09-09, 2025-10-10, 2026-03-03, 2027-07-07  2025, 2025, 2026, 2027
'''

def extrair_anos(datas):
    # Divide a string de datas em uma lista
    lista_datas = datas.split(", ")
    # TODO: Extraia o ano de cada data e cria uma nova lista com os anos
    anos = [item[0:4] for item in lista_datas]

    # Junta os anos em uma string separada por vírgula e retorna
    return ", ".join(anos)


entrada = input()

# TODO: Chame a função para imprimir o resultado:
saida = extrair_anos(entrada)

print(saida)