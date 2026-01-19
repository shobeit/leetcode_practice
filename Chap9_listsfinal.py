def check_ingredient_match(recipe, inventory):
    missing_ingredient = []
    for items in recipe:
        
        if items in inventory:
            continue
        else:
            missing_ingredient.append(items)

    percentage = ((len(recipe) - len(missing_ingredient)) / len(recipe)) *100
    
    return(percentage, missing_ingredient)