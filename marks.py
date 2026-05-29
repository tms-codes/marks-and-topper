
students= []
while True:

 print("choose one to begin")
 print("1.add student")
 print("2.show student")
 print("3.topper student")
 print("4.failed student")
 print("5.exit")
 choice= int(input("enter your choice"))
 if  choice ==1:
  name = input("enter your name")
  mark1 = int(input("enter the marks1:"))
  mark2 = int(input("enter the marks2:"))
  mark3 = int(input("enter the marks3:"))
  avg = (mark1+mark2+mark3)/3
  student ={"name":name,
            "mark1":mark1,
            "mark2":mark2,
            "mark3":mark3,
            "avg":avg}
  students.append(student)
 elif choice==2:
  for student in students:
   print(student)
 elif choice == 3:
  highest = 0
  topper = None

  for student in students:

    if student["avg"] > highest:

        highest = student["avg"]
        topper = student

        print(topper)
 elif choice ==4:
  if mark1<35 or mark2<35 or mark3<35:
   print("this student failed", student)
  else:
   print("this student is passed",student)
 elif choice == 5:
  print("you exited")
  break
 else:
  print("INVALID CHOICE")
   