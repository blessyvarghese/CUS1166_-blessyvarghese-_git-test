from Models import Student

from Math_utils import Average

def main():
    x = []
    x.append(Student("Blessy",100))
    x.append(Student("Deena",90))
    x.append(Student("Sarah",80))
    x.append(Student("Peter",66))
    x.append(Student("Joel",97))
    x.append(Student("Jacob",83))
    x.append(Student("Mathew",44))
    x.append(Student("Jackie",94))
    x.append(Student("Tyler",79))
    x.append(Student("Shawn",99))

    for b in x:
        print(b.PrintStudentInfo())
    print(Average(x))

if __name__ == '__main__':
    main()
