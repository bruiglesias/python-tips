from pyModbusTCP.server import DataBank, ModbusServer
import random
import time
class ServidorMODBUS():
    
    """
    Classe servidor modbus
    """

    def __init__(self, host_ip, port):
        self._server = ModbusServer(host = host_ip, port = port, no_block=True)
        self._db = DataBank


    def run(self):
     
        self._server.start()
        print("Servidor modbus em execução")
        while True:
            self._db.set_words(1000, [random.randrange(int(0.95 * 400), int(1.05 * 400))])
            print("==============================================")
            print("Tabela modbus")
            print(f"Holding Register \r\n R1000 {self._db.get_words(1000)} \r\n R2000 {self._db.get_words(2000)}")
            print(f"Coil \r\n R1000 {self._db.get_bits(1000)} \r\n")
            time.sleep(1)
        