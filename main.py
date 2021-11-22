# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name:str, greeting_template: str='Hello, <name>!'):
   return greeting_template.replace('<name>',name)

print(greet("Lotte"))
print(greet("Lotte",'Hi, <name>'))
print('opdracht2')
gravity = {  'sun':274,'jupiter':24.92,'neptune':11.15, 'saturn':10.44,'earth':9.798,'uranus':8.87,'venus':8.87,'mars':3.71,'mercury':3.7,'moon':1.62,'pluto':0.58 }
def force(mass:float,body:str='earth'):
   return mass*(round(gravity.get(body.lower()),1))

print(force(3,'sun'))
print(force(11,'Pluto'))
print(force(0.01,'Earth'))
print('opdracht3')

def pull(m1:float,m2:float,d:float):
   return 6.674*10**-11* ((m1*m2)/d**2)

print(pull(800,15000,3))
print(pull(0.1,5.972*10**24,6.371*10**6))




