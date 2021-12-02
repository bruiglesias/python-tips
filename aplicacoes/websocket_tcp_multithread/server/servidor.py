import socket
import threading


class Servidor():

    """
        Classe servidor - Calculadora Remota - API Socket
    """

    def __init__(self, host, port):
        """
            Construtor da classe servidor
        """
        self._host = host
        self._port = port
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._bufferSize = 1024

    def _service(self, con, client):
        """
            Método implementa o serviço de calculadora
            :param con: objeto socket utilizado para enviar e receber dados
            :param client: endereço e porta do cliente
        """
        print("Atendendo cliente ", client)
        operadores = ['+', '-', '*', '/']
        
        while True:
            try:
                msg = con.recv(self._bufferSize)
                msg_s = str(msg.decode('ascii')) # ex: 15+10
                op = ""

                for x in operadores:
                    if msg_s.find(x) > 0:
                        op = x # ex: +
                        msg_s = msg_s.split(op) # ex: ['15', '10']
                        break
                    
                if op == '+':
                    resp = float(msg_s[0]) + float(msg_s[1])
                elif op == '-':
                    resp = float(msg_s[0]) + float(msg_s[1])
                elif op == '*':
                    resp = float(msg_s[0]) + float(msg_s[1])
                elif op == '/':
                    resp = float(msg_s[0]) + float(msg_s[1])
                else:
                    resp = "Operacao invalida"

                con.send(bytes(str(resp), 'ascii'))
                print(client, ' --> requisição atendida')
            
            except OSError as e:
                print("Conexão encerrada ", client )
                return
            except Exception as e:
                print("Erro nos dados ", client, " : ", e.args)
                con.send(bytes("Erro", "ascii"))
    


    def start(self):
        """
            Inicia a execução do serviço
        """

        endpoint = (self._host, self._port)

        try:
            self._tcp.bind(endpoint)
            self._tcp.listen(1)
            print("Servidor foi iniciado em ", self._host, ":", self._port)

            while True:
                con, client = self._tcp.accept()
                self.__tre
                self._service(con, client)
        except Exception as e:
            print("Erro ao inicializar o servidor ", e.args)
        

class ServidorMT(Servidor):
    """
        Classe Servidor MT - Calculadora remota - Multithreading
    """

    def __init__(self, host, port):
        """
            Construtor da classse Servidor MT
        """
        super().__init__(host, port)
        self.__threadPool = {}

    def start(self):
        """
            Inicia a execução do serviço
        """

        endpoint = (self._host, self._port)

        try:
            self._tcp.bind(endpoint)
            self._tcp.listen(1)
            print("Servidor foi iniciado em ", self._host, ":", self._port)

            while True:
                con, client = self._tcp.accept()
                self.__threadPool[client] = threading.Thread(target=self._service, args=(con, client))
                self.__threadPool[client].start() 
                
        except Exception as e:
            print("Erro ao inicializar o servidor ", e.args)


