
class FigureToWord:
    WORD_DICT = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }
    LEVEL = {
        1: "",
        2: "thousand",
        3: "million",
        4: "billion",
        5: "trillion",
        6: "quadrillion",
        7: "quintillion",
        8: "sextillion",
        9: "septillion"
    }

    def __init__(self, pointKeyword="Decimal",
                 includeCommas=True,
                 includeDecimalPlaces=True
                 ):
        self.__keyword = pointKeyword
        self.__decimals = includeDecimalPlaces
        self.__commas = includeCommas

    @property
    def pointKeyword(self):
        return self.__keyword

    @property
    def addDecimals(self):
        return self.__decimals

    @property
    def addCommas(self):
        return self.__commas

    @pointKeyword.setter
    def pointKeyword(self, keyword: str):
        self.__keyword = keyword

    @addDecimals.setter
    def addDecimals(self, includeDecimals: bool):
        self.__decimals = includeDecimals

    @addCommas.setter
    def addCommas(self, includeCommas: bool):
        self.__commas = includeCommas

    def convertToWords(self, number):
        # convert number to str from int or float
        number = str(number) if not isinstance(number, str) else number.strip()
        try:
            negative = "Negative " if float(number) < 0 else ""
            levels, point_num = self.generate_levels(number.replace("-", ""))
        except ValueError:
            return f'Input "{number}" MUST be a number'

        lev = len(levels)
        if lev > 9:
            return f"{negative}{','.join(levels)}.{point_num} is too big, bigger that Septillion."

        inWords = ""
        for level in levels:
            if level == "000":
                lev -= 1
                continue
            inWords = self.readHundreds(level, inWords, self.LEVEL[lev])
            lev -= 1

        inWords = f"{negative}{inWords}"
        inWords = self.add_commas(inWords) if self.__commas else inWords
        inWords = self.addDecimalWords(point_num, inWords) if self.__decimals else inWords

        return inWords.capitalize()

    def readHundreds(self, number, prev_words: str = "", level: str = ""):
        number = int(number)
        if number == 0:
            return self.WORD_DICT[0]
        else:
            number_str = str(number)
            if number >= 100:
                hundreds, tens, ones, teens = int(number_str[0]), int(number_str[1]), int(number_str[2]), int(
                    number_str[1:])
            elif number >= 10:
                hundreds, tens, ones, teens = 0, int(number_str[0]), int(number_str[1]), number
            else:
                hundreds, tens, ones, teens = 0, 0, number, number

            hundredth_word = f"{self.WORD_DICT[hundreds]} hundred" if hundreds else ""
            level = f" {level}" if level else ""
            add_space = " " if prev_words else ""
            if 1 <= teens <= 19:
                word = "and " if prev_words and teens == number and not level else ""
                word += self.WORD_DICT[teens]
            else:
                tenth_word = self.WORD_DICT[tens * 10] if tens else ""
                ones_word = self.WORD_DICT[ones] if ones else ""
                # tenth_space = " " if ones_word else ""
                tenth_space = ""
                hyphen = "-" if tenth_word and ones_word else ""
                word = f"{tenth_word}{hyphen}{tenth_space}{ones_word}"

            hundred_and = " and " if hundredth_word and word else ""
            word = f"{prev_words}{add_space}{hundredth_word}{hundred_and}{word}{level}"
            return word

    def generate_levels(self, number: str):
        # check if number is numeric or float
        whole_number, point_number = number, ''
        point_key = number.find('.')  # check if the number to be converted has a decimal place
        if point_key > -1:
            whole_number = number[:point_key]
            # merging all the "point_number" statements on 1 like makes it difficult to read and understand
            point_number = f"0.{number[point_key + 1:]}"
            point_number = str(float(point_number))
            point_number = point_number[2:]

        level_loops = len(whole_number) // 3
        mod = len(whole_number) % 3  # check how many digits does the first level have, either 1, 2 or 3
        first_section = 3 if mod == 0 else mod
        slice_from, slice_to = 0, first_section
        add = 1 if mod else 0  # If modulus == 0, there is no need for 1 extra loop
        levels = []
        for i in range(level_loops + add):
            slice = whole_number[slice_from:slice_to]
            levels.append(slice)  # save slices
            slice_from, slice_to = slice_to, slice_to + 3  # prepare the next slice
        return levels, point_number

    def add_commas(self, words: str):
        return words.replace("illion ", "illion, ").replace("thousand ", "thousand, ")

    def addDecimalWords(self, number: str, words):
        if number:
            words += f" {self.__keyword}"
            for num in number:
                words += f" {self.WORD_DICT[int(num)]}"
        return words
