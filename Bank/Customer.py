class Customer:
    attributes = []
    low = 0
    high = 0

    def __init__(self, details):
        a = []
        for d in details:
            d = d.replace(',', '')
            d = d.replace('\n', '')
            d = d.replace('"', '')
            a.append(float(d))

        self.attributes = a
        self.low = 0
        self.high = 0

    def __str__(self):
        line = ""
        for a in self.attributes:
            line += str(a) + "\t"
        return line

    def get_interest(self):
        return self.low / (self.low + self.high)
