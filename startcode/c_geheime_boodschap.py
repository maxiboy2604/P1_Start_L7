geheime_boodschap = (19, 8, 9, 3, 26, 21, 14, 14, 17, 26, 3, 8, 2, 19, 8, 14, 13, 0, 17, 8, 4, 18, 27)
alfabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '!', '.', '?')


bericht = ""


for i in geheime_boodschap:
        bericht += alfabet[i]
print("Ontcijferde geheime boodschap:")
print(bericht)
