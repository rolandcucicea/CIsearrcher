#this bit just sorts and formats the SO#'s from the dashboard in searchable form
#IMPORTANT: save them in "/SO.txt"
with open("SO.txt", 'r') as rf:
    with open("SO_copy.txt", 'w') as wf:
        for line in rf:
            for char_position in range( len(line) ):
                if line[char_position] == " ":
                    start = char_position    
            if len(line[start+1:-1]) <= 7:
                wf.write(line[start+1:])

while True:
    print("")
    lookfor  = int(input(" Please scan SO: "))
    so = int(str(lookfor)[-6:])
    flag = False
    with open("SO_copy.txt", 'r') as rf:
        for line in rf:
            if (int(line) == so):
                with open("CI_released", 'r') as rci:
                    for text in rci:
                        print(text, end="")
                flag = True
        if flag == False:
                with open("noCI", 'r') as rnoci:
                    for char in rnoci:
                        print(char,end="")
    if so == 0:
        break


