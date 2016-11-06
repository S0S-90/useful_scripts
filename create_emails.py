import csv

def make_lower(string):    
    return string[0].lower() + string[1:]

def umlaute_ersetzen(string):
    neu = ""
    for i in string:
        if ord(i) == 228:
            neu = neu + "ae"
        elif ord(i) == 246:
            neu = neu + "oe"
        elif ord(i) == 252:
            neu = neu + "ue"
        elif ord(i) == 223:
            neu = neu + "ss"
        else:
            neu = neu + i
    return neu

with open("namen.csv") as namen:  # Datei, in der jede Zeile so aussieht: Vorname, Nachname
    text = csv.reader(namen)
    namelist = []
    for line in text:
        namelist.append(line)

def main():
    namelist_neu = []
    for name in namelist:
        vorname = umlaute_ersetzen(make_lower(name[0]))
        nachname = umlaute_ersetzen(make_lower(name[1]))
        namelist_neu.append([vorname, nachname])

    mails = []
    for n in namelist_neu:
        mails.append("{}.{}@stud-mail.uni-wuerzburg.de".format(n[0], n[1]))

    with open("mails.csv", "w") as mail_file:  # kann im Thunderbird-Adressbuch mit Extras -> Importieren -> ... importiert werden
        mail_file.write("E-Mail-Adressen\n")
        for mail in mails:
            mail_file.write(",,,," + mail + "\n")

if __name__ == "__main__":
    main()
