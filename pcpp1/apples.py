import random

class Apple:
    apple_counter = 0
    total_weight = 0
    lower_bound = 0.2
    upper_bound = 0.5
    max_weight = 300
    max_apples = 1000
    limit_reached = False
    
    def __init__(self):
        Apple.apple_counter += 1
        self.apple_weight = random.uniform(Apple.lower_bound, Apple.upper_bound)
        Apple.total_weight += self.apple_weight
        if(Apple.total_weight > Apple.max_weight or Apple.apple_counter > Apple.max_apples):
            Apple.total_weight -= self.apple_weight
            Apple.apple_counter -= 1
            print(f'Apples: {Apple.apple_counter}, Weight: {Apple.total_weight}')
            Apple.limit_reached = True

class Packager:
    def __init__(self) -> None:
        self.apple_list = []
        while not Apple.limit_reached:
            a = Apple()
            self.apple_list.append(a)

p = Packager()