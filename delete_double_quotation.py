import glob
import sys
import os
import shutil
import csv

def to_csv(original_csv_file, new_file=None):
    #reader = csv.reader(original_csv_file.splitlines())
    with open(original_csv_file, 'r', encoding='utf-8', newline='') as rf:
        reader = csv.reader(rf, delimiter=',')
        with open(new_file, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            for row in reader:
                writer.writerow(row)


target_directory = sys.argv[1]
output_directory = os.getcwd() + os.sep + "output"
os.makedirs(output_directory, exist_ok=True)
cwd = os.path.dirname(__file__)

targetFiles = glob.glob(cwd + os.sep + target_directory + os.sep + '*')

for file in targetFiles:
    try:
        to_csv(file, output_directory + os.sep + os.path.basename(file))
        #print(file)
    except:
        shutil.rmtree(output_directory)
        print("error")
        sys.exit(1)
        