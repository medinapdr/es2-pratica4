def valida_cpf(cpf: str) -> bool:
    cpf = cpf.replace(".", "").replace("-", "")

    if len(cpf) != 11 or not cpf.isdigit():
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    digito1 = digito1 if digito1 < 10 else 0

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11)
    digito2 = digito2 if digito2 < 10 else 0

    return cpf[-2:] == f"{digito1}{digito2}"

