#opening the input file with read permission
file = open("Compozent_Task/1st_Task/1.3_File_handling/input.txt","+r")
read = file.read()
#spliting every word in input.txt in a seprate line
text = read.split()
count=0
#a loop to count the number of line(words) in input.txt
for lines in text:
    count = count + 1
#opening/creating the output file with write permission
dw = open("Compozent_Task/1st_Task/1.3_File_handling/output.txt","w")
#converting count into a string cause write only accept str
count = str(count)
dw.write(count)
print("check the number of words that input.txt has in output.txt file")

#you can edit the input.txt file to see if the output is different