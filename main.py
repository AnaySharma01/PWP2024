#Imports packages
import re
import os

#Creates a new csv file
f = open("saved_file.csv","+w")
 
#Creates an array of the files 
path = 'C:/Users/anays/Downloads/PWP2022'
files = os.listdir(path)

#Loops through the array of files
for file in files:
  #Creates variables for checking for duplicates
  count = 0
  add_char = ""
  isduplicate = True
  
  #Matches the file with the file currently in the loop
  match = re.match(r"(IMG|MMA|SM|WJ2)_*(\d+)(\.JPG)", file)
  #Pads zeroes in front of the number
  padded_zeroes = "000" + match.group(2)
  #Creates new file
  new_file = f"PWP2024_{padded_zeroes}A_ANAY{match.group(3)}"
  #Renames the files after joining the paths
  old_filepath = os.path.join(path, file)
  while isduplicate:
    #Checks if there are duplicates in the file
    try:
      new_filepath = os.path.join(path, new_file)
      os.rename(old_filepath, new_filepath)
      f.writelines(file+","+new_file+"\n")
      isduplicate = False
    except:
    #If there are duplicates, add extra letter to the file name
      if count == 0:
        add_char = 'n'
      elif count == 1:
        add_char = 'a'
      elif count == 2:
        add_char = 'y'
      else: add_char += 'y'
      new_file = f"PWP2024_{padded_zeroes}A{add_char}_ANAY{match.group(3)}"
f.close()
  
