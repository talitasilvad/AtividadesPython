class ConversorHorario:
    def __init__(self, hora24, minuto):
        self.hora24 = hora24
        self.minuto = minuto

    def converter12horas(self):
        if self.hora24 < 0 or self.hora24 > 23 or self.minuto < 0 or self.minuto > 59:
            return "Horário inválido."
        
        if self.hora24 == 0:
            periodo = "AM"
            hora12 = 12  
        elif self.hora24 < 12:
            periodo = "AM"
            hora12 = self.hora24
        elif self.hora24 == 12:
            periodo = "PM"
            hora12 = 12  
        else:
            periodo = "PM"
            hora12 = self.hora24 - 12
        return f"{hora12}:{self.minuto:02d} {periodo}"

    def exibir_mensagem(mensagem):
        print(mensagem)

while True:
    try:
        hora24 = int(input("Digite a hora (formato 24 horas, valor negativo para encerrar): "))
        if hora24 < 0:
            break
        minuto = int(input("Digite os minutos: "))
        conversor = ConversorHorario(hora24, minuto)
        resultado = conversor.converter12horas()
        ConversorHorario.exibir_mensagem(f"Horário convertido: {resultado}")
    
    except ValueError:
        print("Por favor, digite valores inteiros válidos para hora e minutos.")
