class Cuentahabiente:
    def __init__(self, nombre, rfc, direccion, saldo_inicial):
        self.__nombre = nombre
        self.__rfc = rfc
        self.__direccion = direccion
        self.__saldo_inicial = saldo_inicial
        self.__movimientos = []
        self.__movimientos.append(f'Deposito - ${saldo_inicial:0.2f}\n')
        
    def __str__(self):
        return f'{self.__nombre} ({self.__rfc}): ${self.__saldo_inicial:0.2f}\n'
    
    def hacer_deposito(self, cantidad):
        self.__saldo_inicial = self.__saldo_inicial + cantidad
        if len(self.__movimientos) == 5:
            del self.__movimientos[0]
            self.__movimientos.append(f'Deposito - ${cantidad:0.2f}\n')
        else:
            self.__movimientos.append(f'Deposito - ${cantidad:0.2f}\n') 
      
    def hacer_retiro(self, cantidad):
        if cantidad > self.__saldo_inicial:
            return False
        else:
            self.__saldo_inicial -= cantidad
            if len(self.__movimientos) == 5:
                del self.__movimientos[0]
                qty = f'- ${-cantidad:0.2f}'
                self.__movimientos.append(f'Retiro {qty:13}\n')
            else:
                qty = f'- ${-cantidad:0.2f}'
                self.__movimientos.append(f'Retiro{qty:13}\n')
                return True
          
    def hacer_transferencia(self, cantidad, destinatario):
        if cantidad > self.__saldo_inicial:
            return False
        else:
            destinatario.__saldo_inicial += cantidad
            self.__saldo_inicial -= cantidad
            if len(self.__movimientos) == 5:
                del self.__movimientos[0]
                self.__movimientos.append(f'Transferencia - ${-cantidad:0.2f}\n')
                destinatario.__movimientos.append(f'Transferencia - ${cantidad:0.2f}\n')
            else:
                self.__movimientos.append(f'Transferencia - ${-cantidad:0.2f}\n')
                destinatario.__movimientos.append(f'Transferencia - ${cantidad:0.2f}\n')
              
            return True
            
    @property
    def consultar_saldo(self):
        return self.__saldo_inicial
    
    def ver_movimientos(self):
        mov_print= ''
        for movimiento in self.__movimientos:
            mov_print += movimiento
        return mov_print


if __name__ == '__main__':
    c1 = Cuentahabiente('Rico McPato', 'RCMCPT01C', 'Duckburg', 0.10)
    c2 = Cuentahabiente('Bruce Wayne', 'DC2739', 'Gotham', 1000000)
    for g in range(10, 1000000, 1000):
        c1.hacer_deposito(g)
    c1.hacer_retiro(5000)
    c1.hacer_transferencia(25000, c2)
    print(c1)
    print(c1.ver_movimientos())
    print(c2)
    print(c2.ver_movimientos())


    
  
  
