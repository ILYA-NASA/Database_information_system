from User_Interface import user_choice
from  process import data_processor
from work_file import read_file

data = 'processing_model.csv'
print(data_processor(read_file(data, 'r'), user_choice()))
