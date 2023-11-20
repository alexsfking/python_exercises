'''
### kyu 4 ###
When we attended middle school were asked to simplify mathematical expressions
like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy"). But
tell that to your pc and we'll see!

Write a function: simplify, that takes a string in input, representing a
multilinear non-constant polynomial in integers coefficients (like
"3x-zx+2xy-x"), and returns another string as output where the same expression
has been simplified in the following way ( -> means application of simplify):

All possible sums and subtraction of equivalent monomials ("xy==yx") has been
done, e.g.: "cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"


All monomials appears in order of increasing number of variables, e.g.:
"-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

If two monomials have the same number of variables, they appears in
lexicographic order, e.g.: "a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

There is no leading + sign if the first coefficient is positive, e.g.: "-y+x" ->
"x-y", but no restrictions for -: "y-x" ->"-x+y"

N.B. to keep it simplest, the string in input is restricted to represent only
multilinear non-constant polynomials, so you won't find something like
`-3+yx^2'. Multilinear means in this context: of degree 1 on each variable.

Warning: the string in input can contain arbitrary variables represented by
lowercase characters in the english alphabet.
'''

import re

overall_pattern = re.compile(r'([\+\-]?[0-9]*[a-z]+)')
term_pattern = re.compile(r'''^
                          (?P<sign>[\+\-]?)
                          (?P<coefficient>[0-9]*)
                          (?P<variables>[a-z]+)
                          $''',re.VERBOSE)
one_pattern = re.compile(r'([+\-])1(?=[a-z])')

def simplify(poly:str)->str:
    overall_matches = overall_pattern.findall(poly)
    results_dict=dict()
    for term in overall_matches:
        term_matches = term_pattern.match(term)
        sign = term_matches.groupdict().get('sign') or '+'
        coefficent = term_matches.groupdict().get('coefficient') or '1'
        variables = ''.join(sorted(term_matches.groupdict().get('variables')))
        if variables in results_dict:
            c = results_dict[variables]
            results_dict[variables] = c + int(sign+coefficent)
            if(results_dict[variables]==0):
                del results_dict[variables]
        else:
            results_dict[variables] = int(sign+coefficent)
    sorted_results = sorted(results_dict.items(),key=lambda x: (len(x[0]), x[0]))
    result_terms = [f"{value:+}{key}" for key, value in sorted_results]
    for i, term in enumerate(result_terms):
        result_terms[i] = one_pattern.sub(r'\1', term)
    result_terms[0]=result_terms[0].replace('+','')
    return ''.join(result_terms)