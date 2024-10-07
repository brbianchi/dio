'''
Descrição
    Você tem uma lista de tipos de visuais e precisa processar essa lista para remover duplicatas e normalizar os nomes dos visuais. O objetivo é garantir que cada visual apareça apenas uma vez na lista e que todos os nomes estejam em um formato uniforme.
        Remover Duplicatas: É comum em listas que certos itens apareçam mais de uma vez. Para evitar isso, precisamos garantir que cada tipo de visual apareça apenas uma vez na lista final.
        Normalizar Nomes: Quando os usuários digitam nomes, eles podem usar diferentes formatos de capitalização (maiúsculas e minúsculas). Por exemplo, "gráfico de barras" e "Gráfico de Barras" são essencialmente o mesmo visual, mas escritos de maneiras diferentes. Precisamos padronizar esses nomes para que todos sigam o mesmo formato, facilitando a comparação e a remoção de duplicatas.

    Para normalizar os nomes, vamos usar a capitalização do tipo "Título Capitalizado", onde a primeira letra de cada palavra é maiúscula e as demais letras são minúsculas. Por exemplo, "gráfico de barras" se tornará "Gráfico De Barras".

Entrada
    O usuário irá fornecer uma lista de tipos de visuais como uma única string, onde cada visual é separado por vírgulas. A lista pode conter visuais repetidos ou escritos de maneira inconsistente.

Saída
    Uma lista com visuais únicos e normalizados.

Exemplos
    A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

    Entrada 	                                                                                                        Saída
    Gráfico de Barras, Gráfico de Barras, Tabela, Gráfico de Pizza, gráfico de barras 	                                Gráfico De Barras, Gráfico De Pizza, Tabela
    Gráfico de Linhas, gráfico de linhas, Tabela, tabela, gráfico de Linhas, Tabela Dinâmica 	                        Gráfico De Linhas, Tabela, Tabela Dinâmica
    gráfico de pizza, Gráfico de Pizza, gráfico de pizza, gráfico de colunas, Gráfico de Barras, gráfico de colunas 	Gráfico De Barras, Gráfico De Colunas, Gráfico De Pizza
'''

def filtrar_visuais(lista_visuais):
    # Converter a string de entrada em uma lista
    visuais = lista_visuais.split(", ")
    
    # TODO: Normalize e remova duplicatas usando um conjunto
    lista_final = list(set([item.title() for item in visuais]))

    # TODO: Converta o conjunto de volta para uma lista ordenada:
    lista_final = sorted(lista_final)
    
    # Unir a lista em uma string, separada por vírgulas
    return ", ".join(lista_final)

# Capturar a entrada do usuário
entrada_usuario = input()

# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)