import math
while True:
    print(' 1 . Do you want to calculate between 2 numbers 🔢')
    print(' 2 . Or do you want to find area of different shapes ⭕ 🔳 📐')
    print(' 3 . convert a currency 💱 💵 💴 💶 💷 💹')
    print(' 4 . Convert A Crypto To Another Crypto ₿ 💻')
    print(' 5 . Time Conversion ⏰')
    choice = int(input('Enter your choice : '))
    if choice == 2:

        print('Ok now select the shapes : ')
        print('1.Area of Circle 🔴 ')
        print('2.Area of Rectangle')
        print("3.Area of Square 🟧 ")
        print('4.Area of trapezium')
        print('5.Area of Triangle 🔺 ')
        print("6.Exit")
        print('The Availabe Choices Are : 1 , 2 , 3 , 4 , 5 , 6 . You Can Choose Any One Of Them')
        choice = int(input("Enter your choice : "))
        if choice == 1:
            radius = int(input("Enter radius of Circle : "))
            print("Area of Circle", 3.14*radius*radius)

        elif choice == 2:
            length = int(input("Enter length of Rectangle : "))
            breadth = int(input("Enter breadth of Rectangle : "))
            print("Area of Rectangle : ", length*breadth)

        elif choice == 3:
            side = int(input("Enter side of Square : "))
            print("Area:", side*side)
        elif choice == 4:
            base_1 = int(input('enter base_1 : '))
            base_2 = int(input('enter base_2 : '))
            height = int(input('enter the height : '))
            print('Area of Trapezium is ', ((base_1+base_2)*height)/2)
        elif choice == 5:
            side_a = int(input('enter a side 1 : '))
            side_b = int(input('enter a side 2 : '))
            side_c = int(input('enter a side 3 : '))
            semi_perimeter = side_a + side_b + side_c / 2
            Area = math.sqrt(semi_perimeter*(semi_perimeter - side_a)
                             * (semi_perimeter - side_b)*(semi_perimeter - side_c))
            print('Area of a triangle :', Area)

        elif choice == 6:
            break
        else:
            print("Choose the choice from above")

        repeat = input("Do you want to continue? (y/n) : ")
        if repeat == 'n' or repeat == 'N':
            break

    if choice == 1:

        print('So what do you want to do now ? ')
        print(' A . Perform Addition Between Two Numbers !  1️⃣  ➕ 2️⃣')
        print(' B . Perform Subtraction Between Two Numbers !  1️⃣  ➖ 2️⃣')
        print(' C . Perform Multiplication Between Two Numbers !  1️⃣  ➗ 2️⃣')
        print(' D . Perform Division Between Two Numbers !  1️⃣  ✖️ 2️⃣')
        print(' E . Find Square Of Two Numbers !    🌟🌟 2️⃣')
        print(' F . Find Cube Of Two Numbers !    🌟🌟 3️⃣')
        print(' G . Find Square Root Of Two Numbers !  1️⃣  √ 2️⃣')
        print(' H . Perform Floor Division Between Two Numbers !  1️⃣  // 2️⃣')
        print(' I . Exit !')
        print('Ok , Now Enter Those Two Numbers You want To Perform The Calculations')
        num_1 = int(input('Enter Number 1 : '))
        num_2 = int(input('Enter Number 2 : '))
        print('The Two Numbers Are', num_1, 'and', num_2)
        print('The Availabe Choices Are : 1 (➕) , 2 (➖), 3 (➗), 4 (✖️ ), 5 (🌟🌟 2️⃣ ), 6 (🌟🌟 3️⃣ ), 7 (√), 8 (//), 9 (❌). You Can Choose Any One Of Them')
        choice = int(input('Enter Your Choice : '))

        if choice == 1:
            sum_of_numbers = num_1 + num_2
            print('The Sum Of Two Numbers Are : ', sum_of_numbers)

        elif choice == 2:
            diff_of_numbers = num_1 - num_2
            print('The Difference Of Two Numbers Are : ', diff_of_numbers)

        elif choice == 3:
            prod_of_numbers = num_1 * num_2
            print('The Product Of Two Numbers Are : ', prod_of_numbers)
        elif choice == 4:
            div_of_numbers = num_1 / num_2
            print('The Division Of Two Numbers Are : ', div_of_numbers)
        elif choice == 5:
            sqre_of_numbers = num_1 ** 2, num_2 ** 2
            print('The Square Of Two Numbers Are : ', sqre_of_numbers)
        elif choice == 6:
            cube_of_numbers = num_1 ** 3,  num_2 ** 3
            print('The Cube Of Two Numbers Are : ', cube_of_numbers)
        elif choice == 7:
            sqrt_of_numbers = math.sqrt(num_1), math.sqrt(num_2)
            print('The Square Root Of Two Numbers Are : ', sqrt_of_numbers)
        elif choice == 8:
            flrdiv_of_numbers = num_1 // num_2
            print('The Floor Divsion Between Two Numbers Are : ', flrdiv_of_numbers)

        elif choice == 9:
            break

        else:
            print("Choose the choice from above")

        repeat = input("Do you want to continue? (y/n) : ")
        if repeat == 'n' or repeat == 'N':
            break
    if choice == 3:
        print('Here are the currencies available for conversion')
        print(' 1 .  INR To USD')
        print(' 2 .  INR To GBP')
        print(' 3 .  INR To SGD')
        print(' 4 .  INR To YEN')
        print(' 5 .  INR To KWD')
        print(' 6 .  USD To SGD')
        print(' 7 .  USD To GBP')
        print(' 8 .  USD To KWD')
        print(' 9 .  USD To YEN')
        print(' 10 . USD To AUD')
        choice = int(input('Enter Your Choice : '))
        if choice == 1:
            amt = int(input('Enter The Amount You Want To Convert : '))
            Inr_Usd = amt*0.012153876
            print(amt, 'Rupees Converted To USD ----->', Inr_Usd, '💲💵')
        elif choice == 2:
            amt = int(input('Enter The Amount You Want To Convert : '))
            Inr_Gbp = amt*0.0099477166
            print(amt, 'Rupees Converted To GBP ----->', Inr_Gbp, '￡💷')
        elif choice == 3:
            amt = int(input('Enter The Amount You Want To Convert : '))
            Inr_Sgd = amt*0.0164465764
            print(amt, 'Rupees Converted To SGD ----->', Inr_Sgd, '💲💵')
        elif choice == 4:
            amt = int(input('Enter The Amount You Want To Convert : '))
            Inr_Yen = amt*1.6591559967
            print(amt, 'Rupees Converted To YEN ----->', Inr_Yen, '¥💴')
        elif choice == 5:
            amt = int(input('Enter The Amount You Want To Convert : '))
            Inr_KWd = amt*0.0037280921
            print(amt, 'Rupees Converted To KWD ----->', Inr_KWd, '💲💵')
        elif choice == 6:
            amt = int(input('Enter The Amount You Want To Convert : '))
            Usd_Sgd = amt*1.353196
            print(amt, 'USD Converted To SGD ----->', Usd_Sgd, '💲💵')
        elif choice == 7:
            amt = int(input('Enter The Amount You Want To Convert : '))
            Usd_Gbp = amt*0.81354292
            print(amt, 'USD Converted To GBP ----->', Usd_Gbp, '￡💷')
        elif choice == 8:
            amt = int(input('Enter The Amount You Want To Convert : '))
            Usd_Kwd = amt*0.30674264
            print(amt, 'USD Converted To KWD ----->', Usd_Kwd, '💲💵')
        elif choice == 9:
            amt = int(input('Enter The Amount You Want To Convert : '))
            Usd_Yen = amt*136.27019
            print(amt, 'USD Converted To YEN ----->', Usd_Yen, '¥💴')
        elif choice == 10:
            amt = int(input('Enter The Amount You Want To Convert : '))
            Usd_Aud = amt*1.4778516
            print(amt, 'USD Converted To AUD ----->', Usd_Aud, '¥💴')

        repeat = input("Do you want to continue? (y/n) : ")
        if repeat == 'n' or repeat == 'N':
            break
    if choice == 4:
        print('ENTER THE CRYPTO YOU WANT TO CONVERT : ')
        print(' 1 . BTC TO ETH')
        print(' 2 . BTC TO DOGE')
        print(' 3 . ETH TO DOGE')
        print(" 4 . ETH TO BTC")
        print(" 5 . LTC TO ETH")
        print(" 6 . LTC TO BTC")
        choice = int(input('Enter Your Choice : '))
        if choice == 1:
            amt = int(input('Enter The Amount Of Crypto You Want To Convert : '))
            BTC_ETH = amt*13.48372179
            print(amt, 'BTC Converted To ETH ----->', BTC_ETH)
        elif choice == 2:
            amt = int(input('Enter The Amount Of Crypto You Want To Convert : '))
            BTC_DOGE = amt*176, 588
            print(amt, 'BTC Converted To DOGE ----->', BTC_DOGE)
        elif choice == 3:
            amt = int(input('Enter The Amount Of Crypto You Want To Convert : '))
            ETH_DOGE = amt*13, 102
            print(amt, 'ETH Converted To DOGE ----->', ETH_DOGE)
        elif choice == 4:
            amt = int(input('Enter The Amount Of Crypto You Want To Convert : '))
            ETH_BTC = amt*0.07421936
            print(amt, 'ETH Converted To BTC ----->', ETH_BTC)
        elif choice == 5:
            amt = int(input('Enter The Amount Of Crypto You Want To Convert : '))
            LTC_ETH = amt*0.06031075
            print(amt, 'LTC Converted To ETH ----->', LTC_ETH)
        elif choice == 6:
            amt = int(input('Enter The Amount Of Crypto You Want To Convert : '))
            LTC_BTC = amt*0.00447724
            print(amt, 'LTC Converted To BTC ----->', LTC_BTC)
        repeat = input("Do you want to continue? (y/n) : ")
        if repeat == 'n' or repeat == 'N':
            break
    if choice == 5:
        print(' 1 . Seconds To Milliseconds')
        print(' 2 . Seconds To Minutes')
        print(' 3 . Seconds To Hours')
        choice = int(input('Enter The Choices : '))
        if choice == 1:
            Time = int(input('Enter The Amount Of Time You Want To Convert : '))
            SEC_MILISEC = Time*1000
            print(Time, 'SEC Converted To MILLISEC ----->',
                  SEC_MILISEC, 'MILLISECONDS')
        elif choice == 2:
            Time = int(input('Enter The Amount Of Time You Want To Convert : '))
            SEC_MIN = Time*0.01666667
            print(Time, 'SEC Converted To MIN ----->', SEC_MIN, 'MINUTES')
        elif choice == 3:
            Time = int(input('Enter The Amount Of Time You Want To Convert : '))
            SEC_HRS = Time*0.00027778
            print(Time, 'SEC Converted To HRS ----->', SEC_HRS, 'HOURS')
        result = input('Do You Want To Continue ?(y/n) : ')
        if result == 'n' or 'N':
            break
print('THANK YOU 🙏🙏 FOR USING THIS PROJECT !!!')

# bykarthi:)
