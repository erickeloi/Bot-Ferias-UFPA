from datetime import date

data_atual = date.today()
ano_atual = data_atual.year
mes_atual = data_atual.month
dia_atual = data_atual.day

# Lógica das Datas:

# Periodos Letivos - INTENSIVOS
# 2022.1
# yyyy-mm-dd
# 2022-01-03 ( inicio do 2022.1 - INTENSIVO )
# 2022-02-28 ( fim do 2022.1 - INTENSIVO )

fim_pl20221 = date(2022, 2, 28)

dias_faltando_fim_pl20221_aux = fim_pl20221 - data_atual

dias_faltando_fim_pl20221 = dias_faltando_fim_pl20221_aux.days

# Dias corridos = 56 dias
# Dias letivos = 49 dias ( Sábado também conta )

# 2022.3
# 2022-07-01 ( inicio do 2022.3 - INTENSIVO )
# 2022-08-31 ( fim do 2022.3 - INTENSIVO )

# 61 dias corridos
# 43 dias letivos

fim_pl20223 = date(2022, 8, 31)

dias_faltando_fim_pl20223_aux = fim_pl20223 - data_atual

dias_faltando_fim_pl20223 = dias_faltando_fim_pl20223_aux.days
# -------------------------------------------------

# Periodos Letivos - EXTENSIVOS
# 2022.2
# 2022-03-14 ( inicio do 2022.2 - EXTENSIVO )
# 2022-07-11 ( fim do 2022.2 - EXTENSIVO )

# 119 dias corridos
# 100 dias letivos

fim_pl20222 = date(2022, 7, 11)

dias_faltando_fim_pl20222_aux = fim_pl20222 - data_atual

dias_faltando_fim_pl20222 = dias_faltando_fim_pl20222_aux.days

# Periodos Letivos - EXTENSIVOS
# 2022.4
# 2022-08-22 ( inicio do 2022.4 - EXTENSIVO )
# 2022-12-21 ( fim do 2022.4 - EXTENSIVO )

# 121 dias corridos
# 100 dias letivos

fim_pl20224 = date(2022, 12, 21)

dias_faltando_fim_pl20224_aux = fim_pl20224 - data_atual

dias_faltando_fim_pl20224 = dias_faltando_fim_pl20224_aux.days


# -------------------------------------------------

# Lógica da Mensagem:


def texto_do_tweet():
    periodo_letivo = str()
    texto_final = ''

    def texto_padrao_dias(dias_que_faltam, periodo_atual):
        return f"Faltam {dias_que_faltam} dias para as Férias (Término do P.L. {periodo_atual})\n"

    def texto_padrao_dia(periodo_atual):
        return f"Falta 1 dia para as Férias (Término do P.L. {periodo_atual})\n"

    def texto_glorioso(periodo_atual):
        return f"Chegou o Glorioso Dia Meus Bacanos !!! (Férias - Acabou o P.L. {periodo_atual})\n"

    if ano_atual == 2022 and 1 <= mes_atual <= 2:
        periodo_letivo = '2022.1 - INTENSIVO'

        if dias_faltando_fim_pl20221 > 1:
            texto_final += texto_padrao_dias(dias_faltando_fim_pl20221, periodo_letivo)
        elif dias_faltando_fim_pl20221 == 1:
            texto_final += texto_padrao_dia(dias_faltando_fim_pl20221)
        elif dias_faltando_fim_pl20221 == 0:
            texto_glorioso(periodo_letivo)

    elif ano_atual == 2022 and 3 <= mes_atual <= 7:
        periodo_letivo = '2022.2 - EXTENSIVO'

        if dias_faltando_fim_pl20222 > 1:
            texto_final += texto_padrao_dias(dias_faltando_fim_pl20222, periodo_letivo)
        elif dias_faltando_fim_pl20222 == 1:
            texto_final += texto_padrao_dia(dias_faltando_fim_pl20222)
        elif dias_faltando_fim_pl20222 == 0:
            texto_glorioso(periodo_letivo)

    if ano_atual == 2022 and 7 <= mes_atual <= 8:
        periodo_letivo = '2022.3 - INTENSIVO'

        if dias_faltando_fim_pl20223 > 1:
            texto_final += texto_padrao_dias(dias_faltando_fim_pl20223, periodo_letivo)
        elif dias_faltando_fim_pl20223 == 1:
            texto_final += texto_padrao_dia(dias_faltando_fim_pl20223)
        elif dias_faltando_fim_pl20223 == 0:
            texto_glorioso(periodo_letivo)

    if ano_atual == 2022 and 8 <= mes_atual <= 12:
        periodo_letivo = '2022.4 - EXTENSIVO'

        if dias_faltando_fim_pl20224 > 1:
            texto_final += texto_padrao_dias(dias_faltando_fim_pl20224, periodo_letivo)
        elif dias_faltando_fim_pl20224 == 1:
            texto_final += texto_padrao_dia(dias_faltando_fim_pl20224)
        elif dias_faltando_fim_pl20224 == 0:
            texto_glorioso(periodo_letivo)

    return texto_final

