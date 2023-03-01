'''
        TIJD:    - klasse:  10 min
                 - functie: 25 min (15 zonder klasse)
        geschat: 45 min

'''


class ClientCard:

    def __init__(self):
        self.__id_ = id(self)
        self.__purchases_ = dict()

    def get_id(self):
        return self.__id_

    def get_purchases(self):
        return self.__purchases_

    def get_nb_purchases(self):
        return len(self.get_purchases().keys())

    def get_amount_at(self, day):
        return self.get_purchases().get(day, 0.0)

    def add_purchase(self, day, amount):
        if day not in self.get_purchases():
            self.get_purchases()[day] = amount
        else:
            self.get_purchases()[day] += amount

    def get_total(self, start, end):
        total = 0
        if end is None:
            for day in range(start, max(self.get_purchases().keys())):
                total += self.get_purchases().get(day,0)
        else:
            for day in range(start, end):
                total += self.get_purchases().get(day,0)
        return total

    def transfer_from(self, other):
        self.get_purchases().update(other)
        other.get_purchases().clear()

    def __str__(self):
        in_filter = len(list(filter(lambda day: card.get_amount_at(day) >= 1000, range(50, 150)))) == 1
        header = "ID: " + str(self.get_id()) + \
                 "  |  nb of purchases: " + str(self.get_nb_purchases()) +  \
                 "  |  in filter(50/150): " + str(in_filter) + \
                 '  |  total(100/200): ' + (str(card.get_total(100, 200)) if in_filter else "NA") + \
                 "\n" + "--------------------------------------------------------------------------------------------" + "\n"
        body = ""

        for day, amount in sorted(self.get_purchases().items()):
            amount_txt = str(amount)
            day_text = str(day) + " : " + amount_txt + "\n"
            body += day_text

        return header + body


def total(clientcardslst):
    return sum(map(lambda card: card.get_total(100, 200),
                   filter(lambda card: len(list(
                           filter(lambda day: card.get_amount_at(day) >= 1000,range(50, 150)))) == 1,
                          clientcardslst)))


import random

clientcards = []
amounts = [k for k in range(2000)]
days = [k for k in range(300)]
for N in range(10):
    card = ClientCard()
    for n in range(random.randint(3, 15)):
        card.add_purchase(random.choice(days), random.choice(amounts))
    clientcards.append(card)

for card in clientcards:
    print(card)

print(total(clientcards))