#https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
def gradingStudents(grades):
    # Write your code here
    for i in range(0,len(grades)):
        if grades[i]<38:
            grades[i]=grades[i]
        elif (5-grades[i]%5)<3:
            grades[i] = grades[i]-grades[i]%5+5
        else:
            grades[i] = grades[i]
    return(grades)
