import numpy as np

#tablica procesów
tab = np.array([], type(int))

processNumber = 100 #liczba szystkich procesów

#czas przyjścia procesu:
timeL = 10   #wartość minimalna
timeH = 20 #wartość maxymalna

#czas wykonania procesu
lenL = 4      #wartość minimalna
lenH = 5      #wartość max

#ustaienia losoych wartość z wyżej wymienionego zakresu dla procesów
for i in range(0, processNumber):
    #czas przyjścia:
    timeR = np.random.randint(low = timeL, high = timeH)
    #czas wykonania
    lengthR = np.random.randint(low = lenL, high = lenH)
    helper = np.array([timeR, lengthR])
    #tab = np.append(tab, helper)
    #dodanie indexu do tablicy
    tab = np.append(tab, [1])
    #ustawienie artości tablicy
    tab[i] = helper

print(tab)

def sort(tab, id):
    for i in range(len(tab)):
        for j in range(len(tab)):
            if(tab[i][id]<tab[j][id]):
                k = tab[j][id]
                tab[j][id] = tab[i][id]
                tab[i][id] = k

def FCFS(tab):
    print("--- FCFS ---")
    print(tab)

    #czas procesora:
    time = 0

    #id ostatniego procesu:
    last = -1

    #id aktualnego procesu
    stos = -1

    #czas wykonyania procesu
    stosTime = 0

    #tablica czasów oczekiwania dla poszczególnych procesów
    timeSum = np.array([], type(int))

    while(1):
        print("Current FCFS time is: ", time)

        #dodanie pierwszego elementu na stos
        if(stos == -1 and last == -1 and tab[0][0] <= time):
            stos = 0

        #dodanie kolejnego elementu na stos
        if(stos == -1 and last != -1):
            if(time >= tab[last+1][0]):
                stos = last+1

        #wykonanie procesu
        if(stos != -1):
            stosTime+=1
            print("Processor exec process: ", tab[stos])

            #koniec wykonania procesu
            if(stosTime == tab[stos][1]):
                #ustalenie czasu oczekiwania:
                timeSum = np.append(timeSum, [time + 1 - tab[stos][0] - tab[stos][1]])
                last = stos
                stos = -1
                stosTime = 0

                #koniec algorytmu
                if(last == processNumber - 1):
                    break
        else:
            print("processor do nothing")

        time+=1
        print("------------------------")

    print("--- FCFS END ---")

    #zwrócenie wartości wszystkich czasów oczekiwania
    return timeSum


#funkcja szukająca procesu do wykonania o najmniejszym czasie wykonania
def search(tab, time):

    #ustawienie wartości zmiennych
    min = 1000000
    minId = -1

    #wyszukanie wartości id dla tych procesów, które mają najkrótszy czas wykonania oraz są dostępne (czas procesora)
    for i in range(len(tab)):
        if(tab[i][1] < min and tab[i][0] <= time):
            min = tab[i][1]
            minId = i

    return minId


def SJF(tab):

    #ustawienie wartości poszcególnych zmiennych
    time = 0 #czas procesora
    stos = -1 #id aktualnie wykonywanego procesu
    stosTime = 0 #czas ^ proczesu
    timeSum = np.array([], type(int)) #tablica czasów oczekiwań procesów

    while(1):
        print("Current SJF time: ", time)
        #znalezienie odpowiedniego procesu:
        if(stos == -1):
            stos = search(tab, time)


        if(stos == -1):
            print("processor do nothing")
        else:
            print("processor exec process: ", tab[stos])
            #wykonanie procesu:
            stosTime += 1
            #zakończenie wykonyania procesu:
            if(stosTime == tab[stos][1]):
                timeSum = np.append(timeSum, [ time + 1 - tab[stos][0] - tab[stos][1] ])

                stosTime = 0
                #usuniecie procesu z pamieci (stosu procesora)
                tab = np.delete(tab, stos)
                stos = -1
                #zakonczenie funkcji
                if(len(tab) == 0):
                    break
        time += 1
        print("------------------------")

    print("--- SJF END ---")
    return timeSum

def summary(tab):
    #posortowanie procesów po czasie
    sort(tab, 0)

    #wywołanie funkcji planoania czasu oraz ustaienie tablic czasów oczekiwań.
    fcfsTable = FCFS(tab)
    sjfTable = SJF(tab)

    #wyświetlnenie podsumowania:
    print("------------")
    print("Summary: ")
    print("------------")
    print("Process Number: ", processNumber)
    print("Process Time: (", timeL, ", ", timeH, ")")
    print("Process Exec Time: (", lenL, ", ", lenH, ")")

    print(" --- FCFS --- ")
    #print(fcfsTable)
    print("Average Time for FCFS Algorithm: ", sum(fcfsTable)/len(fcfsTable))

    print(" --- SJF --- ")
    #print(sjfTable)
    print("Average Time for SJF Algorithm: ", sum(sjfTable)/len(sjfTable))


summary(tab)

