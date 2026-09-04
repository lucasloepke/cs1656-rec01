from ast import For
import os
from requests import get
import json
import csv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Task(object):
    def __init__(self):
        self.response = get('https://labrinidis.cs.pitt.edu/cs1656/data/hours.json', verify=False) 
        self.hours = json.loads(self.response.content) 

    ### def part4(self)
    # For this part, you must use `self.hours` we defined
    # in part 3, and store its data as a CSV file (hours.csv),
    # with the fields `name`, `day` and `time`. You should look
    # up the `csv` module and the `writer()` function in particular.
    # The command to open the csv file for writing is already in the template,
    # so, don't change it.
    def part4(self):
        with open('hours.csv', 'w', newline='') as csvfile:
            f = csv.writer(csvfile)
            f.writerow(['name', 'day', 'time'])
            f.writerows([row['name'], row['day'], row['time']] for row in self.hours)
    #write output to hours.csv


    # For this part, you must open the CSV file created from part 4, 
    # read its contents, and write them in the file `part5.txt`.
    def part5(self):
        with open('hours.csv', 'r') as csvfile:
            r = csv.reader(csvfile)
            with open('part5.txt', 'w') as x:
                for row in r:
                    x.write(','.join(row) + '\n')
    #write output to 'part5.txt'
        
        
    # For this part, you must open the CSV file again, but 
    # this time you must parse it using `csv.reader()`, and 
    # write only the rows, one row at a time, in the file 
    # `part6.txt`. The rows have to be written as if they 
    # were being printed on the console. For example, if the 
    # csv has two rows, with one row having two fields, a string 
    # "One" and a string "Two", and the second row having the strings 
    # "Three" and "four", they have to be written as
    #​	\['One', 'Two']\['Three', 'Four'\]

    def part6(self):
        with open('hours.csv', 'r') as csvfile:
            r = csv.reader(csvfile)
            #write output to 'part6.txt'
            with open('part6.txt', 'w') as f:
                for row in r:
                    f.write('\\' + str(row))
                    
        
    # For this part, you must open the CSV file again, parse it 
    # using `csv.reader()`, iterate through the rows, and write 
    # every cell, one cell at a time, without spaces or anything, 
    # in the file `part7.txt`. The example above would be written 
    # as OneTwoThreeFour
    def part7(self):
        with open('hours.csv', 'r') as csvfile:
            r = csv.reader(csvfile)
            #write output to 'part7.txt'
            with open('part7.txt', 'w') as f:
                for row in r:
                    f.write(''.join(row))
        


if __name__ == '__main__':
    task = Task()
    task.part4()
    task.part5()
    task.part6()
    task.part7()