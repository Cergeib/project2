
sequence_site = 'ааbbbb'
vector = 'cсссссссааааааааааааааааааааbbbbbbbbbbbbbbbbbbbbbaaacaaabbbbbbbbbbbbbbbbaaabbbbaaaсссссссаааааааааа'

insertion_sequence = "аааааааасссссссаааааааааааааааааbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaa" # последовательность вставок

insert_set = ['aacccc', 'bbbbbb', 'ааbbbb', 'аааааа', 'аасссс', 'сссааа', 'аааааа', 'аааааа', 'ааbbbb'] #набор вставок

res = ' '.join([insertion_sequence[i:i+6] for i in range(0, len(insertion_sequence), 6)]) if ' ' not in insertion_sequence[:6] and len(insertion_sequence) > 6 else insertion_sequence
# # делим набор символов в строке по 6шт пробелами,
# # для получения служебного знака, чтобы по нему поделить строку на списки
sort_order = (res.split(' '))
# сделали список

print(sort_order)

new_insert_sequence = []

for i in sort_order:
 if i in insert_set:
  new_insert_sequence.append(i)
 else:
  break
print(new_insert_sequence)
# сортировать по другому списку (вставки выстроены в необходимой последовательности)

new_insert_sequence = ''.join(new_insert_sequence)
print(new_insert_sequence)
# склеиваем вставки

a, b = vector.split(sequence_site)
result = a+sequence_site+new_insert_sequence+b
print(result)
#режет по концу сайта рестрикции
#вставляет последовательность
