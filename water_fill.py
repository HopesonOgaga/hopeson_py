import math



height = input('enter height of container :')
radius = input('enter the radius :')

volume = math.pi * int(radius) ** 2 * int(height)

print(f'the volume of the water to fill the bucket: {volume}')