import time
# Subdomain duplicate eliminator tool
print("\t\t\t\t* * * * * Welcome * * * * *")
print(
    "[*] Info : This tool is used to eliminate the duplicates between two files usually works for subdomain duplacy"
)
inp_file_1 = input("[+] Enter the name/path for first file:- ")
inp_file_2 = input("[+] Enter the name/path for second file:- ")

#opening the files which contains subdomains
file_1 = open(inp_file_1, 'r+')
file_2 = open(inp_file_2, 'r+')

list_1 = file_1.readlines()
list_2 = file_2.readlines()

#creating two list variables and storing file data into them
list_3 = []  # empty list
list_4 = []  # empty list

file_1.close()
file_2.close()

#Writting the output in the final file
# removing duplicates from list 1
with open("final_subdy.txt", 'w+') as new_file:
  # new_file.writelines(list_1)
  for x in list_1:
    if x in list_2:
      continue
    else:
      list_3.append(x)
  list_3.append('\n')

# removing duplicates from list 2
with open("final_subdy.txt", 'a') as new_file:
  for x in list_2:
    if x in list_3:
      continue
    else:
      list_3.append(x)
  list_3.append('\n')

ok = list(set(list_3))
print(len(ok))

# removing duplicates from final list
with open("final_subdy.txt", 'a') as new_file:
  new_file.writelines(ok)

#finishing touch
time.sleep(1)
print("Final file is ready , Thankyou for Using")
print("Bie Bie")
exit()
