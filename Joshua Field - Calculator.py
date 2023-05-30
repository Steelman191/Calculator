print("Welcome to the Cool Calculator 3000!!!")
import time;
time.sleep(0.7)
print("you can use this to calculate units!")
def main() :
    while True:
        try:
            Response = input("enter kilomters, miles, celsius, fahrenheit ")
        except ValueError:
            print("That is an invalid syntax")
        else:
            pass
        if Response == "kilometers":
            while True:
                try:
                    kilometers = float(input("Enter value in kilometers: "))
                    conv_fac = 0.621371
                    miles = km * conv_fac
                    print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
                except ValueError:
                    print("That is an invalid syntax")
                else:
                    return km
