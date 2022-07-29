#!/usr/bin/env python3.10


def hcf(*args: int) -> None:
    """determines the highest common factor between two or more numbers"""
    
    factors = []
    if len(args) < 2:
        print("Enter two or more numbers")
        
    else:
        for divisor in range(1, max(args)):
            
            # divides each number in args by divisor and maps their remiander into an iterable (factor)
            factor = map(lambda dividend: dividend % divisor, args)
            
            # checks if divisor is a factor of each number in args
            if sum(factor) == 0:
                factors.append(divisor)
                
    gcd = max(factors)
    print(f"Highest Common Factor of {args} is {gcd}")


print()
print(" EUCLID'S ALGORITHM (GCD) ".center(50, "-"))
numbers = (input("To get the highest common factor (HCF), enter numbers seperated by commas\n-> ")).split(",")
numbers = [int(number) for number in numbers]
hcf(*numbers)
