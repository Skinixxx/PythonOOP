class FileManager:
    def __init__(self,filename):
        self.filename=filename

    def read(self):
        with open(self.filename,'r') as f:
            return f.read()
        
    def write(self,text):
        with open(self.filename,'w') as f:
            f.write(text)
        
    def append(self,text):
        with open(self.filename,'a') as f:
            f.write(text)

file = FileManager("example.txt")
file.write("Hi. ")
file.append("Hola. ")
print(file.read())
file.write("Hmmm")
print(file.read())