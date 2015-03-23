import os

DELIMITER=","

def write_delimited_list_to_file(items, filename):
    with open(filename,'w+') as f:
        for item in items:
            f.write(item+DELIMITER)
        f.seek(-1, os.SEEK_END)
        f.truncate() # get rid of the last comma
