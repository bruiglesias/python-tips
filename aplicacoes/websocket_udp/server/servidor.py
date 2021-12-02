import socket

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
        self._bufferSize = 1024
        self._udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def _service(self, mensagem, address):
        """
            Método implementa o serviço de calculadora
            :param con: objeto socket utilizado para enviar e receber dados
            :param client: endereço e porta do cliente
        """
        
        operadores = ['+', '-', '*', '/']
        
     
        try:

            print("Atendendo cliente ", address)
            msg_s = str(mensagem.decode('ascii')) # ex: 15+10
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

            self._udp.sendto(bytes(str(resp), 'ascii'), address)
            print(address, ' --> requisição atendida')
        
        except OSError as e:
            print("Conexão encerrada ", address )
            return
        except Exception as e:
            print("Erro nos dados ", address, " : ", e.args)
            self._udp.send(bytes("Erro", "ascii"))
    


    def start(self):
        """
            Inicia a execução do serviço
        """

        endpoint = (self._host, self._port)

        try:
            self._udp.bind(endpoint)
            print("Servidor foi iniciado em ", self._host, ":", self._port)

            while True:
                bytesAddressPair = self._udp.recvfrom(self._bufferSize)
                mensagem = bytesAddressPair[0]
                address = bytesAddressPair[1]
                self._service(mensagem, address)
        except Exception as e:
            print("Erro ao inicializar o servidor ", e.args)
        


            
        