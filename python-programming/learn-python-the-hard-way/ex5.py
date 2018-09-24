name = "Carl Centola"
age = 28
height = 70
height_cm = height * 2.5400013716
weight = 180
weight_kg = weight * 0.453592
eyes = "green"
teeth = "white"
hair = "black"

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} ponds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usuually {teeth} depending on the coffee.")

total = age + height + weight # US
total_metric = age + height_cm + weight_kg #metric

print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"Using the metric system, my total would be {round(total_metric)}.")
