def data_reader():
    data = open('processing_model.txt', 'r', encoding= 'utf-8')
    data = data.read().splitlines()
    a = []
    for i in data:
        i = i.split(',')
        a.append(i)
    return a



# print(data_reader())
# # data = open("res.txt", 'w')
# # data.writelines(str(data_reader()))
# # data.close()
# for line in data_reader():
#     line = ' '.join(line)
#     print(line)

def data_processor(lst, n):
    a = []
    if n == 'all':
        return lst
    elif 0 < n < 6:
        for i in lst:
            a.append(i[n-1])
        return a
    else:
        return 'Error'

print(data_processor(data_reader(), 2))