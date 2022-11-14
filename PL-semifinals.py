print('AIRLINE SEAT RESERVATION SYSTEM')

lists = list()
for i in range(1, 81):
    lists.append(i)
    fullname = list()
for j in range(1, 81):
    fullname.append(j)
    age = list()
for k in range(1, 81):
    age.append(k)
    gender = list()
for i in range(1, 81):
    gender.append(i)
    r = 1
while r !=0:

        print("\n\n=======================================================")
        print("\n1. Seat Reservation")
        print("2. Check Reserved Seat/s")
        print("3. Check Customers' Status")
        print("4. Cancel Reservation")
        print("5. Quit\n")
        print("=======================================================")

        option = int(input("\nEnter your option: "))
        print("\n")

        if option == 1:
            seat = int(input('Enter seat number you want: '))
            
            if lists[seat-1] == seat:
                fullname1 = str(input('Enter your fullname: '))
                age1 = int(input('Enter your age: '))
                gender1 = str(input('Enter your gender: '))
                lists.pop(seat-1)
                fullname.pop(seat-1)
                age.pop(seat-1)
                gender.pop(seat-1)
                
                lists.insert(seat-1, 'Reserved Seat')
                fullname.insert(seat-1, fullname1)
                age.insert(seat-1, age1)
                gender.insert(seat-1, gender1)
                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print("        Your Seat is Reserved :)")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

            else:
                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print("     Seat is already taken, please try any other seat/s.")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        elif option == 2:
            print("Available Seat:\n")
            for k in lists:
                print(k, end=" ")

        elif option == 3:
            seatr = int(input('Enter your preferred seat number: '))
            seatr = seatr-1

            if fullname[seatr] == seatr+1:
                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print("        Seat is Available.")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                
            else:
                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('This seat is reserved by:')
                print('Name: ', fullname[seatr].title())
                print('Age: ', age[seatr])
                print('Gender: ', gender[seatr].title())
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        elif option == 4:
            seat = int(input('Enter your seat number: '))

            if lists[seat-1] == seat:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print("   You haven't reserved your seat yet.")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

            else:
                lists.pop(seat-1)
                lists.insert(seat-1, seat)
                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print("      Your Seat Reservation is Cancelled.")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                
        elif option == 5:
            r = 0
            exit()

        else:
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("      Please enter correct key.")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
