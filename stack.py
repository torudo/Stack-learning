from random import randint
import time
import stack_arguments
import sys
from timeit import default_timer as timer
import json
import csv
from datetime import date

# if len(sys.argv)<2:
#   print("Give me a File to plot!")
#   exit()
# file = sys.argv[1]


#Programm starten ohne argumente: Abfrage
# Stackbereich
# anzahl abfragungen
# stacknummern / Karten

def ask_for_card(i,start,end,fehler,points,counter):
    while(i > 0):
         random_nummer = randint(int(start),int(end))
         print("Tell me Card at", str(random_nummer), "and it is:")
         #print(stack_arr[random_nummer-1])
         antwort = input()
         if(antwort == stack_arr[random_nummer-1]):
             print('right')
             points += 1
         elif(antwort == "q" or antwort == "Q"):
             break
         else:
             #print('Anwser is:', stack_arr[random_nummer-1])
             print("Wrong!")
             fehler.append(random_nummer)
             fehler.append(stack_arr[random_nummer-1])
         i -= 1
         counter += 1
    return counter, points

def ask_for_number(i,start,end,fehler,points,counter):
    while(i > 0):
         random_nummer = randint(int(start),int(end))
         print("Tell me Position from", stack_arr[random_nummer-1], "and it is:")
         #print(stack_arr[random_nummer-1])
         antwort = input()
         if(antwort == str(random_nummer)):
             print('right')
             points += 1
         elif(antwort == "q" or antwort == "Q"):
             break
         else:
             #print('Anwser is:', str(random_nummer))
             print("Wrong!")
             fehler.append(random_nummer)
             fehler.append(stack_arr[random_nummer-1])
         i -= 1
         counter += 1
    return counter, points

def ask_for_both(i,start,end,fehler,points,counter):
    while(i > 0):
         random_nummer_case = randint(1,2)
         #print(random_nummer_case)
         random_nummer = randint(int(start),int(end))
         if (random_nummer_case == 1):
            print("Tell me Card at", str(random_nummer), "and it is:")
            #print(stack_arr[random_nummer-1])
            antwort = input()
            if(antwort == stack_arr[random_nummer-1]):
                print('right')
                points += 1
            elif(antwort == "q" or antwort == "Q"):
                break
            else:
                #print('Anwser is:', stack_arr[random_nummer-1])
                print("Wrong!")
                fehler.append(random_nummer)
                fehler.append(stack_arr[random_nummer-1])
         else:
             print("Tell me Position from", stack_arr[random_nummer-1], "and it is:")
             #print(stack_arr[random_nummer-1])
             antwort = input()
             if(antwort == str(random_nummer)):
                 print('right')
                 points += 1
             elif(antwort == "q" or antwort == "Q"):
                 break
             else:
                 #print('Anwser is:', str(random_nummer))
                 print("Wrong!")
                 fehler.append(random_nummer)
                 fehler.append(stack_arr[random_nummer-1])
         i -= 1
         counter += 1
    return counter, points

#Stack
stack_arr = ['Kreuz 4', 'Herz 2', 'Karo 7', 'Kreuz 3', 'Herz 4', 'Karo 6',
            'Pik A', 'Herz 5', 'Pik 9','Pik 2', 'Herz D', 'Karo 3', 'Kreuz D',
            'Herz 8', 'Pik 6', 'Pik 5', 'Herz 9','Kreuz K','Karo 2', 'Herz B',
            'Pik 3', 'Pik 8','Herz 6', 'Kreuz 10', 'Karo 5', 'Karo K',
            'Kreuz 2', 'Herz 3', 'Karo 8', 'Kreuz 5', 'Pik K', 'Karo B',
            'Kreuz 8', 'Pik 10', 'Herz K', 'Kreuz B', 'Pik 7', 'Herz 10',
            'Karo Ass', 'Pik 4', 'Herz 7', 'Karo 4', 'Kreuz A', 'Kreuz 9',
            'Pik B', 'Karo D', 'Kreuz 7', 'Pik D','Karo 10', 'Kreuz 6',
            'Herz A', 'Karo 9'
            ]

#startparameter
mode_in = "c"
start = 1
end = len(stack_arr)
i = 3
points = 0
counter = 0


#einstellungen
print('Hi! Cards (c) or Numbers (n), if empty, both!')
mode_in = input()

print('give me the the part of stack. If empty, we take all')
start = input('start: ')
if (start == ''):
    start = 1

end = input('end: ')
if (end == ''):
    end = len(stack_arr)

if (int(start) - int(end) > 0):
    print("End is bigger than start, I switch it ;)")
    start, end = end, start
print("I'll ask from",start, "to", end)

print('How many turns do you want to play?')
while True:
    number_of_questions = input()
    if (number_of_questions.isdigit()):
        break
    elif(number_of_questions == ''):
        print("We will take 5!")
        number_of_questions = 5
        break
    else:
        print("This was not a number! Try again!")
i = int(number_of_questions)

print("Ready ?")

print("Lets go!")

#timer und abfrage startet:
start = timer()
fehler = []

if (mode_in == "c"):
    counter, points = ask_for_card(i,start,end,fehler,points,counter)
elif(mode_in == "n"):
    counter, points = ask_for_number(i,start,end,fehler,points,counter)
else:
    counter, points = ask_for_both(i,start,end,fehler,points,counter)

end = timer()
#auswertung:
print("")
print("Results:")
print("###################################################")
print("##   You got", str(points), "/", str(counter), "right \t                ##")
print("##   and you needed %d seconds                    ##" %(end - start))
print("##    -----------------                          ##")
print("##  Here are your mistakes                       ##")
for j in range(0,len(fehler),2):
    print("##",fehler[j], fehler[j+1], "\t                                 ##")
    print("##                                               ##")
print("###################################################")

date_today = str(date.today()).split("-")
#print(date_today)

filename = 'data_stack.csv'

with open(filename, 'a',newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(date_today + [counter] + [points] + fehler)
#    csv_writer.writerow([])
#    csv_writer.writerow([])
#    csv_writer.writerow([date_today])

    #json.dump((points, counter, len(fehler)/2, fehler), f_obj)

# with open(filename) as f_obj:
#     numbers = json.load(f_obj)
