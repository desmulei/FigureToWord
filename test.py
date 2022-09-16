from figureToWord import FigureToWord

convert = FigureToWord()  # create an object

# TEST 1
in_words = convert.convertToWords(777777777771)
print(in_words)
# OUTPUT --- Seven hundred and seventy-seven billion, seven hundred and seventy-seven million,
# seven hundred and seventy-seven thousand, seven hundred and seventy-one


# TEST 2
convert.addCommas = False
convert.addDecimals = True
in_words = convert.convertToWords(4887519857.8965)
print(in_words)
# OUTPUT --- Four billion eight hundred and eighty-seven million five hundred and nineteen thousand
# eight hundred and fifty-seven decimal eight nine six five


# TEST 3
convert.pointKeyword = 'point'
convert.addCommas = True
number = "98634509100032456723565443345.78405200"
in_words = convert.convertToWords(number)
print(in_words.upper())
# OUTPUT --- NINE HUNDRED AND EIGHTY-SIX QUADRILLION, THREE HUNDRED AND FORTY-FIVE TRILLION, NINETY-ONE BILLION,
# THREE HUNDRED AND TWENTY-FOUR THOUSAND, FIVE HUNDRED AND SIXTY-SEVEN POINT SEVEN EIGHT FOUR ZERO FIVE TWO


# TEST 4
in_words = convert.convertToWords(-345097290)
print(in_words)
# OUTPUT --- Negative three hundred and forty-five million, ninety-seven thousand, two hundred and ninety
