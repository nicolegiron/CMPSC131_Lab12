# Author: Nicole Giron nqg5259@psu.edu
# Collaborator: Hanyu Zhang hzz5302@psu.edu
# Collaborator: Mack Mason mjm8542@psu.edu
# Collaborator: Zihan Xia zfx5078@psu.edu
# Section: 4
# Breakout: 6

from sys import argv
import pickle
import csv

def run():
  """
  This program should be run with the following command line arguments:

  python3 lab12.py input.pickle output.csv
  
  input.pickle file will be a binary file that contains pickle-dump'ed 
  data of a python list of dictionaries. Each dictionary will share
  the same key and corresponds to the csv file's header row. And each
  dictionary corresponds to a row in the csv file.

  Your program shall read in the data from input.pickle file; and then
  write to the output csv file including the header row.
  """
  if len(argv) < 3:
    print(f"Usage: python3 {argv[0]} input.pickle output.csv")
    return
  with open(argv[1], 'rb') as f:
    csvpickle = pickle.load(f) 
  with open(argv[2], 'w', newline='') as output:
    csvoutput = csv.DictWriter(output, csvpickle[0].keys(), dialect='excel')
    csvoutput.writeheader()
    rows=[]
    for row in csvpickle:
      rows.append(row)
    csvoutput.writerows(rows)
  return

if __name__ == "__main__":
  run()
