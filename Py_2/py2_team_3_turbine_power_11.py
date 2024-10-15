import math as m 
def turbine_power(air_density, blade_length, velocity_wind, power_coefficient):
    
    # if it's below 4 no energy generated
    if(velocity_wind<4):
        print("Error, velocity is too low, no power generated")
        return 0
    
    # if it's above 20 no energy generated
    if(velocity_wind>20):
        print("Error, velocity is too high, no power generated")
        return 0
    
    # calculate power generated
    power = 0.5 * air_density * (m.pi * (blade_length**2)) * (velocity_wind ** 3) * power_coefficient
    
    # return power
    return power 