import socket

class Cliente():

    """
        Classe cliente - Calculadora remota - API Socket
    """

    def __init__(self, server_ip, port):
        
        """
            Construtor da classe cliente
            :param server_ip: ip do servidor
            :param port: porta de serviço
        """

        self.__server_ip = server_ip
        self.__port = port
        self.__udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._bufferSize = 1024

    def __method(self):

        """
            Um método que implemeta as requisições do cliente e IHM
        """

        try:
            msg = "empty"
            while msg != "x":

                msg = input("Digite a operação desejada (x para sair): ")
                if msg == "":
                    continue
                elif msg == "x":
                    break
                else:
                    endpoint = (self.__server_ip, self.__port)
                    self.__udp.sendto(bytes(msg, 'ascii'), endpoint)
                    resp = self.__udp.recvfrom(self._bufferSize)
                    
                    message = resp[0]
                    server = resp[1][0]
                    port = resp[1][1]
                    print(f"Server {server}:{port} says: ")
                    print(" = ", resp[0].decode('ascii'))

            
            self.__udp.close()
            print("Conexão fechada")
        except Exception as e:
            print("Erro ao realizar a comunicação com o servidor: ", e.args)

    def start(self):
        """
            Método que inicializa a execução do cliente
        """

        

        try:
            print("Conexão realizada com sucesso")
            self.__method()
        except Exception as e : 
            print("Erro na conexão com o servidor ", e.args)


