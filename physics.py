import numpy as np

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
# F is the force applied to the object in Newtons
# m is the mass of object in kilograms
def calculate_acceleration(F, m):
    if m <= 0:
        raise ValueError("The mass has to be greater than zero")
    return F / m


# Problem 5
# calculates the angular acceleration of an object given the torque applied to it and its moment of inertia.
# tau is the torque applied to the object in Newton-meters
# I is the moment of inertia of the object in kg m^2
def calculate_angular_acceleration(tau, I):
    if tau < 0 or I <= 0:
        raise ValueError("The moment of inertia has to be greater than zero")
    return tau / I


# Problem 6
# calculates the torque applied to an object given the force applied to it and the distance from the axis of rotation to the point where the force is applied.
# F_magnitude is the magnitude of force applied to the object in Newtons.
# F_direction is the direction of the force applied to the object in degrees.
# r is the distance from the axis of rotation to the point where the force is applied in meters.
def calculate_torque(F_magnitude, F_direction, r):
    if F_magnitude < 0 or r < 0:
        raise ValueError(
            "The magnitude of the force applied and radius has to be greater than or equal to zero."
        )
    return r * F_magnitude * np.sin(np.radians(F_direction))


# Problem 7
# calculates the moment of inertia of an object given its mass and the distance from the axis of rotation to the center of mass of the object.
# m is the mass of the object in kilograms
# r is the distance from the axis of rotation to the center of mass of the object in meters
def calculate_moment_of_inertia(m, r):
    if m <= 0 or r < 0:
        raise ValueError(
            "The mass of the object must be greater than zero and the radius has to be greater than or equal to zero."
        )
    return m * np.power(r, 2)


# Problem 8-1
# calculates the acceleration of the AUV in the 2D plane.
# F_magnitude is the magnitude of force applied by the thruster in Newtons.
# F_angle is the angle of the force applied by the thruster in radians.
# mass is the mass of the AUV in kilograms. The default value is 100kg.
# volume is the volume of the AUV in cubic meters. The default value is 0.1m^3.
# thruster_distance is the distance from the center of mass of the AUV to the thruster in meters. The default value is 0.5m.
def calculate_auv_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5
):
    if F_magnitude < 0 or mass <= 0 or volume <= 0 or thruster_distance < 0:
        raise ValueError("Invalid input.")
    x_acceleration = calculate_acceleration(F_magnitude * np.cos(F_angle), mass)
    y_acceleration = calculate_acceleration(F_magnitude * np.sin(F_angle), mass)
    acceleration = np.array([x_acceleration, y_acceleration])
    return acceleration


# Problem 8-2
# calculates the angular acceleration of the AUV.
# F_magnitude is the magnitude of force applied by the thruster in Newtons.
# F_angle is the angle of the force applied by the thruster in radians.
# inertia is the moment of inertia of the AUV in kg m^2. The default value is 1kg m^2.
# thruster_distance is the distance from the center of mass of the AUV to the thruster in meters. The default value is 0.5m.
def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    if F_magnitude < 0 or inertia <= 0 or thruster_distance < 0:
        raise ValueError("Invalid input.")
    torque = thruster_distance * F_magnitude * np.sin(F_angle)
    return calculate_angular_acceleration(torque, inertia)


# Problem 9-1
# calculates the acceleration of the AUV in the 2D plane.
# T is an np.ndarray of the magnitudes of the forces applied by the thrusters in Newtons.
# alpha is the angle of the thrusters in radians.
# mass is the mass of the AUV in kilograms. The default value is 100kg.
def calculate_auv2_acceleration(T, alpha, mass=100):
    if not isinstance(T, np.ndarray):
        raise TypeError(
            "T is an np.ndarray of the magnitudes of the forces applied by the thrusters in Newtons."
        )
    if T.size != 4:
        raise ValueError("T must have 4 values")
    if mass <= 0:
        raise ValueError("Mass must be greater than zero.")

    force_robot = (
        np.array(
            [
                [np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
                [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)],
            ]
        )
        @ T
    )
    rotation_matrix = np.array(
        [[np.cos(alpha), np.sin(alpha)], [-np.sin(alpha), np.cos(alpha)]]
    )
    force_universal = rotation_matrix @ force_robot

    acceleration_universal = force_universal / mass

    return acceleration_universal


# Problem 9-2
# calculates the angular acceleration of the AUV.
# T is an np.ndarray of the magnitudes of the forces applied by the thrusters in Newtons.
# alpha is the angle of the thrusters in radians.
# L is the distance from the center of mass of the AUV to the thrusters in meters.
# l is the distance from the center of mass of the AUV to the thrusters in meters.
# inertia is the moment of inertia of the AUV in kg m^2. The default value is 100kg m^2
def calculate_auv2_angular_accelration(T, alpha, L, l, inertia=100):
    if not isinstance(T, np.ndarray):
        raise TypeError(
            "T is an np.ndarray of the magnitudes of the forces applied by the thrusters in Newtons."
        )
    if L <= 0 or l <= 0 or inertia <= 0:
        raise ValueError("Invalid input.")
    radius = np.sqrt(np.power(L, 2), np.power(l, 2))
    beta = np.arctan(l / L)
    np.reshape(T, 4)
    directions = np.array([[1], [-1], [1], [-1]])

    torque = radius * np.sin(alpha + beta) * T @ directions

    return torque / inertia
