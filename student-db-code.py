d = {}
ch = 'y'
while ch in 'Yy':
    print('''The Functions are
    1. Add new student
    2. Edit student detail
    3. Delete a student record
    4. Display student list
    5. Search details according to adm no.
    6. To calculate no. of students having percent between a range''')
    n = int(input('Enter choice: '))
    if n==1:
        k = int(input('Adm no.: '))
        n = input('Name: ')
        c = int(input('Class: '))
        p = int(input('Percent: '))
        v = [n, c, p]
        d[k] = v
    elif n==2:
        print("You can change name, class & percent")
        ad = int(input('Enter adm no.: '))
        c = int(input('Enter class: '))
        p = int(input('Enter percent: '))
        n = input('Enter new name: ')
        l = [n, c, p]
        d[ad] = l
    elif n==3:
        dd = int(input('Enter student database to be deleted: '))
        del d[dd]
        print("the database has been deleted")
    elif n==4:
        for i in d:
            print(i, d[i])
    elif n==5:
        cd=int(input('Enter adm no.: '))
        print(d.get(cd))
    elif n == 6:
        c=0
        r1=int(input('Enter range 1: '))
        r2=int(input('Enter range 2: '))
        for k in d:
            percent=d[k][2]
            if r1 <= percent <= r2:
                c=c+1
        print('The no of students having marks between', r1, 'and', r2, 'are', c)
    ch=input('Do you want to continue (y/n)? ')
print('Thank you!')
