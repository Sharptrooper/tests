import re


def funcao(string, display=False):
    # catch to ensure string does not exceed maximum length
    if len(string) > 5:
        return "Error: Too many problems."
    finalFirstRow = ""
    finalSecondRow = ""
    finalSlashRow = ""
    finalResultRow = ""

    for a in string:
        b = a.split()

        # checks which one of the two digits is bigger
        if len(b[0]) > len(b[2]):
            length = len(b[0]) + 2
        else:
            length = len(b[2]) + 2

        # catch to make sure operand is addition or subtraction
        if b[1] != "+" and b[1] != "-":
            return "Error: Operator must be '+' or '-'."

        # regEx check to see if any forbidden characters are included
        if bool(re.search("[\D]", b[0])) or bool(re.search("[\D]", b[2])):
            return "Error: Numbers must only contain digits."
        # catch to make sure number size is not exceeded
        for aux in b:
            if len(aux) > 4:
                return "Error: Numbers cannot be more than four digits."
        # loop to align first number
        newFirstRow = b[0]
        while len(newFirstRow) < length:
            newFirstRow = " " + newFirstRow
        finalFirstRow = finalFirstRow + newFirstRow

        # loop to align second number
        newSecondRow = b[1] + " "
        while len(newSecondRow) + len(b[2]) < length:
            newSecondRow = newSecondRow + " "
        finalSecondRow = finalSecondRow + newSecondRow + b[2]

        # slashes!
        for aux in range(length):
            finalSlashRow = finalSlashRow + "-"

        # loop to align result line. math is ugly
        if b[1] == "+":
            newResultRow = int(b[0]) + int(b[2])
        else:
            newResultRow = int(b[0]) - int(b[2])
        newResultRow = str(newResultRow)
        while len(newResultRow) < length:
            newResultRow = " " + newResultRow
        finalResultRow = finalResultRow + newResultRow

        # adds spaces between each equation to increase readability
        if a != string[-1]:
            finalSlashRow += "    "
            finalFirstRow += "    "
            finalSecondRow += "    "
            finalResultRow += "    "
    supremeFinal = ""
    if display:
        supremeFinal = finalFirstRow + "\n" + finalSecondRow + "\n" + finalSlashRow + "\n" + finalResultRow
    else:
        supremeFinal = finalFirstRow + "\n" + finalSecondRow + "\n" + finalSlashRow
    return supremeFinal


print(funcao(["45 + 78", "9000 - 784", "500 + 654", "676 + 767"], True))
