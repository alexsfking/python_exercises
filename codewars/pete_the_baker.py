def cakes(recipe, available):
    num_cakes=0
    while(True):
        for ingredient,amount in recipe.items():
            if ingredient not in available:
                return num_cakes
            else:
                available[ingredient]-=amount
                if(available[ingredient]<0):
                    return num_cakes
        num_cakes+=1