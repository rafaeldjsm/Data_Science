def primeiro_lex(lst):

    men_nome = lst[0]
    for k in lst:
        ks = k.strip()
        if ks < men_nome:
            men_nome = ks
    return men_nome
