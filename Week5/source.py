#Farinaz Fallahpour
import csv
from statistics import mean
import collections


def calculate_averages(input_file_name, output_file_name):
    with open(output_file_name, 'w') as writefile:
        with open(input_file_name, 'r') as readfile:
            lines = csv.reader(readfile)
            for line in lines:
                name = line[0]
                grades = line[1:]
                gradesInt = map(lambda x: int(x), grades)
                currentMean = mean(gradesInt)
                writefile.write(name + ',' + str(currentMean) + '\n')


def calculate_sorted_averages(input_file_name, output_file_name):
    std = collections.OrderedDict()
    with open(input_file_name, 'r') as readfile:
        lines = csv.reader(readfile)
        for line in lines:
            name = line[0]
            grades = line[1:]
            gradesInt = map(lambda x: int(x), grades)
            currentMean = mean(gradesInt)
            std[currentMean] = name

    with open(output_file_name, 'w') as writefile:
        for key, value in sorted(std.items()):
            writefile.write(value + ',' + str(key) + '\n')


def calculate_three_best(input_file_name, output_file_name):
    std = collections.OrderedDict()
    with open(input_file_name, 'r') as readfile:
        lines = csv.reader(readfile)
        for line in lines:
            name = line[0]
            grades = line[1:]
            gradesInt = map(lambda x: int(x), grades)
            currentMean = mean(gradesInt)
            std[currentMean] = name

    with open(output_file_name, 'w') as writefile:
        sorted3keys = sorted(std.keys(), reverse=True)
        for key in sorted3keys[:3]:
            writefile.write(std[key] + ',' + str(key) + '\n')


def calculate_three_worst(input_file_name, output_file_name):
    std = collections.OrderedDict()
    with open(input_file_name, 'r') as readfile:
        lines = csv.reader(readfile)
        for line in lines:
            name = line[0]
            grades = line[1:]
            gradesInt = map(lambda x: int(x), grades)
            currentMean = mean(gradesInt)
            std[currentMean] = name

    with open(output_file_name, 'w') as writefile:
        sorted3keys = sorted(std.keys())
        for key in sorted3keys[:3]:
            writefile.write(str(key) + '\n')


def calculate_average_of_averages(input_file_name, output_file_name):
    sum = 0
    count = 0
    with open(input_file_name, 'r') as readfile:
        lines = csv.reader(readfile)
        for line in lines:
            count += 1
            name = line[0]
            grades = line[1:]
            gradesInt = map(lambda x: int(x), grades)
            currentMean = mean(gradesInt)
            sum += currentMean
    totalmean = sum / count
    with open(output_file_name, 'w') as writefile:
        writefile.write(str(totalmean))

# calculate_averages('input.csv', 'calculate_avg.csv')
# calculate_sorted_averages('input.csv', 'calculate_avg_sorted.csv')
# calculate_three_best('input.csv', 'calculate_avg_sorted3.csv')
# calculate_three_worst('input.csv', 'calculate_three_worst.csv')
# calculate_average_of_averages('input.csv', 'calculate_totalmean.csv')
