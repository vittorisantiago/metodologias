import json


def verificar_requisitos():
    with open('requerimientos.json') as f:
        requisitos = json.load(f)
    if requisitos['actualizados']:
        return 0
    return 1


if __name__ == "__main__":
    exit(verificar_requisitos())

