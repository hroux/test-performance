import os
import zipfile
import time
from Crypto.Cipher import AES
 
fantasy_zip = zipfile.ZipFile('./archive.zip', 'w')

start_time = time.time()
for folder, subfolders, files in os.walk('/home/hugues/NetBeansProjects'):
 
    for file in files:
        fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), '.'), compress_type = zipfile.ZIP_DEFLATED)

print("Compression : --- %s seconds ---" % (time.time() - start_time))
fantasy_zip.close()

# Encryption
encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')

file = open("test_file_crypter.txt", "w")

start_time = time.time()
file_reading = open("test_file.txt", "r")
for line in file_reading:
    len = len(line),
    modulo = len[0]%16,
    line_to_write = line,
    for x in range (0, 16 - modulo[0]):
        line_to_write += '\0',
    file.write(str(encryption_suite.encrypt(''.join(line_to_write)))),
print("Cryptage : --- %s seconds ---" % (time.time() - start_time))
file.close()
file_reading.close()
    
# file = open(“testfile.txt”,”w”) 

# file.write(“Hello World”) 
# file.write(“This is our new text file”) 
# file.write(“and this is another line.”) 
# file.write(“Why? Because we can.”) 
 
# file.close() 
