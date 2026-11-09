import csv

# 保存列表数据到csv文件
student_csv_header = ["名称", "班级"]
student_csv_rows = [
    ["张三", "高一3班"],
    ["李四", "高二5班"]
]
with open('student.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(student_csv_header)
    writer.writerows(student_csv_rows)

# 以列表方式读取csv文件数据
with open('student.csv', 'r') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        if len(row) == 2:
            print(row[0] + " " + row[1])

# 保存字典数据到csv文件
employee_csv_rows = [
    {
        "name": "王五",
        "age": 22
    },
    {
        "name": "赵六",
        "age": 33
    }
]
with open('employee.csv', 'w') as csvfile:
    dict_writer = csv.DictWriter(csvfile, fieldnames=['name', 'age'])
    dict_writer.writeheader()
    dict_writer.writerows(employee_csv_rows)

# 以字典方式读取csv文件数据
with open('employee.csv', 'r') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        print(row.get("name")+" "+row.get("age"))

print("----------------------------------------------------------------------------------------------------------------------------")
