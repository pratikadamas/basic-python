
        # DYNAMIC BINDUNG
class shape:
   def draw(self):
      print ("draw method")

class circle(shape):
   def draw(self):
      print ("Draw a circle")

class rectangle(shape):
   def draw(self):
      print ("Draw a rectangle")

print("     USING LIST     ")
shapes = [shape(),circle(), rectangle()]

 # here in every iteration "shp" object type is different  ( DYNAMIC TYPE OH "SHP" CHANGE)

for shp in shapes:
   shp.draw()
print("     USING TUPLE    ")

Shape=(shape(),circle(),rectangle())
for shp in Shape:
   shp.draw()

   # list and tuple hele dynamic binding using loops