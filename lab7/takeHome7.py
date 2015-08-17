def addGrade():
    print "\nadd grade"

def removeGrade():
    print "\nremove grade"

def modifyGrade():
    print "\nmodify grade"

def displayGrades():
    print "\nprint grades"

gradeBook = {"Carl":"B+","Joe":"C","Sarah":"A","Francine":"A"}

selection = 0

while selection != -1:
    print """Select an option:
  [1] Add Student Gade
  [2] Remove Student Grade 
  [3] Modify Student Grade
  [4] Display All Student Grades"""

    selection = int(raw_input("\nEnterSelection: "))

    if selection == 1:
        addGrade()
    elif selection == 2:
        removeGrade()
    elif selection == 3:
        modifyGrade()
    elif selection == 4:
        displayGrades()
