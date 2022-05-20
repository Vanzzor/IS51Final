"""
Program opens and uses a file (final.txt) that has the grades for the students.
we append the lines from the txt file to our program
calculates count of grades
calculate average by the sum of values divided by count of grades
turn average into percentage
if the value is > average, send to list, divide count of list on original grade average
close file
print output to the user


"""

"""
def main 
file=open file.txt
grades=[]
grades.append(int(line.strip))
print="number of grades" len(grades)
avg=0
for grade in grades add avg to grades
average /= len(grade)
print average, avg

def calculate_percent_above_average()
count=0
if grade > avg add to count
return count*100/len(grades)
print "percentage of grades above average"
f.close

"""

def calculate_percent_above_average(grades, avg):
    count=0
    for grade in grades:
        if grade > avg:
            count +=1
    return(count*100)/len(grades)

def main():
    f=open("Final.txt", "r")
    grades=[]
    for line in f:
        grades.append(int(line.strip()))
    print("Number of grades:", len(grades))
    avg=0
    for grade in grades:
        avg += grade
    avg /=len(grades)
    print("Average grade: ", avg)
    print("Percentage of grades above average: {:.2f}%".format(calculate_percent_above_average(grades, avg)))
    f.close()


main()