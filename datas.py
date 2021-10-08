class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.ano = ano
        self. mes = mes

    def formatada(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))