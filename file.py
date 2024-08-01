"""a=open("a.txt",'a')
a.write("python ")
a.close
import os
cwd = os.getcwd()
print(cwd)
files = os.listdir(cwd)
print("Files in %r: %s" % (cwd, files))

#
import csv
with open("abc.csv",mode='w') as pfile:
    pfile_writer=csv.writer(pfile,delimiter=",",quoting=csv.QUOTE_NONE)
    pfile_writer.writerow(["stock_name","stock_quantity","price"])
    pfile_writer.writerow(["ust",5,3200])
"""
import csv
with open("abc.csv",mode='r') as pfile:
    csv_reader=csv.reader(pfile,delimiter=",")
    line_count=0
    for row in csv_reader:

        print(",".join(row));

