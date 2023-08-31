# Points data (X, Y, Number, Direction): (28, 42, 1, North), (27, 46, 2, East), (16, 22, 3, South), (40, 50, 4, West), (8, 6, 5, North),  (6, 19, 6, East), (28, 5, 7, South), (39, 36, 8, West), (12, 34, 9, North), (36, 20, 10, East), (22, 47, 11, South), (33, 19, 12, West), (41, 18, 13, North), (41, 34, 14, East),  (14, 29, 15, South), (6, 49, 16, West), (46, 50, 17, North), (17, 40, 18, East), (28, 26, 19, South), (2, 12, 20, West)
# Given the data above, make a function where given a Point value returns all points in a visible cone that extends in the direction given a visible cone value made up of degrees and maximum direction. For instance, the function VisiblePoints(1,45,20) returns an array with one object (27,46,2,East)
# The function should be able to handle any number of points and any number of visible cones.

import math

# Function to calculate the angle between two points
def angle_between_points(x1, y1, x2, y2):
    angle = math.atan2(y2 - y1, x2 - x1)
    return math.degrees(angle)  # Convert radians to degrees

def VisiblePoints(center_x, center_y, cone_degrees, max_direction, points):
    # Create a list to store the visible points
    visible_points = []
    half_cone = cone_degrees / 2
    # Loop through all the points
    for x, y, number, direction in points:
        # Calculate the angle between the center point and the current point
        angle = angle_between_points(center_x, center_y, x, y)
        # Calculate the difference between the current point's angle and the direction
        angle_diff = abs(angle - direction)
        # If the difference is greater than 180, subtract 360 from the difference
        if angle_diff > 180:
            angle_diff = 360 - angle_diff
        # If the difference is less than or equal to half the cone, add the point to the visible points list
        if angle_diff <= half_cone:
            visible_points.append((x, y, number, direction))

    return visible_points

# Create a list of points
visible_points = [
    (28, 42, 1, "North"),
    (27, 46, 2, "East"),
    (16, 22, 3, "South"),
    (40, 50, 4, "West"),
    (8, 6, 5, "North"),
    (6, 19, 6, "East"),
    (28, 5, 7, "South"),
    (39, 36, 8, "West"),
    (12, 34, 9, "North"),
    (36, 20, 10, "East"),
    (22, 47, 11, "South"),
    (33, 19, 12, "West"),
    (41, 18, 13, "North"),
    (41, 34, 14, "East"),
    (14, 29, 15, "South"),
    (6, 49, 16, "West"),
    (46, 50, 17, "North"),
    (17, 40, 18, "East"),
    (28, 26, 19, "South"),
    (2, 12, 20, "West"),
] # (x, y, number, direction)

