def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: NÃO PODE VOTAR.'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
