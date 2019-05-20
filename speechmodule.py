FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    output = []
    if number >= 100:
        hundreds = number / 100
        output.append(FIRST_TEN[hundreds - 1])
        output.append('hundred')
        number = number % 100
    if number < 100 and number >= 20:
        tens = number / 10
        output.append(OTHER_TENS[tens - 2])
        number = number % 10
        print number
        print output
    if number >= 10 and number < 20:
        print number
        output.append(SECOND_TEN[number % 10])
    if number < 10 and number > 0:
        output.append(FIRST_TEN[number - 1])

    #replace this for solution
    return ' '.join(output)

print checkio(20)