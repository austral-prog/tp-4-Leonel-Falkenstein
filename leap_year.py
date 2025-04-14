def leap_year():
                x= int(input("ingrese un año: "))

                if  (x%4==0 and x%100!=0 ):
                    print (f"El año {x} es bisiesto")

                elif  (x%400==0):
                    print (f"El año {x} es bisiesto")

                else:
                    print(f"El año {x} no es bisiesto")
