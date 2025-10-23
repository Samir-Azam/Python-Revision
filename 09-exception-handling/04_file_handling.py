# Two ways to open a file

# try:
#     file = open("demo.txt", "a")
#     file.write("This is demo.txt file\n")
# except Exception as e:
#     print(e, "Error in opening the file")
# finally:
#     print("Closing the file")
#     file.close()

# 2nd way 

with open("demo.txt","a") as f:
    f.write("Writing into File using with keyword")