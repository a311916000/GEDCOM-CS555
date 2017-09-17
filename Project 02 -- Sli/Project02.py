def readGEDCOM(file):
    ln = 1
    GEDCOM = open(file)
    for line in GEDCOM.readlines():
        print("--> "+line)
        parse(ln, line)    
        ln += 1

    return 
    
def parse(ln, line):

    p = ""
    level = 0;
    tag = ""
    valid = ''
    arguments = ""
    supportedtags= ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]
    
    tail = line.strip()
    if tail == '':
        print("ERROR, Empty line")
        return

    #get level
    [head, tail] = tail.split(' ', 1)
    level = int(head)
    if level < 0:
        print("ERROR, Line must start with a positive int")
        return

    #check for id if it is indi aor fam tag
    try:
        [head, tail] = tail.split(' ', 1)
        if head == '':
            print("ERROR, Incomplete line")
            return
        elif head[0] == '@':
            if head[len(head)-1] == '@':
                p = head
                [head, tail] = tail.split(' ', 1)
                tag = head
        tag = head
    except ValueError:
        [head, tail] = [tail, '']
        tag = head

    if tag in supportedtags:
        valid = 'Y'
    else:
        valid = 'N'

    if p != "":
        arguments = p
    else:
        arguments = tail
    print("<-- "+str(level) +"|" + tag + "|" + valid + "|" + arguments)
    return
              
