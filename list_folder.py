import os
list_dir = os.listdir('D:\\New_dev65\\modules\\zope_build\\src')
# print(type(list_dir))
for j in list_dir:
    if "jiva" in j:
        print(j)
