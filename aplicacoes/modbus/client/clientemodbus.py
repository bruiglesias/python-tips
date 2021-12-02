from pyModbusTCP.client import ModbusClient

import random
import time

class ClienteMODBUS():
    
    def __init__(self, server_ip, porta, scan_time = 1):
        self._cliente = ModbusClient(host=server_ip, port=porta)
        self._scan_time = scan_time

    def lerDado(self, tipo, addr):
        if tipo == 1:
            return self._cliente.read_holding_registers(addr, 1)[0]

        if tipo == 2:
            return self._cliente.read_coils(addr, 1)[0]
        
        if tipo == 3:
            return self._cliente.read_input_registers(addr, 1)[0]
        
        if tipo == 4:
            return self._cliente.read_discrete_inputs(addr, 1)[0]

    def escreveDado(self, tipo, addr,  valor):
        if tipo == 1:
            return self._cliente.write_single_register(addr, valor)

        if tipo == 2:
            return self._cliente.write_single_coil(addr, valor)
    
    def atendimento(self):
        self._cliente.open()

        try:
            atendimento = True
            while atendimento:
                sel = input("Deseja realizar uma leitura, escrita ou configuração? (1- leitura, 2 - escrita, 3 - configuração, 4 - sair) \n")
                if sel == '1':
                    tipo = input("Qual o tipo de dado que deseja ler? (1 - Holding Register, 2 - Coil, 3 - Input Register, 4 - Discrete Input \n")
                    addr = input("Digite o endereço da tabela modbus \n")
                    nvezes = int(input("Digite o numero de vezes que deseja ler: \n"))
                    

                    for i in range(0, nvezes):
                        print(f"Leitura {i + 1}: {self.lerDado(int(tipo), int(addr))}")
                        time.sleep(self._scan_time)
                
                elif sel == '2':
                    tipo = input("Qual o tipo de dado que deseja escrever? (1 - Holding Register, 2 - Coil \n")
                    addr = input("Digite o endereço da tabela modbus \n")
                    valor = input("Escreva o valor que deseja escrever \n")
                    self.escreveDado(int(tipo), int(addr), int(valor))

                elif sel == '3':
                    scant =  input("Digite o tempo de varredura desejado em segundos \n")
                    self._scan_time = float(scant)
                elif sel == '4':
                    self._cliente.close()
                    atendimento = False

                else: print("Seleção inválida \n")



                    
        except Exception:
            pass
