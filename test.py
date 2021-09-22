import csv

with open ('questions.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open ('odpowiedzi.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

   # next(csv_reader) #omija pierwsza linijke 
        for line in csv_reader:
         #   print(line[0])
            csv_writer.writerow(line)  