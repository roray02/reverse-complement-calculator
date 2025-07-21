#!/usr/bin/python3
#!/usr/bin/env python3

def reverse_complement(sequence):
   complement_dict = {  # dictionary that maps each nucleotide to its complement
       'A': 'T',
       'T': 'A',
       'C': 'G',
       'G': 'C'
   }

   sequence = sequence.upper()  # convert sequence to uppercase just in case

   complement = ''
   for base in sequence:
       if base in complement_dict:
           complement += complement_dict[base]
       else:
           return "Invalid sequence: contains non-nucleotide characters"

   return complement[::-1] # reversing the complement sequence


if __name__ == "__main__":
   # keeps prompting for sequences until an invalid one is entered
   while True:
       sequence = input("Enter an oligonucleotide sequence: ")
       result = reverse_complement(sequence)
      
       # check if result shows invalid sequence
       if result.startswith("Invalid"):
           print(result)
           break    # break loop if invalid sequence
          
       print("Reverse complement:", result)