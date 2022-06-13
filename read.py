# СМОТРЕЛА КАК РАБОТАТЬ С CSV
f = open('database.csv','w',encoding='utf-8')
f.writelines('id')
f.writelines('name' + '\n')
f.writelines('123')
f.writelines('name' + '\n')
f.close()

f = open('database.csv', 'r', encoding='utf-8')
data = list(f.read())
f.close()
print("Hello PEBU3OP")
print(data)