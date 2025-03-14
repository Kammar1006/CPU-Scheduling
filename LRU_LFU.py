import numpy as np

pagesLenght = 20 #ilosc stron
pagesValue = 5 #vartosci stron od 1 do 5
memorySize = 5 #pamięc algorytmów

#stworzenie tablicy stron
pages = np.random.randint(low=1, high=pagesValue+1, size=pagesLenght)


#utworzenie tablicy pamieci dla algorytmu LRU
tab = np.array([], type(int))
for i in range(0, memorySize):
    helper = np.array([0, 0])
    tab = np.append(tab, [1])
    tab[i] = helper

#wyświetlenie informacji
print("Pages Len : ", pagesLenght)
print(pages)

print("Memory size: ", memorySize)
print(tab)


def LRU(pages, tab):
    #czas wykorzystywany do ustalenia co zamienić
    time = 1

    print(" --- LRU --- ")

    #pętla algorytmu
    for i in pages:
        print("------------------")
        print("Processor get page nr: ", i)
        #flaga oznaczająca czy wstawić stronę,
        #tz jest true jesli algorytm nie podjął decyzji
        flag = True

        #find this same page
        #szukanie jeśli strona jest w pamięci
        for j in tab:
            if(j[0] == i and flag):
                j[1] = time
                print(tab)
                flag = False
        #find void in memory
        #szukanie pustego miejsca w pamięci
        if(flag):
            for j in tab:
                if(j[0] == 0 and flag):
                    j[1] = time
                    j[0] = i
                    print(tab)
                    flag = False
        #zmiana najdawniej używanej strony
        #change page if memory hasn't void tile and this is different page:
        if(flag):
            #szukanie najdawniejszej strony
            min = tab[0][1]
            minId = 0
            for j in range(len(tab)):
                if(tab[j][1] < min):
                    min = tab[j][1]
                    minId = j

            #zastąpienie strony
            if(minId != -1):
                tab[minId][1] = time
                tab[minId][0] = i
                flag = False
                print(tab)
            else:
                print("Error")

        time += 1

LRU(pages, tab)

#ustawienie pamięci operacyjnej dla LRU (aktualne strony)
lfuMemory = np.array([], type(int))
for i in range(0, memorySize):
    lfuMemory = np.append(lfuMemory, 0)

#ustawienie pamięci częstotliwości:
lfuPageCounter = np.array([], type(int))
for i in range(1, pagesValue+1):
    lfuPageCounter = np.append(lfuPageCounter, 0)

#wyświetlenie informacji (tablic)
print("LFU memory")
print(lfuMemory)

print("LFU pageCounter")
print(lfuPageCounter)

def LFU(pages, lfuMemory, lfuPageCounter):
    print(" --- LFU --- ")

    print(pages)

    #pętla funkcji:
    for i in pages:
        print("------------------")
        print("Processor get page nr: ", i)
        flag = True

        # find this same page
        # szukanie jeśli strona jest w pamięci
        for j in range(len(lfuMemory)):
            if (lfuMemory[j] == i and flag):
                print(lfuMemory)
                flag = False
        # find void in memory
        # szukanie pustego miejsca w pamięci
        if (flag):
            for j in range(len(lfuMemory)):
                if (lfuMemory[j] == 0 and flag):
                    lfuMemory[j] = i
                    print(lfuMemory)
                    flag = False

        # zmiana najrzadziej używanej strony
        # change page if memory hasn't void tile and this is different page:
        if(flag):
            min = lfuPageCounter[lfuMemory[0]-1]
            minId = 0
            #szukanie strony do zamiany która była używana najrzadziej
            for j in range(len(lfuMemory)):
                if(lfuPageCounter[lfuMemory[j]-1] < min):
                    min = lfuPageCounter[lfuMemory[j]-1]
                    minId = j
            if(minId != -1):
                lfuMemory[minId] = i
                flag = False
                print(lfuMemory)
            else:
                print("Error")

        # inkrementacja częstotliwości
        lfuPageCounter[i-1] += 1
        print(lfuPageCounter)

LFU(pages, lfuMemory, lfuPageCounter)