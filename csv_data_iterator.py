import glob
import os
import sys
count = 0 
my_list = list()
result = []
def iterate():
    for root, subdirs, files in os.walk("/var/www/Lithia/"):
        print(subdirs)
        print(files)
        for file in os.listdir(root):
            filePath = root + '/' + file
            if os.path.isdir(filePath):
                count = +1
                f = open("filepath", "a")
                f.write(str(filePath) + "\n")
                my_list.insert(count, filePath)              
    f.close()
    return my_list

iterate()

counter_list = list(enumerate(my_list, 1))
#print(counter_list)

#filter function 
#keywords 

def filter():
    for root, subdirs, files in os.walk("filepath"):
        for file in os.listdir(root):
            filePath = root + '/' + file
            if os.path.isdir(filePath):
                result.append(filePath)
                print(result)
    return result        

filter()
