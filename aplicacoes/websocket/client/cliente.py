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
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
                    self.__tcp.send(bytes(msg, 'ascii'))
                    resp = self.__tcp.recv(1024)
                    print(" = ", resp.decode('ascii'))

            
            self.__tcp.close()
            print("Conexão fechada")
        except Exception as e:
            print("Erro ao realizar a comunicação com o servidor: ", e.args)

    def start(self):
        """
            Método que inicializa a execução do cliente
        """

        endpoint = (self.__server_ip, self.__port)

        try:
            self.__tcp.connect(endpoint)
            print("Conexão realizada com sucesso")
            self.__method()
        except Exception as e : 
            print("Erro na conexão com o servidor ", e.args)


