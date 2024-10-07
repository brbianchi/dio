'''
Descrição
    Você está desenvolvendo um sistema para organizar vendas por categorias antes de gerar um relatório. O objetivo é criar uma classe Categoria que gerencie as vendas associadas a uma determinada categoria e calcule o total de vendas dessa categoria.

Tarefas:
    Método adicionar_venda: Na classe Categoria, crie um método chamado adicionar_venda que adiciona um objeto Venda à lista de vendas da categoria.
    Método total_vendas: Na classe Categoria, crie um método chamado total_vendas que calcula e retorna o total das vendas (soma do valor de todas as vendas) para essa categoria.
    Na função main:
        Entrada de Dados:
            Leia o nome das categorias e, para cada categoria, leia as vendas associadas.
            Implementação: Adicione cada venda à categoria correspondente usando o método adicionar_venda.
        Exibição dos Resultados:
        Exiba o total de vendas para cada categoria.
            Implementação: Utilize o método total_vendas para calcular e exibir o total das vendas.

Entrada
    A entrada consiste em:
        Nome da Categoria (string)
        Lista de Vendas (com as colunas Produto, Quantidade, Valor)
    Atenção:
        O valor será o TOTAL GERAL de todos os produtos. Dessa forma:

    Eletrônicos
        - Celular, 5, 1000 - Produto Celular, temos 5 unidade e o valor total é 1000;
        - Fone de Ouvido, 10, 500 - Produto Fone de Ouvido, temos 10 unidades e o valor total é 500;
Saída
    A saída é o total de vendas por categoria.

Exemplos
Entrada 	                Saída
Eletrônicos
Celular, 5, 1000
Fone de Ouvido, 10, 500
Móveis
Mesa, 2, 800
Cadeira, 4, 400          	Vendas em Eletrônicos: 1500.0
                            Vendas em Móveis: 1200.0

Alimentos
Arroz, 10, 200
Feijão, 7, 140
Jardinagem
Planta, 2, 60
Ferramentas, 1, 100 	    Vendas em Alimentos: 340.0
                            Vendas em Jardinagem: 160.0

Livros
Aventuras no Tempo, 1, 80
Mistérios do Oceano, 2, 90
Esportes
Tênis, 7, 210
Bola, 3, 120 	            Vendas em Livros: 170.0
                            Vendas em Esportes: 330.0
'''


class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []


    # TODOS: Implementar o método adicionar_venda para adicionar uma venda à lista de vendas:
    def adicionar_venda(self,venda):
        self.vendas.append(venda)
    

    # TODOS: Implementar o método total_vendas para calcular e retornar o total das vendas
    def total_vendas(self):
        total = 0

        for venda in self.vendas:
            total += venda.valor

        return total


def main():
    categorias = []

    for i in range(2):
        nome_categoria = input()
        categoria = Categoria(nome_categoria)

        for j in range(2): 
            entrada_venda = input()
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            # TODOS: Adicione a venda à categoria usando o método adicionar_venda:
            categoria.adicionar_venda(venda)

        categorias.append(categoria)
    
    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
        # TODOS: Exibir o total de vendas usando o método total_vendas:
        print(f"Vendas em {categoria.nome}: {categoria.total_vendas()}")

if __name__ == "__main__":
    main()