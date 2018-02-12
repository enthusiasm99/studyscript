points = [{'x':2, 'y':3},
          {'x':4, 'y':1}]
# print(points['y'])

points.sort(key= lambda i:i['y'])
print(points)