# list Acees and value change option in this code

subject1 = input("enter subject 1 name :")
subject1_marks = int(input("enter subject 1 marks obtained in 100 : "))

subject2 = input("enter subject 2 name :")
subject2_marks = int(input("enter subject 2 marks obtained in 100 : "))

subject3 = input("enter subject 3 name  :")
subject3_marks = int(input("enter subject 3 marks obtained in 100 : "))

subject4 = input("enter subject 4 name  :")
subject4_marks = int(input("enter subject 4 marks obtained in 100 : "))

subjectname  = [subject1,subject2,subject3,subject4]
list = [subject1_marks,subject2_marks,subject3_marks,subject4_marks]

total_marks = subject1_marks+subject2_marks+subject3_marks+subject4_marks

percentage = (total_marks/400)*100

if percentage >=90:
 print("A grade")
 print("pass")

elif percentage >=80:
 print("B grade")
 print("pass")

elif percentage >=70:
 print("C grade")
 print("pass")

elif percentage >=60:
 print("D grade")
 print("pass")

else:
 print("F grade")
 print("Fail")



print(f"Total_Marks:{total_marks}/400")
print(f"Percentage:{percentage}%")
print(f"ALLSUBJECTSNsme:{subjectname}")
print(f"ALLSUBJECTSmARKS:{list}")

# change list subject 3 marks change
# list[2] = int(12) 
# print(f"SUB2CHA{list}")

#aCEES SUBJECT 2 MARKS AND NAME IN LIST
# print(f"SUBJECT2NAME:{subject2} ")
# print(f"SUBJECT2MARKS:{subject2_marks} ")

