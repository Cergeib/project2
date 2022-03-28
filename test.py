from Bio.SeqIO import parse
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

vector = open("C:/Users/yeba/Desktop/vector.fasta")

records = parse(vector, "fasta")
for record in records:
#   print("Id: %s" % record.id)
#   print("Name: %s" % record.name)
#   print("Description: %s" % record.description)
#   print("Annotations: %s" % record.annotations)
#   print("Sequence Data: %s" % record.seq)
    vector_sequence = record.seq
#   print("Sequence Alphabet: %s" % record.seq.alphabet)

print(vector_sequence)

