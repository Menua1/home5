#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#a) Добавьте игру против бота
#b) Подумайте как наделить бота 'интеллектом'
from random import randint as ri
total_swit=150
take_swit=0#берет игрок 
player_swet=0# взял игрок
bot_swet=0#ВЗЯЛ БОТ 


def start():
    print('По итогам жеребьевки выбарают того кто первый будет ходить!\nКаждый игрок может брать от 1 до 28 конфет.\nПобеждает тот кто заберет последние конфеты!')
    OnePlay()

     
def OnePlay():
    rnd_num=ri(1,2)
    if rnd_num==1:
        player_tern()
    else:
        bot_hot()

def player_tern():
    global total_swit
    global take_swit
    global player_swet
    print(f'Ваш ход, на столе сейчас {total_swit} конфет.')
    take_swit=int(input('Сколько конфет вы хотите взять? '))
    while take_swit > 28 or take_swit < 1 or take_swit > total_swit:
        take_swit=int(input('Вы выбрали слишком много конфет,возьмите снова. '))
    total_swit-=take_swit
    player_swet+=take_swit
    if total_swit > 0:
        bot_hot()
    else:
        print('Вы победили!!!')
def bot_hot():
    global total_swit
    global take_swit
    global bot_swet
    take_swit= total_swit%29 if total_swit%29!=0 else ri(1,28)
    total_swit-=take_swit
    bot_swet+=take_swit
    print(f'Бот взял {take_swit} на столе осталось {total_swit} конфет.')
    if total_swit > 0:
        player_tern()
    else:
        print('Бот победил!!!')



