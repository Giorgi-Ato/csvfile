import csv

with open('annual-enterprise-survey-2020-financial-year-provisional-csv.csv', 'r') as fl:
    reader = csv.DictReader(fl, delimiter=',')
    fieldnames = reader.fieldnames
    reader = list(reader)

    for u in fieldnames:
        with open(f'{u}.csv', 'w') as nf:
            writer = csv.writer(nf)
            for i in reader:
                writer.writerow(i[u])
