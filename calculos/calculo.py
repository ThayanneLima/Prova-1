import time  # Importa o módulo para trabalhar com tempo
import psutil  # Importa o módulo para obter informações sobre o sistema e processos
import os  # Importa o módulo para interagir com o sistema operacional
import tracemalloc  # Importa o módulo para rastrear alocação de memória

def get_pid():
    pid = os.getpid()  # Obtém o ID do processo atual
    return pid
  
def medir_tempo():
    return time.perf_counter()  # Retorna o tempo atual em segundos

def tempo_total(inicio, fim):
    return fim - inicio  # Calcula o tempo total em segundos

def memoria_inicio():
    process = psutil.Process(get_pid())  # Obtém informações do processo atual
    inicio = process.memory_info().rss  # Obtém o uso de memória atual do processo
    del process  # Libera a memória após obter as informações necessárias
    return inicio  # Retorna o uso de memória no início

def memoria_fim():
    process = psutil.Process(get_pid())  # Obtém informações do processo atual
    fim = process.memory_info().rss  # Obtém o uso de memória atual do processo
    del process  # Libera a memória após obter as informações necessárias
    return fim  # Retorna o uso de memória no fim

def memoria_total_consumida(inicio, fim):
    diferenca = fim - inicio  # Calcula a diferença de uso de memória
    return inicio + diferenca  # Retorna o uso de memória total consumida

def esperar(segundos):
    time.sleep(segundos)  # Espera o número de segundos especificado

class DesvioPadrao:
    def __init__(self):
        pass

    def media(self, data):
        return sum(data) / len(data)  # Calcula a média dos valores em 'data'

    def variancia(self, data):
        mu = self.media(data)  # Calcula a média dos valores em 'data'
        return sum((x - mu) ** 2 for x in data) / len(data)  # Calcula a variância dos valores em 'data'

    def calcular(self, data):
        return self.variancia(data) ** 0.5  # Calcula o desvio padrão dos valores em 'data'
