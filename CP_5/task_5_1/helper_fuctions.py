
dict1 = {'0':'\u2070',
         '1':'\u00b9',
         '2':'\u00b2',
         '3':'\u00b3',
         '4':'\u2074',
         '5':'\u2075',
         '6':'\u2076',
         '7':'\u2077',
         '8':'\u2078',
         '9':'\u2079',
         '+':'\u207A',
         '-':'\u207B',
         '=':'\u207C',
         '(':'\u207D',
         ')':'\u207E',
         'n':'\u2084',}

dict2 = {'0':'\u2080',
         '1':'\u2081',
         '2':'\u2082',
         '3':'\u2083',
         '4':'\u2084',
         '5':'\u2085',
         '6':'\u2086',
         '7':'\u2087',
         '8':'\u2088',
         '9':'\u2089',
         '+':'\u208A',
         '-':'\u208B',
         '=':'\u208C',
         '(':'\u208D',
         ')':'\u208E',
         'a':'\u2090',
         'e':'\u2091',
         'o':'\u2092',
         'x':'\u2093',
         'h':'\u2095',
         'k':'\u2096',
         'l':'\u2097',
         'm':'\u2098',
         'n':'\u2099',
         'p':'\u209A',
         's':'\u209B',
         't':'\u209C'}

def sups(base,x):
    z = '{}'.format(dict1.get(x))
    return base + z

def subs(base,x):
    z = '{}'.format(dict2.get(x))
    return base + z



def polynomial_str(coefficients):
    pol_string = f"P(λ) = "
    curr_power = len(coefficients) - 1

    for coff in coefficients:

        if curr_power == 0:
            if coff < 0:
                pol_string += "- " + str(abs(coff))
            elif coff > 0:
                pol_string += "+ " + str(coff)
            else:
                continue

        elif curr_power == 1:
            if coff < 0:
                pol_string += f"- {abs(coff)}λ "
            elif coff > 0:
                pol_string += f"+ {coff}λ "
            else:
                curr_power -= 1
                continue

        elif curr_power < len(coefficients) - 1:
            if coff < 0:
                pol_string += f"- {abs(coff)}{sups('λ', str(curr_power))} "
            elif coff > 0:
                pol_string += f"+ {coff}{sups('λ', str(curr_power))} "
            else:
                curr_power -= 1
                continue

        elif curr_power == len(coefficients) - 1:
            if coff == 1:
                pol_string += f"{sups('λ', str(curr_power))} "
            elif coff != 0:
                pol_string += f"{coff}{sups('λ', str(curr_power))} "
            else:
                curr_power -= 1
                continue
        curr_power -= 1

    return pol_string


def display_coeficients(coefficients):
    for i in range(len(coefficients)):
        print(f"{subs('p', str(i))} = {coefficients[i]}")

def display_roots(roots):
    for i in range(len(roots)):
        print(f"{subs('λ', str(i+1))} = {roots[i]}")

# print_coefficients([1,2,3])