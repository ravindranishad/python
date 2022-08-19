from email.headerregistry import Address
import os 

print('current folder')
print(os.getcwd())
print(os.listdir())

print("C Drive content")
os.chdir('C:\\Program Files')
print(os.getcwd())
print(os.listdir())

Address =r'C:\Program File\Python\Python\.exe'
if os.path.exists(Address):
    print('File exists')
else:
    print('File dose not exist')