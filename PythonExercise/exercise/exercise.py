import csv

def operate_csv():
    with open("test.csv") as file_input:
        with open("test.csv", "w") as file_output:
            replaced_text = file_input.read().replace('abc', 'kkk')
            file_output.write(replaced_text)
    
    with open('test.csv') as file_input:
        with open('result.csv', 'w') as file_output:
            reader = csv.reader(file_input)
            writer = csv.writer(file_output)
            for row in reader:
                if len(row) >= 2:
                    row.remove(row[1])
                writer.writerow(row)


def operate_csv_v2():

    with open("test.csv") as file_input:
        lines  = file_input.readlines()
        
        for line in lines:
            replaced_text = line.replace('abc', 'kkk')
            replaced_text_splited = replaced_text.split(',')

            with open("result.csv", "a") as file_output:
                if len(replaced_text_splited) >= 2:
                    replaced_text_splited.remove(replaced_text_splited[1])
                file_output.write(str(replaced_text_splited))

def operate_csv_v3():

    replaced_text = ""
    with open("test.csv") as file_input:
        replaced_text = file_input.read().replace('abc', 'kkk')

    split_text_list = list(csv.reader(replaced_text.splitlines()))

    for row in split_text_list:
        if len(row) >= 2:
            row.remove(row[1])
    
    with open("result.csv", "w") as file_output:
        csv_writer = csv.writer(file_output)
        csv_writer.writerows(split_text_list)
                
operate_csv_v3()
