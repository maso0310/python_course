import csv

# 寫入資料
with open('students.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Score'])
    writer.writerow(['Alice', 85])
    writer.writerow(['Bob', 92])

# 讀取資料
with open('students.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    # ['Name', 'Score']
    # ['Alice', '85']
    # ['Bob', '92']