from Bio.SeqIO import parse#dfsfdsfdsfsdfsdfsdfsdfd
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

vector = open("C:/Users/yeba/Desktop/vector.fasta") #последовательность вектора
records = parse(vector, "fasta")
for record in records:
    vector_sequence = record.seq

print(vector_sequence)

vstavki = []
vst = open("C:/Users/yeba/Desktop/vstavki.txt", 'r') #открываем файл со вставками (3 шт)
vstavki = map(str.strip, vst.readlines())
#дальше сшиваем вставки в одну (строчки Сережи)
new_insert_sequence = ''.join(vstavki)
print(new_insert_sequence)

#открываем файл с сайтами рестрикции
sites1 = open("C:/Users/yeba/Desktop/resrtr.txt", 'r')
sites = [i for i in sites1.read().splitlines() if i] #получаем список с сайтами
print(sites)

#теперь ищем сайты рестрикций в векторе
good_sites = []
list_of_index = []
for i in sites:
    if i in vector_sequence:
        good_sites.append(i) #добавляем в список гуд_сайтс сайты, которые есть в векторе
        list_of_index.append(vector_sequence.find(i)) #и находим их индекс и добавляем его в лист оф индекс. из этого можно сделать потом словарь
print(good_sites)
print(list_of_index)

#теперь берем первый попавшийся сайт рестриции (пока что) и туда вставляем вставку(команды Сережи)
a, b = vector_sequence.split(good_sites[0])
result = a+good_sites[0][0:3]+new_insert_sequence+good_sites[0][3:] + b
print(result)
#режет поcле 3 нуклеотида сайта рестрикции
#вставляет последовательность


vector.close()
vst.close()
sites1.close()

