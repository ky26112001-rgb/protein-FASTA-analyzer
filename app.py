weight_map = {
    "A": 89.09,
    "C": 121.16, 
    "D": 133.10, 
    "E": 147.13,
    "F": 165.19,
    "G": 75.07,
    "H": 155.16,
    "I": 131.18,
    "K": 146.19,
    "L": 131.18,
    "M": 149.21,
    "N": 132.12,
    "P": 115.13,
    "Q": 146.15,
    "R": 174.20,
    "S": 105.09,
    "T": 119.12,
    "V": 117.15,
    "W": 204.23,
    "Y": 181.19
}
sequence = ""
sequence_name = "unknown protein"
total = 0 
import os
filename = input("\nEnter the FASTA filename to open: " )
script_dir = os.path.dirname(os.path.abspath(__file__))
absolute_path = os.path.join(script_dir, filename)
try: 
    with open(absolute_path, "r") as file:
        lines = file.readlines()
    if lines[0].startswith(">"):
        sequence_name = lines[0].replace(">", "").strip()
    else:
        sequence_name = "unknown protein"
    for line in lines[1: ]:
            sequence = sequence + line.strip().upper().replace(" ","")
    total = len(sequence)
except FileNotFoundError:
    print(f"Error: the file '{filename}' was not found. Please check the spelling nad try again.")
    exit()
error = False
for letter in sequence: 
    if letter not in weight_map:
        print(f"error : unidentified amino acid '{letter}' present in sequence")
        error = True
if error:
    print("sequence rejected. try again")
    exit()
else: 
    print("sequence_name:  ",sequence_name)
    print("sequence_length: ", total)

amino_acid_composition = sequence
count = {}
for x in amino_acid_composition: 
    if x in count:
        count[x] = count[x] + 1
    else:
        count[x] = 1
print("amino acid composition and precentage: ")

for amino_acid, frequency in count.items():
    percentage = (frequency / total) * 100
    print(f" {amino_acid} | {frequency} | {percentage: .2f}%")

sequence_valid = True
for amino_acid, frequency in count.items():
    if amino_acid not in weight_map:
        print(f"error: unidentified amino acid '{amino_acid}' present in sequence")
total_molecular_weight = 0.0
for amino_acid, frequency in count.items():
    weight = weight_map.get(amino_acid)
    amino_acid_total_weight = frequency * (weight)
    total_molecular_weight = total_molecular_weight + amino_acid_total_weight
print(f"total molecular weight of sequence: {total_molecular_weight: .2f} g/mol")







