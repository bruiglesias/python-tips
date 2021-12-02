import threading

class Contador():

    def __init__(self, nthreads, maxcont):
        # todas as thread tentaram alterar self._count
        self._count = 0
        self._maxCount = maxcont
        self._threadPool = []
        self._ntreads = nthreads
        self._lock = threading.Lock()
    
    def incremento(self):

        n = 0
        
        # inicio da seção critica  
        self._lock.acquire()

        while n < self._maxCount:
            self._count += 1
            n += 1

        # fim da seção critica
        self._lock.release()
          
    def run(self):
        
        for thread in range(0, self._ntreads):
            self._threadPool.append(threading.Thread(target=self.incremento))
            self._threadPool[thread].start()

        for thread in self._threadPool:
            thread.join()

        # Sem proteger self._count com um lock --> Resultado obtido: 3205243 | Resultado esperado: 5000000
        print(f"Resultado obtido: {self._count} | Resultado esperado: {self._ntreads * self._maxCount}")
    