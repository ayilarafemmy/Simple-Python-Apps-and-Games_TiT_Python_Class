temperature = 5

if temperature > 30: #30 -infinity
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:  # (20, 30]
    print("It's a nice day")
elif temperature > 10: #(10, 20]
    print("It's a cold day")
else: #<10
    print("It's very cold")
print("Done")
