#now we are going read a file that has been already created and perform some tasks

f=open("D:\\DEEPu\\AI Engineer Roadmap\\Python Projects\\Basics Of Python\\Modules\\funny2.txt", "r")
#print(f.read())
#f.close()
#this above code just prints the text file as it is
#and now we will learn how to go through this file line by line
f_out=open("D:\\DEEPu\\AI Engineer Roadmap\\Python Projects\\Basics Of Python\\Modules\\funny2_wc.txt", "w")
for line in f:
    tokens=line.split(' ')
    f_out.write(" WordCount:"+str(len(tokens))+" "+line+"\n")
f.close()
f_out.close()

# r -> opens file for reading only. Throws error if the file does not exist
# w -> opens file for writing only. If file doesn't exist then it will create new one. IF it exist then it will overwrite it.
# r+ -> opens file for both reading and writing
# w+ -> opens file for reading and writing. If file doesn't exist then it will create new one. IF it exist then it will overwrite it.
# a -> opens a file in append mode. Whatever you write you will get appended and original content will not be overwritten.
