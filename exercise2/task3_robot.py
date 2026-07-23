"""------------------------------------------------------------------------------------------------
ROBOT REVOLUTION
This program will let the robot perform action according to the instructions from a central server 
which coordinates the cleaning of the space the vacuums are deployed in.
------------------------------------------------------------------------------------------------"""

#locations in space the vacuum is deployed in, contains True if it is clean or False if it is dirty
cleaning_space = [
    [True,True,True,True,True,True,True,True,True,True],
    [True,True,False,True,True,True,True,True,True,True],
    #          ^^^^^
    [True,True,True,True,True,True,True,True,True,True],
    [True,True,True,True,True,True,True,True,True,True],
    [True,True,False,True,True,False,True,True,True,True],
    #          ^^^^^           ^^^^^
    [True,True,True,True,True,True,True,True,True,True],
    [True,True,True,True,False,True,True,True,True,True],
    #                    ^^^^^
    [True,True,True,True,True,True,True,True,True,True],
    [True,True,True,True,True,True,True,True,True,True],
    [True,True,True,True,True,True,True,True,True,True]
    ]

def turn_right(vacuum:list, compass:list)-> list:
    """
    This function will updates the facing of the vacuum by one position on the compass by turning clockwise around the compass positions
    Parameter
        vacuum : list[int|int|str]: containing the vacuum's position and direction its facing
        compass : list : The list of compass facing of the vacuum
    Return
        vacuum list[int|int|str]: containing the vacuum's position with updated direction facing
    """
    #updates the facing of the vacuum by one position on the compass. use modular to prevent the index out of range.        
    new_compass_index = (compass.index(vacuum[2]) + 1) % len(compass) 
    
    #update vacuum's direction facing
    vacuum[2] = compass[new_compass_index]

    return vacuum

def within_boundary(boundary_row: int, boundary_column:int)-> bool:
    """
    This function will get row and column and check whether the location is within cleaning_space boundary
    Parameter
        boundary_row : int : row number of location to be checked
        boundary_column : int : column number of location to be checked
    Return
        bool : True if the location is within cleaning_space boundary 
    """ 
    #Initiate the in_boundary as True 
    in_boundary = True
    
    #If any of row or column of location to be checked LEAVE cleaning_space boundary, update in_boundary to False
    if boundary_row < 0 or boundary_column < 0 or boundary_row > len(cleaning_space)-1 or boundary_column > len(cleaning_space[0])-1: 
        in_boundary = False

    return in_boundary

def vacuum_action(vacuum:list[int|int|str], action:str)->None:
    """
    This function will get instruction and update vacuum list and the cleaning_space locations according to action.
    Parameter
        vacuum : list[int|int|str]: containing the vacuum's position and direction its facing
        action : str : instruction specifying what the vacuum should do
    """ 
    
    #The list of compass facing of the vacuum 
    compass = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    
    #Initiate dictionary with key as compass direction and value as movement of row and column
    step_forward = {"N":(-1,0), "NE":(-1,1), 
                    "E":(0,1), "SE":(1,1), 
                    "S":(1,0), "SW":(1,-1), 
                    "W":(0,-1), "NW":(-1,-1)}
    
    #the row and column positions of the vacuum if step forward in the direction the vacuum compass facing. 
    update_row = vacuum[0] + step_forward[vacuum[2]][0]
    update_column = vacuum[1] + step_forward[vacuum[2]][1]
    
    #check action and perform accordingly 
    match action:

        #updates the facing of the vacuum by one position on the compass by turning anti-clockwise around the compass positions. use modular to prevent the index out of range.
        case "turn-left":
            new_compass_index = (compass.index(vacuum[2]) - 1) % len(compass)       
            #update vacuum's direction facing
            vacuum[2] = compass[new_compass_index]    
        
        #updates the facing of the vacuum by one position on the compass by turning clockwise around the compass positions 
        case "turn-right":
            turn_right(vacuum,compass)
        
        #update the current location of the vacuum in cleaning_space to True(clean) 
        case "clean":
            cleaning_space[vacuum[0]][vacuum[1]] = True

        case "forward":
            #perform turn right if step forward LEAVE bound and update compass
            if not within_boundary(update_row, update_column):
                turn_right(vacuum,compass)

            #if one step forward NOT leave bound, update location of vacuum
            else:    
                #if current location is dirty, smear the dirt into the location it ends in after the action
                if cleaning_space[vacuum[0]][vacuum[1]] == False:
                    cleaning_space[update_row][update_column] = False

                #update the vacuum's position to one step forward in the direction the vacuum compass facing 
                vacuum[0] = update_row
                vacuum[1] = update_column


def perform_cleaning(instructions:str, vacuum:list)-> None:
    """
    This function will get instruction file, read file and let robot perform instruction according to file.
    Parameter
        instructions : str : instruction file contain instructions specifying what the vacuum should do    
        vacuum : list[int|int|str]: containing the vacuum's position and direction its facing
    """
    #Initiate an empty list to store instruction_line
    instruction_list = []

    #open instructions file to read
    with open(instructions, "r") as instruction_file:
        for line in instruction_file:
            instruction_line = line.strip()
            instruction_list.append(instruction_line)
    
    #Iterate through each instruction in instruction_list and let robot perform each instruction.
    for instruction in instruction_list:
        vacuum_action(vacuum,instruction)



if __name__ == "__main__":
    test_commands = "test_commands.txt"
    vacuum = [2,2,"N"]

    print("INITIAL SPACE")
    for row_index,row in enumerate(cleaning_space):
        for col_index,cell in enumerate(row):
            if (row_index,col_index) == (vacuum[0],vacuum[1]):
                print("r",end='')
            elif cell:
                print(".",end='')
            else:
                print("d",end='')
        print()

    print("CLEANING")
    perform_cleaning(test_commands,vacuum)

    print("FINAL SPACE")
    for row_index,row in enumerate(cleaning_space):
        for col_index,cell in enumerate(row):
            if (row_index,col_index) == (vacuum[0],vacuum[1]):
                print("r",end='')
            elif cell:
                print(".",end='')
            else:
                print("d",end='')
        print()



