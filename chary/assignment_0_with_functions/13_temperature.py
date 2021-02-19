#WAP to read temperature in centigrade & display a suitabel message
#according to temperature state below.
def temperature_state(temp): 
    if(temp<0):
        print("Freezing weather")
    if(temp>=0 and temp<10):
        print("Very cold weather")
    if(temp>=10 and temp<20):
        print("Cold weather")
    if(temp>=20 and temp<30):
        print("Normal in Temperature")
    if(temp>=30 and temp<40):
        print(" Temperature is Hot")
    if(temp>=40):
        print("Temperature is Very Hot")

temp=int(input("Enter the Temperature in centigrade :"))
temperature_state(temp)
