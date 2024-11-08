def feet_to_steps(user_feet):
   #write your code here
   steps_per_foot = 1/2.5
   return int(user_feet * steps_per_foot)

if __name__ == '__main__':
    #take input feet steps here
    #store it into the function
    user_feet = float(input())
    steps = feet_to_steps(user_feet)
    #print your steps here
    print(f'{steps}')
    feet_to_steps(5280)