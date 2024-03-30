#Writing a string in a file

s = "Coding is love"

with open("test.txt", "w") as f:
    f.write(s)
    
fp = open("test.txt", "w")
fp.write(s)
fp.close()

#Write mode delets old data and write tehe new data so we use apend mode 

#all the syntax of read , write , append are same 