import pandas as pd

filename = "~/Desktop/a.xls"
df = pd.read_excel(filename)
rows = df.shape[0]


def check_yes(num_grade, num_class):
    yes_list = []
    no_list = []
    for i in range(rows):
        record = df.iloc[i].values
        if record[3] == str(num_grade) + str(num_class) + "班":
            if record[6] == "是":
                yes_list.append(record[4])
            else:
                no_list.append(record[4])
        else:
            continue
    print(num_grade + str(num_class) + "班")
    print("是", yes_list)
    #  print("否", no_list)
    print()


for i in range(1, 8):
    check_yes("三年级", i)
