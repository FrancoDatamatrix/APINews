from datetime import datetime

class SecondConverter:
    @staticmethod
    def converter(hora):
    
        # Separar las horas y los minutos
        horas, minutos = hora.split(":")

        # Convertir las horas y los minutos a enteros
        horas = int(horas)
        minutos = int(minutos)
        
        # Verificar si las horas y minutos son ambos 0
        if horas == 0 and minutos == 0:
            segundos_totales = 0
        else:
        # realizar la conversión
            segundos_totales = (horas * 3600) + (minutos * 60)
    
        return segundos_totales