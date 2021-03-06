"""
exercise_03
2/8/2018

For this Exercise you will write one definition that will take in the name of a
directory as a string, and return a dictionary containing every sequence in every FASTA file where
the sequence header is the key and the DNA sequences are values.

Your definition will be tested with improperly formatted FASTA files and should handle the following cases:
    1) If there are extra new line characters, or empty lines, your program should still process sequences normally
    2) If a duplicate header exists between two entries your definition should check to see if the sequences are the same
        * If the headers and sequences are identical, your program should print a message that "a duplicate entry exists
          for <header>" and continue normally.
        * If the only the headers match, you should print a message that "duplicate headers with non-identical
          sequences were found for <header>" and neither entry should be added in the dictionary.
          (your print statements don't need to be identical to what I have written here)
    3) If a file in the directory is not a fasta file, your program should not open it.
    4) If a sequence contains characters that are not A, C, G, or T, then it should not be added to the dictionary.

If your program is working correctly, the dictionary should only contain the 4 "good sequence"s in the test folder.


The following syntax may be helpful:

# deleting from a dictionary
del my_dictionary[key]

# printing and formatting a string
x = 'my_variable'
print('Error related to variable: {}'.format(x))

# checking your final dictionary by printing out key, value pairs
for key, value in my_dictionary.items():
    print('Key is: {}\tValue is: {}'.format(key, value))

"""

import os

def fasta_folder_to_dict(folder_path):
    """
       Constructs a dictionary of all of the FASTA formatted entries from a folder containing FASTA files.
       :param folder_path: string
       :return: dictionary
    """
    my_dict = {}
    for file_name in os.listdir(folder_path):
        if(file_name.endswith('fasta')):
            with open(folder_path+file_name, 'r') as infile:
                text = infile.read()
                seqs = text.split('>')
                for seq in seqs:
                    try:
                        x = seq.split('\n', 1)
                        header = x[0]
                        sequence = x[1].replace('\n', '')
                        if header in my_dict:
                            if sequence == my_dict[header]:
                                my_dict[header] = sequence
                                print('Entry is dublicate')
                            else:
                                print('Duplicate header with different sequence')
                                del(my_dict[header])
                                continue
                        x = 1
                        for char in sequence:
                            if char == "A":
                                pass
                            elif char == "C":
                                pass
                            elif char == "T":
                                pass
                            elif char == "G":
                                pass
                            else:
                                x = 0
                                print('Sequence is invalid')
                                break
                        if x == 1:
                            my_dict[header] = sequence
                        if sequence != '':
                            my_dict[header] = sequence
                    except:
                        print('error')


    return my_dict

my_dictionary = fasta_folder_to_dict('test_files/')
for key, value in my_dictionary.items():
    print('Key is: {}\tValue is: {}'.format(key, value))
