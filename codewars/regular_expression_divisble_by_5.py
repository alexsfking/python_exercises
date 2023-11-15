'''
Define a regular expression which tests if a given string representing a binary number is divisible by 5.

Examples:
# 5 divisible by 5
PATTERN.match('101') == true

# 135 divisible by 5
PATTERN.match('10000111') == true

# 666 not divisible by 5
PATTERN.match('0000001010011010') == false
Note:
This can be solved by creating a Finite State Machine that evaluates if a string representing a number in binary base is divisible by given number.

The detailed explanation for dividing by 3 is http://math.stackexchange.com/questions/140283/why-does-this-fsm-accept-binary-numbers-divisible-by-three

The FSM diagram for dividing by 5 is http://aswitalski.github.io/img/FSM-binary-divisible-by-five.png

Finite State Machine Designer - https://madebyevan.com/fsm/

FSM2Regex: Convert your FSMs to regexes and your regexes to FSMs! - https://ivanzuzak.info/noam/webapps/fsm2regex/

Simplify regex - http://ivanzuzak.info/noam/webapps/regex_simplifier/
'''


solution=r'^(0|1((1|(0|11)(01*01)*01*0)0)*(0|11)(01*01)*1)+$'