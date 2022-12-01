# helper function to read data from input file
def read_data(file_name, file_mode='r'):
    file = open(file_name, mode=file_mode)
    data = file.read()
    file.close()
    return data
