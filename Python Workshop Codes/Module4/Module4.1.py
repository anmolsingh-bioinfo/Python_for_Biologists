from Bio import SeqIO   #Importing Biopython module "SeqIO"

# PARSING GENBANK FILE USING BIOPYTHON
with open('sequence.gp.txt') as input_handle:
    for record in SeqIO.parse(input_handle, 'genbank'):
        print("ID:", record.id)

# Converting genbank file to fasta file
with open('sequence.gp.txt') as input_handle, open('sequence.fasta', 'w') as output_handle:
    sequences = SeqIO.parse(input_handle, 'genbank')
    output = SeqIO.write(sequences, output_handle, 'fasta')
    print("Convereted", output , "records")
    print("sequence.fasta created")


# Working with huge genome dataset

from Bio import SeqIO
filepath = "sequence_full.gb.txt"
gb_records = list(SeqIO.parse(filepath, "genbank"))
genes = []

for record in gb_records:
    for feature in record.features:
        if feature.type == 'gene':
            genes.append(feature)
print("Number of genes:", len(genes))

gene_of_interest = "recF"
hits = []
for gene in genes:
    if 'gene' in gene.qualifiers:
        if gene_of_interest == gene.qualifiers['gene'][0]:
            hits.append(gene)
            print("gene found")
            print("Number of hits", len(hits))

recF = hits[0]

from Bio.SeqRecord import SeqRecord
extracted_sequence = recF.extract(gb_records[0].seq)
print("extracted sequence:", extracted_sequence)
print("length of extracted sequence:", len(extracted_sequence))

seq_record = SeqRecord(
    extracted_sequence,
    ID = "recF",
    description= "recF gene sequence"
)

SeqIO.write(seq_record, 'recF.fasta', 'fasta')
print ("'recF.fasta' file has been created")


