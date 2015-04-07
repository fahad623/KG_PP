import csv

location_train_values = "..\\..\\data\\train_values_trunc.csv"
location_train_labels = "..\\..\\data\\train_labels_trunc.csv"
location_test = "..\\..\\data\\test.csv"

location_train_vw = "..\\..\\data\\train.vw" #will be created
location_test_vw = "..\\..\\data\\test.vw" #will be created

def to_vw(location_input_file_values, location_input_file_labels, location_output_file, test = False):
    with open(location_input_file_values) as infile1, open(location_input_file_labels) as infile2, open(location_output_file, "wb") as outfile:
        reader = csv.DictReader(infile)
        for row in reader:
   

to_vw(location_train, location_train_vw)
#to_vw(location_test, location_test_vw, test=True)