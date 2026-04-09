# Example of a string
var = "Hello"
print (var)

var2 = "#@$%"  # we can store special characters or anything inside a string
var3 = "ATGCGTAGACAGTAGACAG"
print (var2)
print (var3)


# String Manipulation - INDEXING
# ATGCGTGATA
# 0123456789   <-- index values (always start from 0)
seq = "ATGCGTGATACGA"
print(seq[5]) # It will print T which is in 5th position
print(seq[-1])  # Negative Indexing

# String Manipulation - SLICING
seq = "ATGCGTGATACGA"
print(seq[1:4:2])  #start:end:step (in this case it starts from 1 index position go upto 4th index poasition stepping up by 2 )

# String Method
seq = "ATGCGTGATACGAAAA"
print(seq.find("AAAA"))  # IT WILL RETURN lowest index value where A starts

seq2 = "ATGTAG CCCTATAT"
print(seq2.split())  # it will split the string into two parts

print(seq2.replace("ATG", "TGC"))

print(seq2.count("G"))


fasta_data = '''>sample_id
ATCTTCTCTCGTGTAATCATAC'''
print(fasta_data)

lines = fasta_data.split('\n')
print(lines)

header = lines[0]
sequence = lines[1]
print (header)
print (sequence)

motifs = ["ATC", "TAG", "GGT", "CCT"]

for m in motifs:
    if m in sequence:
        print( m, "found in position", sequence.find(m), sequence.count(m), "occurs")
    else:
        print(m, "motifs not present")

# Lists

list = ["abc", True, 1, 2, 3 ]
print(list)
print(list[3:5]) # indexing , slicing (it is inclusive in case of lists)
list[1] = False
print (list)
list.insert(2, "ATGC")
print (list)

list2 = ["ATG", False, "TCAG"]
list.extend(list2)
print (list)

list.extend(var)
print(list)

list.remove("ATG")
print(list)

seq_list = [">AW113514.1 MC1637 mouse liver, vehicle control Mus musculus cDNA clone MC1637 3' similar to L07096 Mus domesticus strain MilP mitocondrion geno, mRNA sequence "\
"CGAATNCTTCACGAAAAACACACCCATTATTTAAAATTATTAACCACTCATTCATTGACCTNCCTGCCCC"\
"ATCCAACATTTCATCATGATGAAACTTTGGGTCCCTTCTAGGAGTCTGCCTAATAGTCCAAATCATTACA"\
"GGNCTTTTCTTANCCATACACTACACATCANGATACAATAACAGCCTTTTCATCAGTAACACACATTTGT"\
"NGAGACGTAAATTACGGGTGACTAATNCGATATATNCACGCAAACGGGCCTCAATATTTTTTATTTGCTT"\
"ATTCCTTCATGTCGGACGAGGCTTATATTATGGATCATATACATTTATAGAAACCTGAAACATTGGAGTA"\
"CTTCTACTGTTCGCA"]
sequence = "".join(seq_list)
print(sequence)
print("Sequence Length", len(sequence))

purines = "".join([x for x in sequence[:200] if x in ["A", "G"]])
print("Number of purines in the sequence is:", len(purines))

g_count = sequence.count("G")
c_count = sequence.count("C")
atg_count = sequence.count("ATG")

print(g_count)
print(c_count)
print(atg_count)

#Tuples

tuple = ("apple", 25, "male", "male")
print(tuple)
print(tuple.count("male"))
print(tuple.index("apple"))

student = ("Alice", 23, "Female", "BioTechTrek")
name, age, gender, org = student
print (name)
print (org)

fastq_record = [
    ("seq_id_1", "ATGCGATGCCTACAGCATCGCATACGACTCGACTACGACTACACGACTACGACATCACGACTAGGT", "111111"),
    ("seq_id_2", "GTAGCAGCAGTCAGTACGTGTAGTACGTCAGTCAGTACGTACGTACGTACGTACGTACGTACGTACAC", "21211"),
    ("seq_id_3", "CATCATGCAGTCGTACGTACAGTCGTCAGTAGTACGTACTGCGTATCGATACGTATGCAGTATGCGTA", "132311")
]

for read in fastq_record:
    read_id, sequence, quality_score = read

    print("Sequence Id:", read_id)
    print("Sequence length:", len(sequence))
    print("Quality Score:", quality_score)


# Dictionary

dictionary = {"Apple": "Red", 
              "Banana": "Yellow",
              "dragon-fruit": "green"
              }

print(dictionary["Apple"])
print(dictionary["Banana"])

dictionary["Apple"] = "pink"
print(dictionary)

print(dictionary.keys())

# biological example 

sample_metadata ={
    "Sample_ID01": {
        "Age": 12,
        "Gender": "Female",
        "Sample": "Blood",
        "Disease": "Healthy"
    },
    "Sample_ID02": {
        "Age": 25,
        "Gender": "Female",
        "Sample": "Gut",
        "Disease": "Healthy"
    },
    "Sample_ID03": {
        "Age": 32,
        "Gender": "Female",
        "Sample": "Skin",
        "Disease": "Healthy"
    }
}

print(sample_metadata)
print("Metadata for Sample_ID03:", sample_metadata["Sample_ID03"])
print("Disease of Sample_ID03:", sample_metadata["Sample_ID03"]["Disease"])
sample_metadata["Sample_ID03"]["Disease"] = "IPF"

removed_sample = sample_metadata.pop("Sample_ID02")
print("Removed sample metadata:", removed_sample)
print(sample_metadata)

print("Sample Ids:", sample_metadata.keys())


# Sets

set = {1,2,3,4,5}
print(set)

set.add("abc")
print(set)

set.remove("abc")
print(set)

set1 = {1, 2 , 3, "a", "b", "c"}
set2 = {3, 4, 5, "d", "e", "f"}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))



