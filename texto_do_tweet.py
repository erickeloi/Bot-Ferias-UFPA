from time import gmtime

# Tempo em UTC:
ano_atual = gmtime()[0]
mes_atual = gmtime()[1]
dia_atual = gmtime()[2]

# Caso a mensagem seja postada entre 21PM - 23:59PM (adaptar para UTC-3):
if 0 <= gmtime().tm_hour <= 2:
    dia_atual -= 1

# Lógica da Mensagem:
tempo_decorrido_em_dias = (mes_atual - 1) * 30 + dia_atual
if ano_atual == 2022:
    tempo_decorrido_em_dias += 365

fim_periodo_2_ufpa_dias = 279

# Periodo 2 UFPA
# dias corridos de 01-01-2021 até 07/10/2021 = 279

# 24/06/2021 a 07/10/2021
# 105 dia(s) = 2° Período Letivo

# 7 dias de férias até o próximo período letivo ( 3° )
# dia 286 ele volta, 14/10/2021

fim_periodo_3_ufpa_dias = 403

# Periodo 3 UFPA
# dias corridos de 01-01-2021 até 08/02/2022 = 403

# 14/10/2021 a 08/02/2022
# 117 dia(s) = 3° Período Letivo

# Passou de 365, pois termina em 2022.


def texto_dos_bacanas():
    periodo = 2

    def texto_padrao_dias(dias_que_faltam, periodo_atual):
        return f"Faltam {dias_que_faltam} dias para as Férias (Término do {periodo_atual}° P.L.)"

    def texto_padrao_dia(periodo_atual):
        return f"Falta 1 dia para as Férias ( Término do {periodo_atual}° P.L.)"

    def texto_glorioso():
        return "Chegou o Glorioso Dia Meus Bacanos!!!"

    try:
        quantos_dias_faltam = fim_periodo_2_ufpa_dias - tempo_decorrido_em_dias

        if quantos_dias_faltam > 1:
            return texto_padrao_dias(quantos_dias_faltam, periodo)

        elif quantos_dias_faltam == 1:
            return texto_padrao_dia(periodo)

        elif quantos_dias_faltam == 0:
            return texto_glorioso()

        # Ele vai passar 7 dias desativado (Férias).
        # E voltar 14/10/2021, começo do 3° Periodo Letivo

        if tempo_decorrido_em_dias >= 286:
            # Correção para corrigir margem de erro das postagens
            tempo_decorrido_em_dias += 2
            #
            quantos_dias_faltam = fim_periodo_3_ufpa_dias - tempo_decorrido_em_dias
            periodo = 3

            if quantos_dias_faltam > 1:
                return texto_padrao_dias(quantos_dias_faltam, periodo)

            elif quantos_dias_faltam == 1:
                return texto_padrao_dia(periodo)

            elif quantos_dias_faltam == 0:
                return texto_glorioso()

    except Exception as error:
        texto_do_debug = open('texto do debug.txt', 'w')
        texto_do_debug.write(f"Deu erro na Mensagem dos bacanas!!!\n{error}\n")
        texto_do_debug.close()
        return "Deu Erro na Mensagem dos bacanas!!! Chame o Erick Herói Imediatamente!!!"
