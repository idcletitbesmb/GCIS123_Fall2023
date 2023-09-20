# Dmitry Smirnov (BRICS)





from turtle import *



# the function to draw cake layer(rectangle)
def layer(new_layer_height, cake_widht, color):
     r = 20 #coefficent to make the picture bigger
     fillcolor(color)
     begin_fill()
     forward(cake_widht * r)
     lt(90)
     fd(new_layer_height * r)
     lt(90)
     fd(cake_widht * r)
     lt(90)
     fd(new_layer_height * r)
     backward(new_layer_height * r)
     lt(90)
     end_fill()



#the check if input is valid
def input_validity_check(new_layer_height, cake_height, height):
    if new_layer_height > cake_height - height:
         return False
    return True



#the main programm
def main():
    print('Welcome to cake constructor! ')
    cake_height = int(input('Input the height of your cake: ')) #
    cake_widht = int(input('Input the widht of your cake: '))
    height = 0 #the height of the drawn part of the cake 
    layers_count = 0 #number of drawn layers
    while height < cake_height:
            if layers_count == 4: # we decided to set the maximum number of layers for 5, so if on this if-check the number of layers is 4, it means that there is only one left
                color = input('Input the color of the last layer: ')
                layer(cake_height - height, cake_widht, color)
                break
            else: 
                color = input('Input the color of the next layer: ')
                new_layer_height = int(input('Input the height of the next layer from 1 to ' + str(cake_height - height) + ': '))
                while input_validity_check(new_layer_height, cake_height, height) == False: #checks if input is valid. If not, asks a new input until it is valid
                    new_layer_height = int(input('Too much, try again: '))
                height += new_layer_height #if input is valid, then the height of the drawn part increases by the height of the new layer
                layers_count += 1 
                layer(new_layer_height, cake_widht, color) #draws the new layer
    update()
    exitonclick()


main()
    
























