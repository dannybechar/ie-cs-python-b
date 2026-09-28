# Warm-up: 5 of 50 kettle drawings are electric kettles. The program says "Balanced". Find the bug.


def kettle_audit():
    traditional = 45
    electric = 5
    total = traditional + electric
    electric_share = electric / total * 100
    print("Electric kettles:", electric_share, "%")
    if electric_share > 20:
        print("Under-represented")
    else:
        print("Balanced")


# Task 1: write car_data_audit() - read how many day, night and rain images a self-driving car
# was trained on, print each group's share in %, and warn about every group under 20%.


kettle_audit()
# car_data_audit()
