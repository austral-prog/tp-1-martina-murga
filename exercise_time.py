def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    minutos_completos = total_segundos // 60
    horas_completas = minutos_completos//60
    print(horas_completas)
    print(minutos_completos-(horas_completas*60))
    print(total_segundos-(minutos_completos*60))
