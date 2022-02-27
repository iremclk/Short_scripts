input=open('input_file_path/input.txt','r') 
data=input.read() #opens and reads the file

comma = ","
newline = "\n"

IPList = data.maketrans(comma, newline)

host=data.translate(IPList) #translates all "," > newline

print(host) #checks the new lines

f= open("output_file_path/output.txt","w+") #creates and opens the new file

f.write(host) #writes the lines to the new file