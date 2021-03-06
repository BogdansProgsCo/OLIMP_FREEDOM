import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1427&f_team=2702&chome=0&new_tid=1427'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

a = "SCOTLAND.txt"

drw_NOdrw = 7
NOdrw_drw = 7
od_ev = 7
ev_od = 7
und15_ovr15 = 7
ovr15_und15 = 7
und25_ovr25 = 7
ovr25_und25 = 7
both_noboth = 7
noboth_both = 7
drw_NOdrw_ft = 7
NOdrw_drw_ft = 7
goal_NOgoal_ft = 7
NOgoal_goal_ft = 7

def adding_team():
    c = "SCOTLAND"
    b = "Aberdeen"
    new_file = open(a, "a+")
    new_file.write('\n _______ ' + c + ' _______')
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


def clean_file():
    new_file = open(a, 'w+')
    new_file.seek(0)
    new_file.close()

def create_file():
    new_file = open(a, "a+")
    # print(new_file.name)
    new_file.close()

def draws_NOdraws(x):
    count = 0
    olimp = []
    for i in x:
        if i == '0:0 ' or i == '1:1 ' or i == '2:2 ' or i == '3:3 ' or i == '4:4 ' or i == '5:5 ' or i == '6:6 ':
            olimp.append("+")
        else:
            olimp.append("-")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
                                                                            if len(olimp) >= 19 and olimp[18] == '+':
                                                                                count += 1
    if count >= drw_NOdrw:
        print(f'??????????_?????????????? = {count}')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n draws_NOdraws = ' + b)
        new_file.close()

def NOdraws_draws(x):
    count = 0
    olimp = []
    for i in x:
        if i == '0:0 ' or i == '1:1 ' or i == '2:2 ' or i == '3:3 ' or i == '4:4 ' or i == '5:5 ' or i == '6:6 ':
            olimp.append("-")
        else:
            olimp.append("+")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
                                                                            if len(olimp) >= 19 and olimp[18] == '+':
                                                                                count += 1
    if count >= NOdrw_drw:
        print(f'??????????????_?????????? = {count}')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n NOdraws_draws = ' + b)
        new_file.close()

def odd_even(x):
    count = 0
    olimp = []
    for i in x:
        if (i != '0:0 ' and i != '1:1 ' and i != '2:2 ' and i != '3:3 ' and i != '4:4 ' and i != '5:5 '
                and i != '2:0 ' and i != '0:2 ' and i != '1:3 ' and i != '3:1 ' and i != '4:2 ' and i != '2:4 '
                and i != '3:5 ' and i != '5:3 ' and i != '4:6 ' and i != '6:4 ' and i != '4:0 ' and i != '0:4 '
                and i != '1:5 ' and i != '5:1 ' and i != '2:6 ' and i != '6:2 ' and i != '3:7 ' and i != '7:3 '
                and i != '0:6 ' and i != '6:0 ' and i != '1:7 ' and i != '7:1 '):
            olimp.append("+")
        else:
            olimp.append("-")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
                                                                            if len(olimp) >= 19 and olimp[18] == '+':
                                                                                count += 1
    if count >= od_ev:
        print(f'??????????_?????? = {count}')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n odd_even = ' + b)
        new_file.close()

def even_odd(x):
    count = 0
    olimp = []
    for i in x:
        if (i != '0:0 ' and i != '1:1 ' and i != '2:2 ' and i != '3:3 ' and i != '4:4 ' and i != '5:5 '
                and i != '2:0 ' and i != '0:2 ' and i != '1:3 ' and i != '3:1 ' and i != '4:2 ' and i != '2:4 '
                and i != '3:5 ' and i != '5:3 ' and i != '4:6 ' and i != '6:4 ' and i != '4:0 ' and i != '0:4 '
                and i != '1:5 ' and i != '5:1 ' and i != '2:6 ' and i != '6:2 ' and i != '3:7 ' and i != '7:3 '
                and i != '0:6 ' and i != '6:0 ' and i != '1:7 ' and i != '7:1 '):
            olimp.append("-")
        else:
            olimp.append("+")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
                                                                            if len(olimp) >= 19 and olimp[18] == '+':
                                                                                count += 1
    if count >= ev_od:
        print(f'??????_?????????? = {count}')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n even_odd = ' + b)
        new_file.close()

def under15_over15(x):
    count = 0
    olimp = []
    for i in x:
        if i == '0:0 ' or i == '1:0 ' or i == '0:1 ':
            olimp.append("+")
        else:
            olimp.append("-")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
                                                                            if len(olimp) >= 19 and olimp[18] == '+':
                                                                                count += 1
    if count >= und15_ovr15:
        print(f'??????_?????? 1.5 = {count}')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n under_over 1.5 = ' + b)
        new_file.close()

def over15_under15(x):
    count = 0
    olimp = []
    for i in x:
        if i == '0:0 ' or i == '1:0 ' or i == '0:1 ':
            olimp.append("-")
        else:
            olimp.append("+")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
                                                                            if len(olimp) >= 19 and olimp[18] == '+':
                                                                                count += 1
    if count >= ovr15_und15:
        print(f'??????_?????? 1.5 = {count}')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n over_under 1.5 = ' + b)
        new_file.close()

def under25_over25(x):
    count = 0
    olimp = []
    for i in x:
        if (i == '0:0 ' or i == '1:1 ' or i == '1:0 '
                or i == '0:1 ' or i == '2:0 ' or i == '0:2 '):
            olimp.append("+")
        else:
            olimp.append("-")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
                                                                            if len(olimp) >= 19 and olimp[18] == '+':
                                                                                count += 1
    if count >= und25_ovr25:
        print(f'??????_?????? 2.5 = {count}')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n under_over 2.5 = ' + b)
        new_file.close()

def over25_under25(x):
    count = 0
    olimp = []
    for i in x:
        if (i == '0:0 ' or i == '1:1 ' or i == '1:0 '
                or i == '0:1 ' or i == '2:0 ' or i == '0:2 '):
            olimp.append("-")
        else:
            olimp.append("+")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
                                                                            if len(olimp) >= 19 and olimp[18] == '+':
                                                                                count += 1
    if count >= ovr25_und25:
        print(f'??????_?????? 2.5 = {count}')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n over_under 2.5 = ' + b)
        new_file.close()

def both_noboth_score(x):
    count = 0
    olimp = []
    for i in x:
        if (i != '0:0 ' and i != '1:0 ' and i != '0:1 ' and i != '2:0 ' and i != '0:2 ' and i != '0:3 ' and i != '3:0 '
                and i != '4:0 ' and i != '0:4 ' and i != '0:5 ' and i != '5:0 ' and i != '0:6 ' and i != '6:0 '
                and i != '0:7 ' and i != '7:0 '):
            olimp.append("+")
        else:
            olimp.append("-")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
                                                                            if len(olimp) >= 19 and olimp[18] == '+':
                                                                                count += 1
    if count >= both_noboth:
        print(f'??????_?????????? ???????????? = {count}')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n both_noboth score = ' + b)
        new_file.close()

def noboth_both_score(x):
    count = 0
    olimp = []
    for i in x:
        if (i != '0:0 ' and i != '1:0 ' and i != '0:1 ' and i != '2:0 ' and i != '0:2 ' and i != '0:3 ' and i != '3:0 '
                and i != '4:0 ' and i != '0:4 ' and i != '0:5 ' and i != '5:0 ' and i != '0:6 ' and i != '6:0 '
                and i != '0:7 ' and i != '7:0 '):
            olimp.append("-")
        else:
            olimp.append("+")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
                                                                            if len(olimp) >= 19 and olimp[18] == '+':
                                                                                count += 1
    if count >= noboth_both:
        print(f'??????????_?????? ???????????? = {count}')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n noboth_both score = ' + b)
        new_file.close()

def draws_NOdraws_first_time(x):
    count = 0
    olimp = []
    for i in x:
        if i == '(0:0)' or i == '(1:1)' or i == '(2:2)' or i == '(3:3)' or i == '(4:4)' or i == '(5:5)':
            olimp.append("+")
        else:
            olimp.append("-")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
                                                                            if len(olimp) >= 19 and olimp[18] == '+':
                                                                                count += 1
    if count >= drw_NOdrw_ft:
        print(f'??????????_?????????????? 1-?? ???????? = {count}')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n draws_NOdraws 1st time = ' + b)
        new_file.close()

def NOdraws_draws_first_time(x):
    count = 0
    olimp = []
    for i in x:
        if i == '(0:0)' or i == '(1:1)' or i == '(2:2)' or i == '(3:3)' or i == '(4:4)' or i == '(5:5)':
            olimp.append("-")
        else:
            olimp.append("+")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
                                                                            if len(olimp) >= 19 and olimp[18] == '+':
                                                                                count += 1
    if count >= NOdrw_drw_ft:
        print(f'??????????????_?????????? 1-?? ???????? = {count}')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n NOdraws_draws 1st time = ' + b)
        new_file.close()

def goal_NOgoal_first_time(x):
    count = 0
    olimp = []
    for i in x:
        if i != '(0:0)':
            olimp.append("+")
        else:
            olimp.append("-")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
                                                                            if len(olimp) >= 19 and olimp[18] == '+':
                                                                                count += 1
    if count >= goal_NOgoal_ft:
        print(f'??????-?????????? 1-?? ???????? = {count}')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n goal_NOgoal 1st time = ' + b)
        new_file.close()

def NOgoal_goal_first_time(x):
    count = 0
    olimp = []
    for i in x:
        if i != '(0:0)':
            olimp.append("-")
        else:
            olimp.append("+")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
                                                                            if len(olimp) >= 19 and olimp[18] == '+':
                                                                                count += 1
    if count >= NOgoal_goal_ft:
        print(f'??????????_?????? 1-?? ???????? = {count}')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n NOgoal_goal 1st time = ' + b)
        new_file.close()


clean_file()
create_file()
adding_team()

draws_NOdraws(rev_full_time)
NOdraws_draws(rev_full_time)

odd_even(rev_full_time)
even_odd(rev_full_time)

under15_over15(rev_full_time)
over15_under15(rev_full_time)

under25_over25(rev_full_time)
over25_under25(rev_full_time)

both_noboth_score(rev_full_time)
noboth_both_score(rev_full_time)

draws_NOdraws_first_time(rev_first_half_time)
NOdraws_draws_first_time(rev_first_half_time)

goal_NOgoal_first_time(rev_first_half_time)
NOgoal_goal_first_time(rev_first_half_time)

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1427&f_team=2710&chome=0&new_tid=1427'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Celtic"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws_NOdraws(rev_full_time)
NOdraws_draws(rev_full_time)

odd_even(rev_full_time)
even_odd(rev_full_time)

under15_over15(rev_full_time)
over15_under15(rev_full_time)

under25_over25(rev_full_time)
over25_under25(rev_full_time)

both_noboth_score(rev_full_time)
noboth_both_score(rev_full_time)

draws_NOdraws_first_time(rev_first_half_time)
NOdraws_draws_first_time(rev_first_half_time)

goal_NOgoal_first_time(rev_first_half_time)
NOgoal_goal_first_time(rev_first_half_time)

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1427&f_team=2701&chome=0&new_tid=1427'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Dundee_Utd"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws_NOdraws(rev_full_time)
NOdraws_draws(rev_full_time)

odd_even(rev_full_time)
even_odd(rev_full_time)

under15_over15(rev_full_time)
over15_under15(rev_full_time)

under25_over25(rev_full_time)
over25_under25(rev_full_time)

both_noboth_score(rev_full_time)
noboth_both_score(rev_full_time)

draws_NOdraws_first_time(rev_first_half_time)
NOdraws_draws_first_time(rev_first_half_time)

goal_NOgoal_first_time(rev_first_half_time)
NOgoal_goal_first_time(rev_first_half_time)

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1427&f_team=2721&chome=0&new_tid=1427'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Hamilton"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws_NOdraws(rev_full_time)
NOdraws_draws(rev_full_time)

odd_even(rev_full_time)
even_odd(rev_full_time)

under15_over15(rev_full_time)
over15_under15(rev_full_time)

under25_over25(rev_full_time)
over25_under25(rev_full_time)

both_noboth_score(rev_full_time)
noboth_both_score(rev_full_time)

draws_NOdraws_first_time(rev_first_half_time)
NOdraws_draws_first_time(rev_first_half_time)

goal_NOgoal_first_time(rev_first_half_time)
NOgoal_goal_first_time(rev_first_half_time)

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1427&f_team=2705&chome=0&new_tid=1427'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Hibernian"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws_NOdraws(rev_full_time)
NOdraws_draws(rev_full_time)

odd_even(rev_full_time)
even_odd(rev_full_time)

under15_over15(rev_full_time)
over15_under15(rev_full_time)

under25_over25(rev_full_time)
over25_under25(rev_full_time)

both_noboth_score(rev_full_time)
noboth_both_score(rev_full_time)

draws_NOdraws_first_time(rev_first_half_time)
NOdraws_draws_first_time(rev_first_half_time)

goal_NOgoal_first_time(rev_first_half_time)
NOgoal_goal_first_time(rev_first_half_time)

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1427&f_team=2707&chome=0&new_tid=1427'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Kilmarnock"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws_NOdraws(rev_full_time)
NOdraws_draws(rev_full_time)

odd_even(rev_full_time)
even_odd(rev_full_time)

under15_over15(rev_full_time)
over15_under15(rev_full_time)

under25_over25(rev_full_time)
over25_under25(rev_full_time)

both_noboth_score(rev_full_time)
noboth_both_score(rev_full_time)

draws_NOdraws_first_time(rev_first_half_time)
NOdraws_draws_first_time(rev_first_half_time)

goal_NOgoal_first_time(rev_first_half_time)
NOgoal_goal_first_time(rev_first_half_time)

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1427&f_team=2712&chome=0&new_tid=1427'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Livingston"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws_NOdraws(rev_full_time)
NOdraws_draws(rev_full_time)

odd_even(rev_full_time)
even_odd(rev_full_time)

under15_over15(rev_full_time)
over15_under15(rev_full_time)

under25_over25(rev_full_time)
over25_under25(rev_full_time)

both_noboth_score(rev_full_time)
noboth_both_score(rev_full_time)

draws_NOdraws_first_time(rev_first_half_time)
NOdraws_draws_first_time(rev_first_half_time)

goal_NOgoal_first_time(rev_first_half_time)
NOgoal_goal_first_time(rev_first_half_time)

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1427&f_team=2709&chome=0&new_tid=1427'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Motherwell"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws_NOdraws(rev_full_time)
NOdraws_draws(rev_full_time)

odd_even(rev_full_time)
even_odd(rev_full_time)

under15_over15(rev_full_time)
over15_under15(rev_full_time)

under25_over25(rev_full_time)
over25_under25(rev_full_time)

both_noboth_score(rev_full_time)
noboth_both_score(rev_full_time)

draws_NOdraws_first_time(rev_first_half_time)
NOdraws_draws_first_time(rev_first_half_time)

goal_NOgoal_first_time(rev_first_half_time)
NOgoal_goal_first_time(rev_first_half_time)

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1427&f_team=2711&chome=0&new_tid=1427'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Rangers"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws_NOdraws(rev_full_time)
NOdraws_draws(rev_full_time)

odd_even(rev_full_time)
even_odd(rev_full_time)

under15_over15(rev_full_time)
over15_under15(rev_full_time)

under25_over25(rev_full_time)
over25_under25(rev_full_time)

both_noboth_score(rev_full_time)
noboth_both_score(rev_full_time)

draws_NOdraws_first_time(rev_first_half_time)
NOdraws_draws_first_time(rev_first_half_time)

goal_NOgoal_first_time(rev_first_half_time)
NOgoal_goal_first_time(rev_first_half_time)

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1427&f_team=2720&chome=0&new_tid=1427'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Ross_County"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws_NOdraws(rev_full_time)
NOdraws_draws(rev_full_time)

odd_even(rev_full_time)
even_odd(rev_full_time)

under15_over15(rev_full_time)
over15_under15(rev_full_time)

under25_over25(rev_full_time)
over25_under25(rev_full_time)

both_noboth_score(rev_full_time)
noboth_both_score(rev_full_time)

draws_NOdraws_first_time(rev_first_half_time)
NOdraws_draws_first_time(rev_first_half_time)

goal_NOgoal_first_time(rev_first_half_time)
NOgoal_goal_first_time(rev_first_half_time)

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1427&f_team=2725&chome=0&new_tid=1427'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "St_Johnstone"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws_NOdraws(rev_full_time)
NOdraws_draws(rev_full_time)

odd_even(rev_full_time)
even_odd(rev_full_time)

under15_over15(rev_full_time)
over15_under15(rev_full_time)

under25_over25(rev_full_time)
over25_under25(rev_full_time)

both_noboth_score(rev_full_time)
noboth_both_score(rev_full_time)

draws_NOdraws_first_time(rev_first_half_time)
NOdraws_draws_first_time(rev_first_half_time)

goal_NOgoal_first_time(rev_first_half_time)
NOgoal_goal_first_time(rev_first_half_time)

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1427&f_team=2715&chome=0&new_tid=1427'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "St_Mirren"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws_NOdraws(rev_full_time)
NOdraws_draws(rev_full_time)

odd_even(rev_full_time)
even_odd(rev_full_time)

under15_over15(rev_full_time)
over15_under15(rev_full_time)

under25_over25(rev_full_time)
over25_under25(rev_full_time)

both_noboth_score(rev_full_time)
noboth_both_score(rev_full_time)

draws_NOdraws_first_time(rev_first_half_time)
NOdraws_draws_first_time(rev_first_half_time)

goal_NOgoal_first_time(rev_first_half_time)
NOgoal_goal_first_time(rev_first_half_time)
