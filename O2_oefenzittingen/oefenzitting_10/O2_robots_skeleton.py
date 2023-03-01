#
# PROCEDURAL CODE
#

# A legion contains a number of robots that are identified by a number.
legion = [1357, 2468, 2580]

# print("Robots in legion:")
# for robot in legion:
#     print("Hello, I'm " + str(robot) + ".")


#
# OBJECT-ORIENTED CODE
#

# Robot: The Robot class is the blueprint of a single robot. Upon creation, a robot is assigned its identifier, which is stored as an attribute of its class.
#           Make sure that this identifier is an integer. Define a method `say_hello` in which the robot presents itself as in the procedural example.
# Legion: The legion-class contains a list of Robot-instances.
#           Define a method `add_robot` to add a new Robot to the list
#           and another method `present` that invokes the `say_hello` method of all robots in this legion.

class Robot:
    def __init__(self,identifier):
        self.__identifier = identifier

    def sayhello(self):
        print("Hello, I'm " + str(self.__identifier) + ".")

class Legion:
    def __init__(self):
        self.robots = list()

    def add_robot(self,robot):
        self.robots.append(robot)

    def present(self):
        for robot in self.robots:
            robot.sayhello()

## Uncomment the lines below when the respective classes are written.

l = Legion()
# Add robots that are identified by a number.
l.add_robot(Robot(1357))
l.add_robot(Robot(2468))
l.add_robot(Robot(2580))
# Add robots that are identified by a name.
l.add_robot(Robot("R2D2"))
l.add_robot(Robot("C3PO"))
l.present()