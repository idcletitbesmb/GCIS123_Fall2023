# Dmitry Smirnov (BRICS)


from turtle import *



# the function for cake layers
def layer(height, cake_widht, color):
     r = 20
     fillcolor(color)
     begin_fill()
     forward(cake_widht * r)
     lt(90)
     fd(height * r)
     lt(90)
     fd(cake_widht * r)
     lt(90)
     fd(height * r)
     backward(height * r)
     lt(90)
     end_fill()




#the main programm
def main():
    print('Welcome to cake constructor! ')
    cake_height = int(input('Input the height of your cake: '))
    cake_widht = int(input('Input the widht of your cake: '))
    height = 0
    layers_count = 0
    while height < cake_height:
            if layers_count == 2:
                color = input('Input the color of the next layer: ')
                layer(cake_height - height, cake_widht, color)
                break
            else: 
                #input check
                color = input('Input the color of the next layer: ')
                new_layer_height = int(input('Input the height of the next layer from 1 to ' + str(cake_height - height) + ': '))
                ok = False
                while ok == False:
                    if new_layer_height > cake_height - height:
                        new_layer_height = int(input('Too much, try again: '))
                    else: 
                        ok = True
                height += new_layer_height
                layers_count += 1
                layer(new_layer_height, cake_widht, color)
    update()
    exitonclick()


main()
    
























