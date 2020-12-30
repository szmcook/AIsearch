from os import listdir
from os.path import isfile, join
import csv

PATH_TO_SEARCHFILES = "./Search Files"
onlyfiles = [f for f in listdir(PATH_TO_SEARCHFILES) if isfile(join(PATH_TO_SEARCHFILES, f))]

ord_range = [[32, 126]]
with open('eggs.csv', 'w', newline='') as csvfile:
  w = csv.writer(csvfile)
  w.writerow(["File Name","Algorithm Code","Num of Cities","Tour Length", "Tour","Note"])
  for fileName in onlyfiles:
    the_file = open("./Search Files/"+fileName, 'r')
    current_char = the_file.read(1)
    file_string = ""
    length = len(ord_range)
    while current_char != "":
        i = 0
        while i < length:
            if ord(current_char) >= ord_range[i][0] and ord(current_char) <= ord_range[i][1]:
                file_string = file_string + current_char
                i = length
            else:
                i = i + 1
        current_char = the_file.read(1)
    the_file.close()
    bananaSplit = file_string.split(",",5)

    algorithm_code = bananaSplit[1][-2:]
    size = bananaSplit[3][7:]
    length = bananaSplit[4][15:]
    pateIsABreakfastFood = bananaSplit[5].split(",NOTE =")
    tour = pateIsABreakfastFood[0]
    note = pateIsABreakfastFood[1]
    w.writerow([fileName,algorithm_code,size,length,tour,note])

