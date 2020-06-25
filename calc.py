def multiplica():
    one = int(input('1º: '))
    two = int(input('2º: '))

    print('a multiplicação é: ', one*two)

def soma():
    one = int(input('1º: '))
    two = int(input('2º: '))

    print('a soma é: ', one+two)
    
def subtra():
    one = int(input('1º: '))
    two = int(input('2º: '))

    print('a subtração é: ', one-two)

ans=True
while ans:
    print ("""
    1.Multiplicação
    2.Soma
    3.Subtração
    4.Exit/Quit
    """)
    ans= int(input("What would you like to do? "))
    if ans==  1: 
      multiplica() 
    elif ans== 2:
      print("\n Student Deleted") 
    elif ans== 3:
      print("\n Student Record Found") 
    elif ans== 4:
      print("\n Goodbye") 
      exit()
    else:
      print("\n Not Valid Choice Try again") 

