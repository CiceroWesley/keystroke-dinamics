from pynput import keyboard
from os.path import getsize
import time

def keystroke(name):
    timeOnPress = []
    timeOnRelease = []
    timeOnPressKeys = []
    timeOnReleaseKeys = []
    password = 'roberto'
    f = open('data.csv','a')

    def on_press(key):
        timeKeyP = time.time()
        timeOnPress.append(timeKeyP)
        timeOnPressKeys.append(key)
        try:
            print('alphanumeric key {0} pressed'.format(key.char))
        except AttributeError:
            print('special key {0} pressed'.format(key))

    def on_release(key):
        timeKeyR = time.time()
        timeOnRelease.append(timeKeyR)
        timeOnReleaseKeys.append(key)
        print('{0} released'.format(key))
        if key == keyboard.Key.enter:
            # Stop listener
            return False

    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    # print("RECOMECA AQUI")
    
    #verificação da senha
    # print(timeOnPressKeys[0].char)
    # print(type(password))

    keys = ''
    for i in range(len(timeOnPressKeys) - 1):
        keys += timeOnPressKeys[i].char
        
    wrong = False
    # for i in range(len(timeOnPressKeys) - 1):
    #     if(timeOnPressKeys[i].char == password[i]):
    #         continue
    #     else:
    #         wrong = True

    if(password != keys):
        wrong = True

    if(wrong):
        print('A senha está incorreta')
        return wrong
    
    # print(password)
    # print(timeOnPressKeys)
        
    timeHoldDD=[]
    #armazenando tempo entre apertar a tecla e soltar
    for i in range(len(timeOnPress)):
        timeHoldDD.append(timeOnRelease[i] - timeOnPress[i])

    timeDD = []
    #salvando tempo entre apertos de teclas
    # a tecla enter não é considerada
    for i in range(len(timeOnPress)-2):
        #print(i)
        #print(timeOnPressKeys[i+1],timeOnPressKeys[i])
        timeDD.append(timeOnPress[i+1]-timeOnPress[i])

    #print(timeDD)
    #removendo hold time da tecla enter
    timeHoldDD.pop()
    #inserindo tempo entre apertos de teclas
    for i in range(len(timeDD)):
        timeHoldDD.append(timeDD[i])
    
    #print(timeHoldDD)  
    #arquivo vázio?
    if(getsize('data.csv') == 0):
        #poderia fazer isso pelo password.
        f.write('Usuario,r_H,o_H,b_H,e_H,r_H,t_H,o_H,or_DD,bo_DD,eb_DD,re_DD,tr_DD,ot_DD')
        f.write('\n')
    # print('passou IF')
    # if(getsize('data.csv') != 0):
    f.write(name + ',')

    sizeTimeHoldDD = len(timeHoldDD)
    for i in range(sizeTimeHoldDD):
        if(i == sizeTimeHoldDD-1):
            f.write(str(timeHoldDD[i]))
        else:
            f.write(str(timeHoldDD[i])+ ',')

    f.write('\n')
    f.close()

    #print(timeHoldDD)
    print(timeOnPressKeys)
    #print(timeOnReleaseKeys)



def main():
    #recebendo o nome do usuário e definindo a quantidade de digitações
    numberTimes = 3
    name = input("Insira seu nome: ")
    name = name.capitalize()
    time.sleep(0.5)
    print("Digite o nome \'roberto\' "+ str(numberTimes) +" vezes e depois aperte enter")
    # for i in range(numberTimes):
    #     print("{}° digitação:".format(i))
    #     error = keystroke(name)
    #     if(error):
    #         i = i - 1
    #         print("dentro"+ str(i))
    i = 0
    while(i < numberTimes):
        print("{}° digitação:".format(i))
        error = keystroke(name)
        i = i + 1
        if(error):
            i = i - 1
            print("Digite novamente.")
        # else:
        #     i = i + 1

        

if __name__ == '__main__':
    main()
