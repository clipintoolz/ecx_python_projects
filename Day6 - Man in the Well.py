#!/usr/bin/env python3.10

def days_to_climb_well(well_height: int) -> None:
    """calculates how many days to climb out of a well

    Args:
        well_height (int): height / depth of well to climb
    """

    day = 0
    if well_height < 8:
        print("He is not in the well")
    else:
        while True:
            if well_height >= 8:
                well_height -= 8  # He climbs 8 metres by day
                well_height += 3  # He slips 3 metres at night
                day += 1
            else:
                day += 1
                break
        print(f"It will take {day} days for him to climb the well")


print()
print(" DAYS TO CLIMB WELL CALCULATOR ".center(50, "-"))
depth_of_well = int(input("Enter the height of the well: "))
days_to_climb_well(depth_of_well)
