def calulate_volume_of_sphere(radius)
  pi = 3.14
  volume = pi * (4/3) * radius * radius * radius
  return volume 

radius1 = 30
volume1 = calulate_volume_of_sphere(radius1)
print(f"The volume of sphere with radius {radius1} is: {volume1}")

radius2 = 40
volume2 = calulate_volume_of_sphere(radius2)
print(f"The volume of sphere with radius {radius2} is: {volume2}")
