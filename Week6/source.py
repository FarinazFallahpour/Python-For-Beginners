#Farinaz Fallahpour
import hashlib
import csv
import collections


def hash_password_hack(input_file_name, output_file_name):
    database = collections.OrderedDict()
    for i in range(1000, 10000):
        my_hash = hashlib.sha256(str(i).encode()).hexdigest()
        database[my_hash] = i
    with open(input_file_name, 'r') as readfile:
        with open(output_file_name, 'w') as writefile:
            lines = csv.reader(readfile)
            for line in lines:
                password = line[1]
                writefile.write(line[0] + ',' + str(database[password]) + '\n')

# hash_password_hack('input.csv','output.csv')
