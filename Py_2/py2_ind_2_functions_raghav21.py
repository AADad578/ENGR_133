import math

def convert_ft3_to_gal(vol):
    return vol*7.48

def checkDimensions(*args):
    for i in args:
        if i<0:
            print("Please enter valid dimensions.")
            return True
    return False
    

def standard(L1, L2, Ds, Dd):
    # Ensure all valid inputs
    if checkDimensions(L1, L2, Ds, Dd):
        return None
    
    volume = 0
    # Main rectangular area
    volume += L1*L2*Ds
    
    # Small Triangular area
    volume += (L1/3.0)*L2*(Dd-Ds)
    
    return convert_ft3_to_gal(volume)
    
def ramp(L1, L2, Ds, Dd):
    # Ensure all valid inputs
    if checkDimensions(L1, L2, Ds, Dd):
        return None    
    volume = 0
    
    #First Triangular Area
    volume += .5*(L1/3.0)*Ds*L2
    
    #Rectangular area over 2nd and 3rd sections
    volume += (L1*2.0/3.0)*Ds*L2
    
    #Triangular area in 3rd section
    volume += .5*(L1/3.0)*(Dd-Ds)*L2
    
    return convert_ft3_to_gal(volume)
    
def round(L1, L2, Ds, Dd):
    # Ensure all valid inputs
    if checkDimensions(L1, L2, Ds, Dd):
        return None

    volume = 0
    
    #main circular section
    volume += math.pi*(L1**2)*Ds
    
    #the bottom section as a truncated cone
    volume += (1/3.0) * math.pi * (Dd-Ds) * (L2**2 + L2 * L1 + L1**2)
    
    return convert_ft3_to_gal(volume)