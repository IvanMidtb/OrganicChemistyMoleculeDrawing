####################################
# Ivan Midtbust Heger, Jackson Sims
# CSCI 150
# Final Project
####################################

from typing import *
import turtle
import Letter_Drawing

# used to translate from alkane names to their lengths and to find valid alkanes
prefix_dic = {'meth': 1, 'eth': 2, 'prop': 3, 'but': 4, 'pent': 5, 'hex': 6, 'hept': 7, 'oct': 8, 'non': 9, 'dec': 10,
              'undec': 11, 'dodec': 12}
sub_prefix_list = {'hydroxy', 'fluoro', 'chloro', 'bromo', 'iodo', 'one', 'oxo'}
sub_suffix_list = {'ol', 'one', 'al'}


# Asks the user to input an organic compound name and draws it using turtle. The asks if they would like to go again
def main():
    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    done = False
    while not done:
        compound = input('Please enter an organic compound to draw: ').lower()
        try:
            organized_compound = str_breaker(compound)

            if is_valid_input(organized_compound):
                parent = organized_compound['parent'][0]
                t.goto(-parent * 15, 0)
                t.pendown()
                t.seth(30)
                alkane_draw(t, parent, 50)
            else:
                organized_compound = {}
                parent = ''

            # Draws substituents
            first = False
            last = False
            for i in organized_compound:
                if i.isnumeric():
                    if int(i) % 2 == 0:
                        angle = 90
                    else:
                        angle = -90
                    if i == '1':
                        first = True
                    elif i == str(parent):
                        last = True
                    for j in organized_compound[i]:
                        t.penup()
                        t.goto(-parent * 15, 0)
                        t.seth(30)
                        alkane_draw(t, int(i), 50)
                        t.pendown()
                        t.seth(angle)
                        if first:
                            t.seth(180)
                            first = False
                            angle = -angle
                        elif last:
                            t.seth(0)
                            last = False
                        sub_draw(t, j, t.heading(), parent, i)

                        angle = -angle
        except:
            print("Undefined input error")

        # Moves turtle out of the way
        t.penup()
        t.seth(0)
        t.goto(0, -500)

        done = go_again(t)


# Checks if an entered compound is valid
def is_valid_input(organized_compound: Dict[str, str]) -> bool:
    if 'parent' not in organized_compound:
        print("No parent chain found")
        return False
    for i in organized_compound:
        if (i == '1' or i == str(length_get(organized_compound[i]))) and len(organized_compound[i]) > 3:
            print('Invalid input, carbon can only have four bonds')
            return False
        elif len(organized_compound[i]) > 2 and not (i == '1' or i == str(organized_compound['parent'][0])):
            print('Invalid input, carbon can only have four bonds')
            return False
        for j in organized_compound[i]:
            if (not str(j).isnumeric()) and (j[:-2] not in prefix_dic) and (j not in sub_suffix_list)\
                    and (j not in sub_prefix_list):
                print('Invalid substring')
                return False
        if i.isnumeric():
            if int(i) > int(organized_compound['parent'][0]):
                print("Can't place substrate on carbon " + i + ". Parent is of length: " + organized_compound['parent'][0])
                return False
    return True


# Breaks down the name of an organic compound into more organized information
def str_breaker(mol: str) -> Dict[str, str]:
    organized = {}
    mol = mol.replace(',', '-')
    mol_parts = mol.split('-')

    # looks at the suffix on the parent molecule
    if mol_parts[-1] in sub_suffix_list:
        if mol_parts[-2].isnumeric():
            organized[mol_parts[-2]] = [mol_parts[-1]]
            mol_parts = mol_parts[:-2]
        else:
            organized['1'] = [mol_parts[-1]]
            mol_parts = mol_parts[:-1]
        mol_parts[-1] += 'e'
    else:
        for x in sub_suffix_list:
            if mol_parts[-1].rfind(x) != -1:
                organized['1'] = [x]
                mol_parts[-1] = mol_parts[-1][:-len(x)] + 'e'

    # takes care of the case where there are no substituents aside of the prefix
    if is_alkane(mol_parts[-1]):
        organized['parent'] = [length_get(mol_parts[-1])]

    # Breaks chain into parent chain and substituents
    else:
        # removes alkane subs from parent chain
        for i in prefix_dic:
            sub_index = mol_parts[-1].find(i)
            if sub_index == 0:
                organized['parent'] = [length_get(mol_parts[-1][len(i) + 2:])]
                mol_parts[-1] = mol_parts[-1][:len(i) + 2]
            elif sub_index == 2 and mol_parts[-1][0:2] == 'di':
                organized['parent'] = [length_get(mol_parts[-1][len(i) + 4:])]
                mol_parts[-1] = mol_parts[-1][:len(i) + 4]
            elif sub_index == 3 and mol_parts[-1][0:3] == 'tri':
                organized['parent'] = [length_get(mol_parts[-1][len(i) + 5:])]
                mol_parts[-1] = mol_parts[-1][:len(i) + 5]

        # removes non-alkane subs from parent chain
        for i in sub_prefix_list:
            sub_index = mol_parts[-1].find(i)
            if sub_index == 0:
                organized['parent'] = [length_get(mol_parts[-1][len(i):])]
                mol_parts[-1] = i
            elif sub_index == 2 and mol_parts[-1][0:2] == 'di':
                organized['parent'] = [length_get(mol_parts[-1][len(i) + 2:])]
                mol_parts[-1] = mol_parts[-1][:len(i) + 2]
            elif sub_index == 3 and mol_parts[-1][0:3] == 'tri':
                organized['parent'] = [length_get(mol_parts[-1][len(i) + 3:])]
                mol_parts[-1] = mol_parts[-1][:len(i) + 3]

        # Organizes substituents in the organized dictionary under the appropriate number
        number_store = []
        for j in range(len(mol_parts)):
            if mol_parts[j].isnumeric():
                number_store.append(mol_parts[j])
            else:
                if not number_store:
                    number_store = ['1']
                if mol_parts[j][:2] == 'di':
                    mol_parts[j] = mol_parts[j][2:]
                    if number_store == ['1']:
                        number_store *= 2
                elif mol_parts[j][:3] == 'tri':
                    mol_parts[j] = mol_parts[j][3:]
                    if number_store == ['1']:
                        number_store *= 3
                for x in number_store:
                    if x not in organized:
                        organized[x] = []
                    organized[x].append(mol_parts[j])
                number_store = []

    # print(organized)
    return organized


# Checks to see if a string is an alkane name
def is_alkane(mol: str) -> bool:
    if mol[-3:] == 'ane':
        mol = mol[:-3]
        if mol in prefix_dic:
            return True
    return False


# draws an alkane of a given length
def alkane_draw(t, l, size):
    angle = 30
    for i in range(l-1):
        t.forward(size)
        if angle == 30:
            angle = 60
        angle = -1 * angle
        t.left(angle)


# Takes the name of an alkane and returns the number of carbons up to 10 carbons
# prints an error message and returns -1 if an alkane is not entered
# eg. methane -> 1, ethane -> 2, propane -> 3
def length_get(mol: str) -> int:
    if not is_alkane(mol):
        return -1
    prefix = mol[:-3]
    return prefix_dic[prefix]


# Checks the substrings for specific sub_prefixes in the list,
# and adds the relevant element's symbol if necessary
def sub_draw(t, j, angle, parent, i):
    if j[:-2] in prefix_dic:
        length = prefix_dic[j[:-2]]
        alkane_draw(t, length + 1, 50)
    elif j in sub_prefix_list or j in sub_suffix_list:
        alkane_draw(t, 2, 50)
        t.seth(angle)
        t.penup()
        t.forward(10)
        t.pendown()
        t.seth(0)
        if j == 'chloro':
            Final.letter_testing.letter_cl(t, 1, 15)
        elif j == 'fluoro':
            Final.letter_testing.letter_fl(t, 1, 15)
        elif j == 'bromo':
            Final.letter_testing.letter_br(t, 1, 15)
        elif j == 'iodo':
            Final.letter_testing.letter_i(t, 1, 15)
        elif j == 'hydroxy' or j == 'ol':
            Final.letter_testing.letter_o(t, 1, 15)
            t.seth(0)
            t.penup()
            t.forward(10)
            t.pendown()
            Final.letter_testing.letter_h(t, 1, 15)
        elif j == 'one' or j == 'oxo' or j == 'al':
            Final.letter_testing.letter_o(t, 1, 15)
            t.penup()
            t.goto(-parent * 15 + 5, 0)
            t.seth(30)
            alkane_draw(t, int(i), 50)
            if angle == 180 or angle == 0:
                t.seth(90)
                t.forward(5)
            t.seth(angle)
            t.pendown()
            alkane_draw(t, 2, 50)
            t.seth(0)


# Asks user if they want to draw another compound.
# Ends the program if "no."
def go_again(t):
    valid_input = False
    complete = False
    while not valid_input:
        again = input('Would you like to go again? ')
        if again.lower() == 'no':
            valid_input = True
            complete = True
        elif again.lower() == 'yes':
            valid_input = True
        else:
            print('Please enter "Yes" or "No". ')
    t.clear()
    return complete


main()
