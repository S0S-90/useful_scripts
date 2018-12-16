### program to find given words in a crossword puzzle (given as csv file)
### diagonals start counting in the lower left and the upper left corner

import csv

FILENAME = "MedTrix_68.csv"
WORDS = ["ARTERIE","PALMAR","NIBP","TRANS","LMA","SPRITZE","VENE","ARZT","ZVK",
         "ITN","NARKOSE","OP","ZUGANG","PULS","TUBUS","UVULA","ANATOMIE","MASKE",
         "SCHERE","FLEXUELE","SHALDON","HERZ","NADEL","SPO2","LARYNX","JUGULARIS"]


def read_in_crossword(filename):
    crossword = []
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            crossword.append(row)
    return crossword


def print_crossword(cw):
    for line in cw:
        niceline = ""
        for column in line:
            niceline += " "+column.upper()+" "
        print niceline


def search_line_for_word(line,word,where,number):
    """takes a 'line' (can also be column or diagonal) as list of characters and looks for word in it
    @param where: string that tells you what kind the 'line' is of
    @param number: number of the 'line'"""
    
    for i in range(len(line)-len(word)):
        if "".join(line[i:i+len(word)]).upper() == word:
            print "found ",word," in ",where,number+1," position: ",i+1
    line.reverse()
    for i in range(len(line)-len(word)):
        if "".join(line[i:i+len(word)]).upper() == word:
            print "found ",word," in ",where,number+1," position: ",i+1,"reverse"
    line.reverse()  # after that line has its original order again
   


def search_lines(cw,words):
    for i,line in enumerate(cw):
        for w in words:
            search_line_for_word(line,w,"line",i)


def search_columns(cw,words):
    columns = []
    for i, c in enumerate(cw[0]):
        column = []
        for j,l in enumerate(cw):
            column.append(l[i])
        columns.append(column)

    for i,c in enumerate(columns):
        for w in words:
            search_line_for_word(c,w,"column",i)


def get_diags_from_up_left_to_down_right(cw):
    diags = []
    i = 0
    while True:
        diag = []
        j = 0
        while i+j < len(cw) and j < len(cw[0]):
            diag.append(cw[i+j][j])
            j +=1
        diags.append(diag)
        if len(diag) == 1:
            break
        i+=1
    diags.reverse()
    i = 1
    while True:
        diag = []
        j = 0
        while j < len(cw) and i+j < len(cw[0]):
            diag.append(cw[j][i+j])
            j +=1
        diags.append(diag)
        if len(diag) == 1:
            break
        i+=1
    return diags


def get_diags_from_up_right_to_down_left(cw):
    diags = []
    total = 0
    while total < len(cw):
        diag = []
        i = 0
        j = total
        while j >= 0:
            diag.append(cw[i][j])
            i = i+1
            j = j-1
        diags.append(diag)
        total += 1
    while True:
        diag = []
        i = 0
        j = total
        if j >= len(cw[0]):
            break
        while i < len(cw):
            diag.append(cw[i][j])
            i = i+1
            j = j-1
        diags.append(diag)
        total += 1
    counter = 1
    total -= 1
    while True:
        diag = []
        i = counter
        j = total
        while i < len(cw):
            diag.append(cw[i][j])
            i = i+1
            j = j-1
        diags.append(diag)
        if len(diag) == 1:
            break
        counter += 1
    return diags


def search_diagonals(cw,words):
    diags = get_diags_from_up_left_to_down_right(cw)
    for i,d in enumerate(diags):
        for w in words:
            if len(w) <= len(d):
                search_line_for_word(d,w,"diag_up_left_to_down_right",i)
        
    diags = get_diags_from_up_right_to_down_left(cw)
    for i,d in enumerate(diags):
        for w in words:
            if len(w) <= len(d):
                search_line_for_word(d,w,"diag_up_right_to_down_left",i)


def search_for_words(cw, words):
    search_lines(cw,words)
    search_columns(cw,words)
    search_diagonals(cw,words)


if __name__ == "__main__":
    crossword = read_in_crossword(FILENAME)
    print_crossword(crossword)
    search_for_words(crossword,WORDS)
