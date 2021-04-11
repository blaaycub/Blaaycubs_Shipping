weight = 7

# Ground Shipping
if weight < 2:
  cost_ground = weight * 1.5 + 20
elif 2 < weight <= 6:
  cost_ground = weight * 3 + 20
elif 6 < weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print(cost_ground)

# Premium Shipping
cost_ground_premium = 125
print("Ground Shipping Premium $", cost_ground_premium)

# Drone Shipping
if weight < 2:
  cost_drone = weight * 4.5
elif 2 < weight <= 6:
  cost_drone = weight * 9
elif 6 < weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print(cost_drone)