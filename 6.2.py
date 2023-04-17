import random
def ticket():
    win = [1, 2, 3, 4, 5, 6, 7]

    count = 0
    for i in range(0,10000):
        ticket = []
        while len(ticket) < 7:
            num = random.randint(1, 15)
            if num not in ticket:
                ticket.append(num)
        ticket.sort()

        if ticket == win:
            count += 1

    probability = count/10000
    return probability

probability=ticket()
print(probability)
