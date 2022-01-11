import gc


class Category:
    totalLedger = []

    def __init__(self, name):
        self.name = name
        self.total = 0
        self.ledger = []

    def deposit(self, amount, description=""):
        amount = float(amount)
        Category.totalLedger.append({"amount": float(amount), "description": description})
        self.ledger.append({"amount": float(amount), "description": description})
        self.total = self.total + float(amount)

    def withdraw(self, amount, description=""):
        amount = float(amount)

        if self.check_funds(amount):
            self.total = self.total + float(-abs(amount))
            Category.totalLedger.append({"amount": float(-abs(amount)), "description": description})
            self.ledger.append({"amount": float(-abs(amount)), "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return self.total

    def check_funds(self, value):
        if value <= self.total:
            return True
        else:
            return False

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            aux = "Transfer to " + destination.name
            self.withdraw(amount, aux)
            aux = "Transfer from " + self.name
            destination.deposit(amount, aux)
            return True
        else:
            return False

    def __str__(self):
        output = ""
        titleLine = ""

        # Generates Title Line
        a = int((30 - len(self.name)) / 2)
        for b in range(a):
            titleLine = titleLine + "*"
        titleLine = titleLine + self.name
        while len(titleLine) < 30:
            titleLine = titleLine + "*"

        output = titleLine + "\n"

        # Goes through the local ledger and generates each line
        localTotal = 0
        for a in self.ledger:
            currentValue = " " + str("{:,.2f}".format(a["amount"]))
            currentDesc = a["description"]
            localTotal = localTotal + float(a["amount"])

            while len(currentDesc) + len(currentValue) < 30:
                currentDesc = currentDesc + " "

            if len(currentDesc) + len(currentValue) > 30:
                currentDesc = currentDesc[:30 - len(currentValue)]

            output = output + currentDesc + currentValue + "\n"

        # Adds the final balance of the local ledger
        output = output + "Total: " + str(localTotal)

        return output


def create_spend_chart(catList):
    graphList = []
    negativeSum = 0
    spendChart = ""
    # Find how much spending is in each category
    for obj in catList:
        if isinstance(obj, Category):
            aux = 0
            for a in obj.ledger:
                if a["amount"] < 0:
                    aux = aux + abs(a["amount"])
                    negativeSum = negativeSum + abs(a["amount"])
            graphList.append({"name": obj.name, "amount": aux, "percent": 0})

    for a in graphList:
        if a["amount"]/negativeSum > 0.1:
            a["percent"] = (round(a["amount"] / negativeSum, 1)) * 100
        else:
            a["percent"] = 0

    # Draws the graph

    x = 100

    while x >= 0:
        if x > 99:
            spendChart = spendChart + str(x) +"|"
        elif x > 1:
            spendChart = spendChart + " " + str(x) +"|"
        else:
            spendChart = spendChart + "  " + str(x) +"|"
        for a in graphList:
            if int(a["percent"]) >= int(x):
                spendChart = spendChart +" o "
            else:
                spendChart = spendChart +"   "
        spendChart = spendChart+" "
        if x == 100:
            lineLength = len(spendChart)
        x = x - 10
        spendChart = spendChart+"\n"

    # Creates the hash line

    spendChart = spendChart+"    "
    for x in range(lineLength-4):
        spendChart = spendChart + "-"
    spendChart=spendChart+"\n"

    # Finds longest name

    nameLength=0
    for a in graphList:
        if len(a["name"]) > nameLength:
            nameLength = len(a["name"])

    for x in range(nameLength):
        spendChart = spendChart + "    "
        for y in graphList:
            aux = y["name"]
            auxList = list(aux)

            try:
                spendChart = spendChart +" "+ auxList[x] + " "
            except:
                spendChart = spendChart + "   "
        spendChart = spendChart + " \n"
    spendChart = spendChart[:-1]
    spendChart = "Percentage spent by category\n" + spendChart

    return spendChart















food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)


print(create_spend_chart([business, food, entertainment]))


print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
