g = 9.81
water_density = 1000


# Problem 1
# calculates the buoyancy force exerted on a object submerged in water.
def calculate_buoyancy(v, density_fluid):
    if v <= 0 or density_fluid <= 0:
        raise ValueError(
            "The volume of the object and the density of the fluid has to be greater than 0"
        )
    else:
        return v * density_fluid * g


# Problem 2
# determines whether an object will float or sink in water.
def will_it_float(v, mass):
    if v <= 0 or mass <= 0:
        raise ValueError(
            "The volume of the object and the mass of the object has to be greater than 0."
        )
    elif calculate_buoyancy(v, water_density) > mass * g:
        return True
    elif calculate_buoyancy(v, water_density) < mass * g:
        return False
    else:
        return None


# Problem 3
# calculates the pressure at a given depth in water.
def calculate_pressure(depth):
    surface_pressure = 101325
    if depth < 0:
        raise ValueError("The depth has to be greater than or equal to 0.")
    else:
        return water_density * g * depth + surface_pressure


# Problem 4
#  calculates the acceleration of an object given the force applied to it and its mass.
def calculate_acceleration(F, m):
    if m < 0:
        raise ValueError("The mass ")
    return F / m
