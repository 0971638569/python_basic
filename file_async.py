print('-----------------Open file---------------------')
info = {
    'name': '',
    'mode': '',
    'status': ''
}
def openFile():
    # mo file
    file = open('readme.md')
    # doc file
    data = file.read();
    # dong file
    file.close()
    # in du lieu doc duoc
    print(data)

def writeFile(string = '11111111111'):
    file = open('readme.md', 'w')
    # doc file
    file.write(string)
    # dong file
    file.close()

def informationFile():
    file = open('readme.md','w')
    info['name'] = file.name
    info['mode'] = file.mode
    info['status'] = file.closed
    file.close()
    
openFile()
writeFile('222222222')
openFile()
writeFile('111111111')
informationFile();
print(info)

print('-----------------Input---------------------')
print('Hello!')
name = input('What your name ?:')
print("Name: " + name)
