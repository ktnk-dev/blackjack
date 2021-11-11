### Настройки
allowed = 21                    # максимальное количество очков
take = 2                        # сколько взять чисел в начале игры (минимум 1)
nums = [1,2,3,4,5,6,7,8,9,10]   # разрешенные цифры
deco = {                        # декорации для текста
    "space": "──────",
    "start": "────┬─",
    "score":     "│",
    "end":   "────┴─"
}

### Функции
from random import randint as r
def draw():
    global nums
    return nums[r(0,len(nums)-1)]       # выбор рандомного числа из списка разрешенных

def show(list):
    res = ""
    for i in list: res+=f" {i}"
    return res[1:]                      # так как первый символ является пробелом, то мы просто убираем его

def sum(list):
    res = 0
    for i in list: res+=i
    return res

def text(list):
    global deco
    spacer = " "*(3-len(str(sum(scores))))                              # сколько нужно поставить пробелов, чтобы выровнять кол-во очков и декорацию по одной линии
    return  f"{spacer}{sum(scores)} {deco['score']} {show(scores)} "    # возрат кол-во очков, декорации и то, какие числа уже были сгенерированны

def clear(text=""): print("\n"*10000+text)        


### Программа
scores = [draw() for i in range(0,take)]    # сколько сгенерировать цифр в начале игры (take)
print(f"Нажмите ENTER чтобы сгенерировать число. Чтобы завершить игру введите любой текст\n\n{deco['start']} Ваши очки {deco['space']}")
while True: 
    temp = draw()       
    if input(text(scores)) == "": 
        scores.append(temp)
        #clear(f"{deco['start']} Ваши очки {deco['space']}")  # Что-бы было красиво)

        ### Проверка если пользователь победил или проиграл
        if sum(scores) > allowed: exit(f"{text(scores)} \n{deco['end']} Вы поиграли, вы набрали более {allowed}")
        elif sum(scores) == allowed: exit(f"{text(scores)}\n{deco['end']} Вы победили")

    ### Если пользователь ввел какой либо символ, то игра завершается
    else: exit(f"{deco['end']} Вы набрали {sum(scores)} очков | следующая цифра была бы {temp}")