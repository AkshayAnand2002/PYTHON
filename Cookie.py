class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())
#cookie_one is variable name of type cookie and we are passing color green.
#which gets passed to constructor which is---
#def__init__(self,color):
#self.color=color
#cookie_two is a different variable is different cookie which is passed blue color.
#color is passed to constructor as in cookie_one.
#for get_color it is just going to return particular cookie and
#here no arguement is passed.
#set_color is for when we pass a color it is going to change the color for that
#particular cookie.
##BELOW IS THE OUTPUT OF ABOVE CODE---
#Cookie one is green
#Cookie two is blue

#Cookie one is now yellow
#Cookie two is still blue

