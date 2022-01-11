import copy, random, collections


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for a, b in kwargs.items():
            aux = 0
            while aux < b:
                aux = aux + 1
                self.contents.append(a)

    def draw(self, attempts):
        if attempts >= len(self.contents):
            return self.contents
        results = []
        for a in range(attempts):
            aux = random.randint(0, len(self.contents) - 1)
            results.append(self.contents[aux])
            self.contents.remove(self.contents[aux])
        return results


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches = 0
    contentsCopy = copy.deepcopy(hat.contents)
    for i in range(num_experiments):
        aux = collections.Counter(hat.draw(num_balls_drawn))
        check = True
        for a, b in expected_balls.items():
            if expected_balls[a] > aux[a]:
                check=False
        if check:
            matches = matches+1
        hat.contents = copy.deepcopy(contentsCopy)

    result = matches/num_experiments

    return result


hat1 = Hat(yellow=5, blue=2, green=6)

print(experiment(hat1, {"yellow": 3, "blue": 1}, 5, 30))
