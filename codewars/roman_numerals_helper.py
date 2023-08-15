class RomanNumerals:
    to_roman_dict={
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    from_roman_dict = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    @staticmethod
    def to_roman(val):
        out=[]
        for key,roman_numeral in sorted(RomanNumerals.to_roman_dict.items(),reverse=True):
            if(val%key<val):
                quotient,remainder=divmod(val,key)
                out.append(roman_numeral*quotient)
                val=remainder
        return "".join(out)

    @staticmethod
    def from_roman(roman_num):
        count=0
        i = 0
        while i < len(roman_num):
            if i + 1 < len(roman_num) and roman_num[i:i+2] in RomanNumerals.from_roman_dict:
                count += RomanNumerals.from_roman_dict[roman_num[i:i+2]]
                i += 2
            elif roman_num[i:i+1] in RomanNumerals.from_roman_dict:
                count += RomanNumerals.from_roman_dict[roman_num[i:i+1]]
                i += 1
        return count
    
roman=RomanNumerals()
print(roman.to_roman(999))
print(roman.from_roman(roman.to_roman(1595))==1595)
print(roman.from_roman('XXI'))
print(roman.from_roman('MDCLXVI'))