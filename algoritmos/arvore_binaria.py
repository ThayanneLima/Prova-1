class Node: # Nó da árvore binária
    def __init__(self, key):
        # Inicializa um novo nó da árvore com uma chave dada
        self.key = key
        self.left = None  # Filho esquerdo do nó
        self.right = None  # Filho direito do nó
        self.head = None  # Referência opcional para o pai do nó

    def insert(self, value):
        # Insere um novo valor na árvore de forma iterativa
        current = self
        while True:
            if value < current.key:
                # Se o valor for menor que a chave atual, vá para o filho esquerdo
                if current.left is None:
                    # Se o filho esquerdo for None, insere o novo valor aqui
                    current.left = Node(value)
                    break
                else:
                    # Caso contrário, continue no filho esquerdo
                    current = current.left
            else:
                # Se o valor for maior ou igual à chave atual, vá para o filho direito
                if current.right is None:
                    # Se o filho direito for None, insere o novo valor aqui
                    current.right = Node(value)
                    break
                else:
                    # Caso contrário, continue no filho direito
                    current = current.right

    def find_deepest_node(self):
        # Encontra o nó mais profundo na árvore
        if self is None:
            return None, 0
        
        queue = [(self, 0)]  # Fila para BFS contendo tuplas de (nó, profundidade)
        deepest_node = None
        max_height = 0

        while queue:
            node, height = queue.pop(0)  # Dequeue
            
            if height > max_height:
                max_height = height  # Atualiza a altura máxima
                deepest_node = node  # Atualiza o nó mais profundo

            if node.left:
                queue.append((node.left, height + 1))  # Enqueue filho esquerdo com profundidade incrementada
                
            if node.right:
                queue.append((node.right, height + 1))  # Enqueue filho direito com profundidade incrementada

        return [deepest_node, max_height]

    def inorder_traversal(self):
        # Percorre a árvore em ordem (esquerda, raiz, direita)
        stack = []
        current = self
        while True:
            if current is not None:
                stack.append(current)  # Vai para o filho esquerdo
                current = current.left
            elif stack:
                current = stack.pop()  # Visita o nó
                print(current.key)
                current = current.right  # Vai para o filho direito
            else:
                break

    def preorder_traversal(self):
        # Percorre a árvore em pré-ordem (raiz, esquerda, direita)
        stack = [self]
        while stack:
            current = stack.pop()
            print(current.key)
            if current.right:
                stack.append(current.right)  # Enqueue filho direito
            if current.left:
                stack.append(current.left)  # Enqueue filho esquerdo

    def postorder_traversal(self):
        # Percorre a árvore em pós-ordem (esquerda, direita, raiz)
        stack1 = [self]
        stack2 = []
        while stack1:
            current = stack1.pop()
            stack2.append(current)
            if current.left:
                stack1.append(current.left)  # Enqueue filho esquerdo
            if current.right:
                stack1.append(current.right)  # Enqueue filho direito
        while stack2:
            print(stack2.pop().key)

    def find(self, value, comparison_count=0):
        # Encontra um valor na árvore e conta o número de comparações
        current = self
        while current:
            comparison_count += 1
            if value < current.key:
                current = current.left  # Vai para o filho esquerdo se o valor for menor
            elif value > current.key:
                current = current.right  # Vai para o filho direito se o valor for maior
            else:
                return current.key, comparison_count  # Valor encontrado
        return None, comparison_count  # Valor não encontrado
