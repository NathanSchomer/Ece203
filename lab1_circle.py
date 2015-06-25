my_radius = 27

def circle_area(radius):
    
    print "\nmy_radius & radius are bound to the same object ", my_radius is radius
   
    radius = radius + 1
    print "\nradius was incremented by one and now equals ", radius
    print "my_radius now equals ", my_radius 

    pi = 3.141
    area = pi*radius**2
    return area

my_area = circle_area(my_radius)
print "\nMy circle has radius %s and area %s" % (my_radius, my_area)
print "\n"
