import pyautogui as pg
txt = open('resources/animals.txt','r')
a= "You are a "
for i in txt:
    pg.write(a+''+i)
 




