breakfasts = ["eggs", "oats", "sprouts"]
lunches = ["dosa", "rice", "cereals"]
dinners = ["bottle gourd", "Soya bean", "lentils"]
for breakfast,lunch,dinner in zip(breakfasts,lunches,dinners):
    print(f"My diet for today was {breakfast}, {lunch} and {dinner}")