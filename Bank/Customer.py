class Customer:
    attributes = []

    def __init__(self, details):
        a = []
        for d in details:
            d = d.replace(',', '')
            d = d.replace('\n', '')
            d = d.replace('"', '')
            a.append(float(d))

        self.attributes = a

    def __str__(self):
        line = ""
        for a in self.attributes:
            line += str(a) + "\t"
        return line
