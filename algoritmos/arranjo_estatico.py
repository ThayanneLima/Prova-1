class ArranjoEstatico:
    def __init__(self, tamanho):
        # Inicializa um arranjo com 'tamanho' elementos, todos inicialmente como None
        self.arranjo = [None] * tamanho
        self.tamanho = tamanho
        self.comparacoes_totais = 0  # Adicionando atributo para contar comparações

    def inserir(self, valor, posicao):
        # Insere 'valor' na posição 'posicao' do arranjo, se 'posicao' for válida
        if posicao < 0 or posicao >= self.tamanho:
            print("Posição inválida!")  # Imprime uma mensagem de erro se a posição for inválida
            return
        self.arranjo[posicao] = valor  # Insere o valor na posição especificada

    def buscar_sequencial(self, valor):
        self.comparacoes_totais = 0  # Zerando o contador de comparações
        for i in range(self.tamanho):  # Loop para percorrer todo o arranjo
            self.comparacoes_totais += 1  # Incrementa o contador de comparações
            if self.arranjo[i] == valor:  # Verifica se o valor atual é igual ao valor buscado
                return i  # Retorna a posição do valor se encontrado
        return -1  # Retorna -1 se o valor não for encontrado

    def buscar_binaria(self, valor):
        self.comparacoes_totais = 0  # Zerando o contador de comparações
        inicio = 0
        fim = self.tamanho - 1

        while inicio <= fim:  # Loop enquanto a parte do arranjo a ser buscada não estiver vazia
            self.comparacoes_totais += 1  # Incrementa o contador de comparações
            meio = (inicio + fim) // 2  # Calcula o índice do elemento do meio
            if self.arranjo[meio] == valor:  # Verifica se o valor do meio é igual ao valor buscado
                return meio  # Retorna a posição do valor se encontrado
            elif self.arranjo[meio] < valor:  # Se o valor do meio for menor, busca na parte direita
                inicio = meio + 1
            else:  # Se o valor do meio for maior, busca na parte esquerda
                fim = meio - 1

        return -1  # Retorna -1 se o valor não for encontrado
