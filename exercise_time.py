def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    total_segundos = 3665
    total_minutos = total_segundos/60
    total_minutos_completos = int(total_minutos)
    total_horas = total_minutos_completos/60
    total_horas_completas = int(total_horas)
    print(total_horas_completas)
    print(total_minutos_completos-total_horas)
    print(total_segundos-total_horas)
