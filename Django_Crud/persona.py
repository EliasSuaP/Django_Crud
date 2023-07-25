###### Super Clase ######
class Persona():
    ###### Funcion inicializadora ######
    def __init__(self, nombre:str, edad:int, saldo:int) -> None:
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo


    ###### sobrecarga de método mágico ######
    def __str__(self) -> str:
        return f'Hello, {self.nombre} you have {self.edad} years old and you bank balance is: ${self.saldo}. Good!'
    

    ###### Métodos no estático ######
    def cumpleanos(self):
        self.edad += 1
        return f'Happy birthday to you, you are now {self.edad} years old.'


    def transferencia(self, persona2:object, monto:int)->str:
        if self.saldo >= monto:
            self.saldo -= monto 
            persona2.saldo += monto
            return print(f'successful transfer to {persona2.nombre} your new balance is: ${self.saldo}')
        else:
            print(f'you do not have a sufficient balance: ${self.saldo}')


###### Instancia ######

persona1 = Persona('José', 33, 200000)
persona2 = Persona('Ester', 45, 500000)
persona3 = Persona('Héctor', 60, 1000000)
persona4 = Persona('Belén', 20, 100000)

print(persona1)
persona1.transferencia(persona2, 10000)

print(persona3)
persona3.transferencia(persona4, 200000)