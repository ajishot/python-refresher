# Problem 1
# calculates the buoyancy force exerted on a object submerged in water.
def calculate_buoyancy(v, density_fluid):
    if v <= 0 or density_fluid <= 0:
        raise ValueError(
            "The volume of the object and the density of the fluid has to be greater than 0"
        )
    else:
        return v * density_fluid * 9.81


# Problem 2
# determines whether an object will float or sink in water.
def will_it_float(v, mass):
    if v <= 0 or mass <= 0:
        raise ValueError(
            "The volume of the object and the mass of the object has to be greater than 0."
        )
    elif (
        calculate_buoyancy(v, 1000) > mass * 9.81
    ):  # 1000kg/m^3 is the density of pure water
        return True
    elif calculate_buoyancy(v, 1000) < mass * 9.81:
        return False
    else:
        return None


# Problem 3
# calculates the pressure at a given depth in water.
def calculate_pressure(depth):
    if depth < 0:
        raise ValueError("The depth has to be greater than or equal to 0.")
    else:
        return 1000 * 9.81 * depth
