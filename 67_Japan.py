import requests
from bs4 import BeautifulSoup
import re
import datetime as dt

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

url = 'https://nb-bet.com/Teams/599-Avispa-Fukuoka-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

draw = 6
odd_even = 10
under_15 = 5
over_25 = 10
under_25 = 10
both_scores = 10
drw_frst_tm = 8
no_goal_frst_tm = 6

drw_NOdrw = 7
NOdrw_drw = 8
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
od_ev = 8
ev_od = 8

a = "Japan.txt"
champ = "Япония"
team = "Ависпа Фукуока"

def adding_team():
    c = "Japan"
    b = "Avispa_Fukuoka"
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
    new_file.close()


def draws(x):
    count = 0
    for i in x:
        if (i == '0 : 0 ' or i == '1 : 1 ' or i == '2 : 2 ' or i == '3 : 3 ' or i == '4 : 4 '
                or i == '5 : 5 ' or i == '6 : 6 ' or i == '7 : 7 '):
            count += 1
        else:
            break
    if count >= draw:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m ничей = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n draws = ' + b)
        new_file.close()


def odd(x):
    count = 0
    for i in x:
        if (i != '0 : 0 ' and i != '1 : 1 ' and i != '2 : 2 ' and i != '3 : 3 '
                and i != '4 : 4 ' and i != '5 : 5 ' and i != '6 : 6 ' and i != '7 : 7 '
                and i != '0 : 6 ' and i != '6 : 0 '
                and i != '1 : 5 ' and i != '5 : 1 ' and i != '1 : 7 ' and i != '7 : 1 '
                and i != '2 : 0 ' and i != '0 : 2 ' and i != '2 : 4 ' and i != '4 : 2 '
                and i != '2 : 6 ' and i != '6 : 2 '
                and i != '3 : 1 ' and i != '1 : 3 ' and i != '3 : 5 ' and i != '5 : 3 '
                and i != '4 : 6 ' and i != '6 : 4 ' and i != '4 : 0 ' and i != '0 : 4 '
                and i != '7 : 3 ' and i != '3 : 7 ' and i != '5 : 7 ' and i != '7 : 5 '
                and i != '8 : 2 ' and i != '2 : 8 '):
            count += 1
        else:
            break
    if count >= odd_even:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m не-чет = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n odd = ' + b)
        new_file.close()


def even(x):
    count = 0
    for i in x:
        if (i == '0 : 0 ' or i == '1 : 1 ' or i == '2 : 2 ' or i == '3 : 3 '
                or i == '4 : 4 ' or i == '5 : 5 ' or i == '6 : 6 ' or i == '7 : 7 '
                or i == '0 : 6 ' or i == '6 : 0 '
                or i == '1 : 5 ' or i == '5 : 1 ' or i == '1 : 7 ' or i == '7 : 1 '
                or i == '2 : 0 ' or i == '0 : 2 ' or i == '2 : 4 ' or i == '4 : 2 '
                or i == '2 : 6 ' or i == '6 : 2 '
                or i == '3 : 1 ' or i == '1 : 3 ' or i == '3 : 5 ' or i == '5 : 3 '
                or i == '4 : 6 ' or i == '6 : 4 ' or i == '4 : 0 ' or i == '0 : 4 '
                or i == '7 : 3 ' or i == '3 : 7 ' or i == '5 : 7 ' or i == '7 : 5 '
                or i == '8 : 2 ' or i == '2 : 8 '):
            count += 1
        else:
            break
    if count >= odd_even:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m чет = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n even = ' + b)
        new_file.close()


def under_1_5(x):
    count = 0
    for i in x:
        if i == '0 : 0 ' or i == '1 : 0 ' or i == '0 : 1 ':
            count += 1
        else:
            break
    if count >= under_15:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m мен 1.5 = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n under_1.5 = ' + b)
        new_file.close()


def over_2_5(x):
    count = 0
    for i in x:
        if (i != '0 : 0 ' and i != '1 : 1 ' and i != '1 : 0 '
                and i != '0 : 1 ' and i != '2 : 0 ' and i != '0 : 2 '):
            count += 1
        else:
            break
    if count >= over_25:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m бол 2.5 = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n over_2.5 = ' + b)
        new_file.close()


def under_2_5(x):
    count = 0
    for i in x:
        if (i == '0 : 0 ' or i == '1 : 1 ' or i == '1 : 0 '
                or i == '0 : 1 ' or i == '2 : 0 ' or i == '0 : 2 '):
            count += 1
        else:
            break
    if count >= under_25:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m мен 2.5 = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n under_2.5 = ' + b)
        new_file.close()


def both_score(x):
    count = 0
    for i in x:
        if (i != '0 : 0 ' and i != '1 : 0 ' and i != '0 : 1 ' and i != '2 : 0 '
                and i != '0 : 2 ' and i != '0 : 3 ' and i != '3 : 0 ' and i != '4 : 0 '
                and i != '0 : 4 ' and i != '0 : 5 ' and i != '5 : 0 ' and i != '0 : 6 '
                and i != '6 : 0 '):
            count += 1
        else:
            break
    if count >= both_scores:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m обе зибили = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n both_score = ' + b)
        new_file.close()


def both_no_score(x):
    count = 0
    for i in x:
        if (i == '0 : 0 ' or i == '1 : 0 ' or i == '0 : 1 ' or i == '2 : 0 ' or i == '0 : 2 '
                or i == '0 : 3 ' or i == '3 : 0 ' or i == '4 : 0 ' or i == '0 : 4 '
                or i == '0 : 5 ' or i == '5 : 0 ' or i == '0 : 6 ' or i == '6 : 0 '
                or i == '0 : 7 ' or i == '7 : 0 '):
            count += 1
        else:
            break
    if count >= both_scores:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m обе НЕ зибили = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n both_no_score = ' + b)
        new_file.close()


def draws_first_time(x):
    count = 0
    for i in x:
        if (i == '(0 : 0)' or i == '(1 : 1)' or i == '(2 : 2)' or i == '(3 : 3)' or i == '(4 : 4)'
                or i == '(5 : 5)'):
            count += 1
        else:
            break
    if count >= drw_frst_tm:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m ничьи 1-й тайм = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n draws_first_time = ' + b)
        new_file.close()


def no_goal_first_time(x):
    count = 0
    for i in x:
        if i == '(0 : 0)':
            count += 1
        else:
            break
    if count >= no_goal_frst_tm:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m 0:0  1-й тайм = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n no_goal_first_time = ' + b)
        new_file.close()


def Odd_Even(x):
    count = 0
    olimp = []
    for i in x:
        if (i != '0 : 0 ' and i != '1 : 1 ' and i != '2 : 2 ' and i != '3 : 3 ' and i != '4 : 4 '
                and i != '5 : 5 ' and i != '2 : 0 ' and i != '0 : 2 ' and i != '1 : 3 '
                and i != '3 : 1 ' and i != '4 : 2 ' and i != '2 : 4 ' and i != '3 : 5 '
                and i != '5 : 3 ' and i != '4 : 6 ' and i != '6 : 4 ' and i != '4 : 0 '
                and i != '0 : 4 ' and i != '1 : 5 ' and i != '5 : 1 ' and i != '2 : 6 '
                and i != '6 : 2 ' and i != '3 : 7 ' and i != '7 : 3 ' and i != '0 : 6 '
                and i != '6 : 0 ' and i != '1 : 7 ' and i != '7 : 1 ' and i != '2 : 8 '
                and i != '8 : 2 '):
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
    if count >= od_ev:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m НЕчет_чет = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n odd_even = ' + b)
        new_file.close()


def Even_Odd(x):
    count = 0
    olimp = []
    for i in x:
        if (i != '0 : 0 ' and i != '1 : 1 ' and i != '2 : 2 ' and i != '3 : 3 '
                and i != '4 : 4 ' and i != '5 : 5 ' and i != '2 : 0 ' and i != '0 : 2 '
                and i != '1 : 3 ' and i != '3 : 1 ' and i != '4 : 2 ' and i != '2 : 4 '
                and i != '3 : 5 ' and i != '5 : 3 ' and i != '4 : 6 ' and i != '6 : 4 '
                and i != '4 : 0 ' and i != '0 : 4 ' and i != '1 : 5 ' and i != '5 : 1 '
                and i != '2 : 6 ' and i != '6 : 2 ' and i != '3 : 7 ' and i != '7 : 3 '
                and i != '0 : 6 ' and i != '6 : 0 ' and i != '1 : 7 ' and i != '7 : 1 '
                and i != '2 : 8 ' and i != '8 : 2 '):
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
    if count >= ev_od:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m чет_НЕчет = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n even_odd = ' + b)
        new_file.close()


def draws_NOdraws(x):
    count = 0
    olimp = []
    for i in x:
        if i == '0 : 0 ' or i == '1 : 1 ' or i == '2 : 2 ' or i == '3 : 3 ' or i == '4 : 4 ' \
                or i == '5 : 5 ' or i == '6 : 6 ' or i == '7 : 7 ' or i == '8 : 8 ':
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
    if count >= drw_NOdrw:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m ничья_НЕничья = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n draws_NOdraws = ' + b)
        new_file.close()


def NOdraws_draws(x):
    count = 0
    olimp = []
    for i in x:
        if i == '0 : 0 ' or i == '1 : 1 ' or i == '2 : 2 ' or i == '3 : 3 ' \
                or i == '4 : 4 ' or i == '5 : 5 ' or i == '6 : 6 ' or i == '7 : 7 ':
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
    if count >= NOdrw_drw:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m НЕничья_ничья = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n NOdraws_draws = ' + b)
        new_file.close()


def under15_over15(x):
    count = 0
    olimp = []
    for i in x:
        if i == '0 : 0 ' or i == '1 : 0 ' or i == '0 : 1 ':
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
    if count >= und15_ovr15:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m мен_бол 1.5 = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n under_over 1.5 = ' + b)
        new_file.close()


def over15_under15(x):
    count = 0
    olimp = []
    for i in x:
        if i == '0 : 0 ' or i == '1 : 0 ' or i == '0 : 1 ':
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
    if count >= ovr15_und15:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m бол_мен 1.5 = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n over_under 1.5 = ' + b)
        new_file.close()


def under25_over25(x):
    count = 0
    olimp = []
    for i in x:
        if (i == '0 : 0 ' or i == '1 : 1 ' or i == '1 : 0 '
                or i == '0 : 1 ' or i == '2 : 0 ' or i == '0 : 2 '):
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
    if count >= und25_ovr25:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m мен_бол 2.5 = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n under_over 2.5 = ' + b)
        new_file.close()


def over25_under25(x):
    count = 0
    olimp = []
    for i in x:
        if (i == '0 : 0 ' or i == '1 : 1 ' or i == '1 : 0 '
                or i == '0 : 1 ' or i == '2 : 0 ' or i == '0 : 2 '):
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
    if count >= ovr25_und25:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m бол_мен 2.5 = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n over_under 2.5 = ' + b)
        new_file.close()


def both_noboth_score(x):
    count = 0
    olimp = []
    for i in x:
        if (i != '0 : 0 ' and i != '1 : 0 ' and i != '0 : 1 '
                and i != '2 : 0 ' and i != '0 : 2 ' and i != '0 : 3 '
                and i != '3 : 0 ' and i != '4 : 0 ' and i != '0 : 4 '
                and i != '0 : 5 ' and i != '5 : 0 ' and i != '0 : 6 '
                and i != '6 : 0 ' and i != '0 : 7 ' and i != '7 : 0 '
                and i != '0 : 8 ' and i != '8 : 0 '):
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
    if count >= both_noboth:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m обе_необе забили = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n both_noboth score = ' + b)
        new_file.close()


def noboth_both_score(x):
    count = 0
    olimp = []
    for i in x:
        if (i != '0 : 0 ' and i != '1 : 0 ' and i != '0 : 1 ' and i != '2 : 0 '
                and i != '0 : 2 ' and i != '0 : 3 ' and i != '3 : 0 '
                and i != '4 : 0 ' and i != '0 : 4 ' and i != '0 : 5 '
                and i != '5 : 0 ' and i != '0 : 6 ' and i != '6 : 0 '
                and i != '0 : 7 ' and i != '7 : 0 '):
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
    if count >= noboth_both:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m необе_обе забили = {count} \033[0m')
        print(' ')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n noboth_both score = ' + b)
        new_file.close()


def draws_NOdraws_first_time(x):
    count = 0
    olimp = []
    for i in x:
        if i == '(0 : 0)' or i == '(1 : 1)' or i == '(2 : 2)' or i == '(3 : 3)' \
                or i == '(4 : 4)' or i == '(5 : 5)':
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
    if count >= drw_NOdrw_ft:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m ничья_НЕничья 1-й тайм = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n draws_NOdraws 1st time = ' + b)
        new_file.close()


def NOdraws_draws_first_time(x):
    count = 0
    olimp = []
    for i in x:
        if i == '(0 : 0)' or i == '(1 : 1)' or i == '(2 : 2)' or i == '(3 : 3)'\
                or i == '(4 : 4)' or i == '(5 : 5)' or i == '(6 : 6)':
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
    if count >= NOdrw_drw_ft:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m НЕничья_ничья 1-й тайм = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n NOdraws_draws 1st time = ' + b)
        new_file.close()


def goal_NOgoal_first_time(x):
    count = 0
    olimp = []
    for i in x:
        if i != '(0 : 0)':
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
    if count >= goal_NOgoal_ft:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m гол-НЕгол 1-й тайм = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n goal_NOgoal 1st time = ' + b)
        new_file.close()


def NOgoal_goal_first_time(x):
    count = 0
    olimp = []
    for i in x:
        if i != '(0 : 0)':
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
    if count >= NOgoal_goal_ft:
        print(f'\033[1;34m{next_game_3}\033[1;35m ({next_games_1})   \033[1;36m {champ:10} '
              f'\033[1;33m {team :15} \033[1;31m НЕгол_гол 1-й тайм = {count} \033[0m')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n NOgoal_goal 1st time = ' + b)
        new_file.close()


clean_file()
create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/1794-Sereso-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Серезо Осака"

def adding_team():
    b = "Cerezo_Osaka"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/1795-Khokkaydo-Konsadole-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass


team = "Консадоле Саппоро "

def adding_team():
    b = "Consodale_Sapporo"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/597-Tokio-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "ФК Токио "

def adding_team():
    b = "FC_Tokyo"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/2650-Iokogama-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Йокогама ФК"

def adding_team():
    b = "FC_Yokohama"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/585-Gamba-Osaka-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Гамба Осака"

def adding_team():
    b = "Gamba_Osaka"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/589-Kasima-Antlers-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Касима Антлерс"

def adding_team():
    b = "Kashima_Antlers"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/588-Kasiva-Reysol-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Касива Рейсол"

def adding_team():
    b = "Kashiwa_Reysol"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/587-Kavasaki-Frontale-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Кавасаки Фронтале"

def adding_team():
    b = "Kavasaki_Frontale"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/592-Nagoya-Grampus-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Нагоя Грампус"

def adding_team():
    b = "Nagoya_Grampus"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/2645-Oita-Trinita-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Оита Тринита"

def adding_team():
    b = "Oita_Trinita"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/593-Sagan-Tosu-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Саган Тосу"

def adding_team():
    b = "Sagan_Tosu"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/596-Simidzu-S-Pals-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Шимицу С-Пульс"

def adding_team():
    b = "Shimizu_S_Puls"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/595-Syonan-Belmare-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Шонан Беллмар"

def adding_team():
    b = "Shonan_Bellmare"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/594-Sanfrechche-Khirosima-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Санфресс Хиросима"

def adding_team():
    b = "Sunfress_Hiroshima"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/2641-Tokusima-Vortis-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

nnext_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Токусима Вортис"

def adding_team():
    b = "Tokushima_Vortis"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/598-Urava-Red-Daymonds-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Урава Ред Даймондс"

def adding_team():
    b = "Urawa_Red-Daymonds"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/583-Vegalta-Senday-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Вегалта Сендай"

def adding_team():
    b = "Vegalta_Sendai"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/584-Vissel-Kobe-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Виссел Кобе"

def adding_team():
    b = "Vissel_Kobe"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)

url = 'https://nb-bet.com/Teams/586-Iokogama-F-Marinos-statistika-komandi'

r = requests.get(url, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)

nbbet = soup.select(".a-dotted-hover")
one = ("...".join((str(i) for i in nbbet)))
two = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s[(-][0-9]{1}\s[:-]\s[0-9]{1}[\)-]', one)
three = (" ".join((str(i) for i in two)))

full_time = re.findall(r'[0-9]{1}\s[:-]\s[0-9]{1}\s', three)
first_half_time = re.findall(r'[(][0-9]{1}\s[:]\s[0-9]{1}[)]', three)

next_game = soup.select(".first-td-content-results-auto")
next_game_1 = ("...".join((str(i) for i in next_game)))
next_game_1_1 = next_game_1.replace(' ', '')

next_game_2 = re.findall(r'\d{2}[.]\d{2}[.]\d{2}', next_game_1_1)

next_games = next_game_2[10:]
next_games_1 = len(next_games)

date = []
y = '.20'

if len(next_game_2) >= 6:
    b = next_game_2[5]
    bb = b[:6 - 1] + y + b[6:]
    date.append(bb)
else:
    pass

if len(next_game_2) >= 7:
    c = next_game_2[6]
    cc = c[:6 - 1] + y + c[6:]
    date.append(cc)
else:
    pass

if len(next_game_2) >= 8:
    d = next_game_2[7]
    dd = d[:6 - 1] + y + d[6:]
    date.append(dd)
else:
    pass

if len(next_game_2) >= 9:
    e = next_game_2[8]
    ee = e[:6 - 1] + y + e[6:]
    date.append(ee)
else:
    pass

if len(next_game_2) >= 10:
    f = next_game_2[9]
    ff = f[:6 - 1] + y + f[6:]
    date.append(ff)
else:
    pass

if len(next_game_2) >= 11:
    g = next_game_2[10]
    gg = g[:6 - 1] + y + g[6:]
    date.append(gg)
else:
    pass

if len(next_game_2) >= 12:
    h = next_game_2[11]
    hh = h[:6 - 1] + y + h[6:]
    date.append(hh)
else:
    pass

if len(next_game_2) >= 13:
    j = next_game_2[12]
    jj = j[:6 - 1] + y + j[6:]
    date.append(jj)
else:
    pass

if len(next_game_2) >= 14:
    k = next_game_2[13]
    kk = k[:6 - 1] + y + k[6:]
    date.append(kk)
else:
    pass

if len(next_game_2) >= 15:
    l = next_game_2[14]
    ll = l[:6 - 1] + y + l[6:]
    date.append(ll)
else:
    pass

if len(next_game_2) >= 16:
    m = next_game_2[15]
    mm = m[:6 - 1] + y + m[6:]
    date.append(mm)
else:
    pass

if len(next_game_2) >= 17:
    n = next_game_2[16]
    nn = n[:6 - 1] + y + n[6:]
    date.append(nn)
else:
    pass

if len(next_game_2) >= 18:
    o = next_game_2[17]
    oo = o[:6 - 1] + y + o[6:]
    date.append(oo)
else:
    pass

if len(next_game_2) >= 19:
    p = next_game_2[18]
    pp = p[:6 - 1] + y + p[6:]
    date.append(pp)
else:
    pass

if len(next_game_2) >= 20:
    q = next_game_2[19]
    qq = q[:6 - 1] + y + q[6:]
    date.append(qq)
else:
    pass

if len(next_game_2) >= 21:
    r = next_game_2[20]
    rr = r[:6 - 1] + y + r[6:]
    date.append(rr)
else:
    pass

if len(date) >= 1:
    date_0 = dt.datetime.strptime(date[0], '%d.%m.%Y')
    if len(date) >= 2:
        date_1 = dt.datetime.strptime(date[1], '%d.%m.%Y')
        if len(date) >= 3:
            date_2 = dt.datetime.strptime(date[2], '%d.%m.%Y')
            if len(date) >= 4:
                date_3 = dt.datetime.strptime(date[3], '%d.%m.%Y')
                if len(date) >= 5:
                    date_4 = dt.datetime.strptime(date[4], '%d.%m.%Y')
                    if len(date) >= 6:
                        date_5 = dt.datetime.strptime(date[5], '%d.%m.%Y')
                        if len(date) >= 7:
                            date_6 = dt.datetime.strptime(date[6], '%d.%m.%Y')
                            if len(date) >= 8:
                                date_7 = dt.datetime.strptime(date[7], '%d.%m.%Y')
                                if len(date) >= 9:
                                    date_8 = dt.datetime.strptime(date[8], '%d.%m.%Y')
                                    if len(date) >= 10:
                                        date_9 = dt.datetime.strptime(date[9], '%d.%m.%Y')
                                        if len(date) >= 11:
                                            date_10 = dt.datetime.strptime(date[10], '%d.%m.%Y')
                                            if len(date) >= 12:
                                                date_11 = dt.datetime.strptime(date[11], '%d.%m.%Y')
                                                if len(date) >= 13:
                                                    date_12 = dt.datetime.strptime(date[12], '%d.%m.%Y')
                                                    if len(date) >= 14:
                                                        date_13 = dt.datetime.strptime(date[13], '%d.%m.%Y')
                                                        if len(date) >= 15:
                                                            date_14 = dt.datetime.strptime(date[14], '%d.%m.%Y')
                                                            if len(date) >= 16:
                                                                date_15 = dt.datetime.strptime(date[15], '%d.%m.%Y')


if date_0 < date_1:
    next_game_3 = cc
else:
    if date_1 < date_2:
        next_game_3 = dd
    else:
        if date_2 < date_3:
            next_game_3 = ee
        else:
            if date_3 < date_4:
                next_game_3 = ff
            else:
                if date_4 < date_5:
                    next_game_3 = gg
                else:
                    if date_5 < date_6:
                        next_game_3 = hh
                    else:
                        if date_6 < date_7:
                            next_game_3 = jj
                        else:
                            if date_7 < date_8:
                                next_game_3 = kk
                            else:
                                if date_8 < date_9:
                                    next_game_3 = ll
                                else:
                                    if date_9 < date_10:
                                        next_game_3 = mm
                                    else:
                                        if date_10 < date_11:
                                            next_game_3 = nn
                                        else:
                                            if date_11 < date_12:
                                                next_game_3 = oo
                                            else:
                                                if date_12 < date_13:
                                                    next_game_3 = pp
                                                else:
                                                    if date_13 < date_14:
                                                        next_game_3 = qq
                                                    else:
                                                        if date_14 < date_15:
                                                            next_game_3 = rr
                                                        else:
                                                            pass

team = "Йокогама Ф.Маринос"

def adding_team():
    b = "Yokohama_F-Marinos"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


create_file()
adding_team()

draws(full_time)
odd(full_time)
even(full_time)
under_1_5(full_time)
over_2_5(full_time)
under_2_5(full_time)
both_score(full_time)
both_no_score(full_time)
draws_first_time(first_half_time)
no_goal_first_time(first_half_time)

Odd_Even(full_time)
Even_Odd(full_time)
draws_NOdraws(full_time)
NOdraws_draws(full_time)
under15_over15(full_time)
over15_under15(full_time)
under25_over25(full_time)
over25_under25(full_time)
both_noboth_score(full_time)
noboth_both_score(full_time)
draws_NOdraws_first_time(first_half_time)
NOdraws_draws_first_time(first_half_time)
goal_NOgoal_first_time(first_half_time)
NOgoal_goal_first_time(first_half_time)
