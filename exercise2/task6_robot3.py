"""----------------------------------------------------------------------------------------------------
SCRUB A' DUB DUB
This program will let the robot perform action according to the instructions from a central server 
which coordinates the cleaning of the space the vacuums are deployed in. Taking in the consideration 
about obstructions inside the space, multiple ways to be dirty and clean and multiple robot vacuums 
working in the same space.
----------------------------------------------------------------------------------------------------"""

#locations in space the vacuum is deployed in, contains None if clean or "d" if dirty or "l" if water or "s" if soap 
cleaning_space = [
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,"d" ,None,None,None,None,None,None,None],
    [None,None,None,None,"s" ,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,"d" ,None,None,"l" ,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,"l" ,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None]
    ]

#locations in space the vacuum is deployed in, contains "r" for robot, "c" for cat, "w" for wall, None for nothing
obstruction_space = [
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,"c" ,None,None,None,None,None],
    [None,None,"r" ,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,"w" ,None,None,None],
    [None,None,None,None,"r" ,None,None,None,None,None],
    [None,"w" ,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    ]

def turn_left(vacuum:list, compass:list)->list:
    """
    This function will updates the facing of the vacuum by one position on the compass by turning anti-clockwise around the compass positions
    Parameter
        vacuum : list[int|int|str]: containing the vacuum's position and direction its facing
        compass : list : The list of compass facing of the vacuum
    Return
        vacuum list[int|int|str]: containing the vacuum's position with updated direction facing
    """
    #updates the facing of the vacuum by one position on the compass. use modular to prevent the index out of range.
    new_compass_index = (compass.index(vacuum[2]) - 1) % len(compass)      
    
    #update vacuum's direction facing
    vacuum[2] = compass[new_compass_index] 
    
    return vacuum

def turn_right(vacuum:list, compass:list)->list:
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

def check_wall(wall_row:int, wall_column:int)-> bool:
    """
    This function will get row and column and check whether the location have wall
    Parameter
        wall_row : int : row number of location to be checked
        wall_column : int : column number of location to be checked
    Return
        bool : True if the location have wall
    """ 
    #Initiate the have_wall as False
    have_wall = False

    #if there is wall, update have_wall to True 
    if obstruction_space[wall_row][wall_column] == "w":
        have_wall = True
    
    return have_wall

def check_robot(robot_row:int, robot_column:int)-> bool:
    """
    This function will get row and column and check whether the location have robot
    Parameter
        robot_row : int : row number of location to be checked
        robot_column : int : column number of location to be checked
    Return
        bool : True if the location have robot
    """ 
    #Initiate the meet_robot as False
    meet_robot = False
    
    #if there is robot, update meet_robot to True 
    if obstruction_space[robot_row][robot_column] == "r":
        meet_robot = True
    
    return meet_robot
    
def vacuum_action(vacuum:list[int|int|str], action:str)-> str:
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

        #updates the facing of the vacuum by one position on the compass by turning anti-clockwise around the compass positions
        case "turn-left":
            turn_left(vacuum,compass)
        
        #updates the facing of the vacuum by one position on the compass by turning clockwise around the compass positions 
        case "turn-right":
            turn_right(vacuum,compass)
        
        #update the current location of the vacuum in cleaning_space to None(clean) if the current location is dirty
        case "clean": 
            if cleaning_space[vacuum[0]][vacuum[1]] == "d":
                cleaning_space[vacuum[0]][vacuum[1]] = None
        
        #update the current location of the vacuum in cleaning_space to None(clean) if the current location is water
        case "mop":
            if cleaning_space[vacuum[0]][vacuum[1]] == "l":
                cleaning_space[vacuum[0]][vacuum[1]] = None

        case "forward":

            #perform turn right if step forward LEAVE bound and update compass
            if not within_boundary(update_row, update_column):
                turn_right(vacuum,compass)
                action='turn-right'

            # if step forward meet the wall, robot turn right
            elif check_wall(update_row, update_column):
                turn_right(vacuum,compass)
                action='turn-right'

            # if step forward meet the robot, robot turn left
            elif check_robot(update_row, update_column):
                turn_left(vacuum,compass)
                action='turn-left'    
            
            # if step forward meet the cat, robot turn right
            elif obstruction_space[update_row][update_column] == "c":

                #the row and column positions of the cat if jump forward in the direction the robot compass facing. 
                update_cat_row = update_row + step_forward[vacuum[2]][0]
                update_cat_column = update_column + step_forward[vacuum[2]][1]

                #check cat new location whether it meet the wall or out of boundary or meet another robot, if not cat jump
                if not check_wall(update_cat_row, update_cat_column) and within_boundary(update_cat_row, update_cat_column) and not check_robot(update_cat_row, update_cat_column):
        
                    #update the new location of the cat
                    obstruction_space[update_row][update_column] = None
                    obstruction_space[update_cat_row][update_cat_column] = "c"
                
                # if step forward meet the cat, robot turn right
                turn_right(vacuum,compass)
                action = 'turn-right'

            #if one step forward NOT leave bound, update location of vacuum
            else:
                
                current_location = cleaning_space[vacuum[0]][vacuum[1]]

                match current_location:
                        
                    #if current location is dirty, smear the dirt into the location it ends in after the action
                    case "d":
                        
                        #if location after the action is clean, smear the dirt 
                        if cleaning_space[update_row][update_column] == None:
                            cleaning_space[update_row][update_column] = "d"

                        #if location after the action is water, smear the mud 
                        elif cleaning_space[update_row][update_column] == "l":
                            cleaning_space[update_row][update_column] = "m"

                        #if location after the action is soap, the location is clean 
                        elif cleaning_space[update_row][update_column] == "s":
                            cleaning_space[update_row][update_column] = None              

                    #if current location is mud, smear the mud into the location it ends in after the action
                    case "m":
                        cleaning_space[update_row][update_column] = "m"

                    #if current location is water, the vacuum slip
                    case "l":

                        slip_row = update_row + step_forward[vacuum[2]][0]
                        slip_column = update_column + step_forward[vacuum[2]][1]

                        #the new location will meet the wall or out of boundary, turn right instead
                        if not within_boundary(slip_row, slip_column) or check_wall(slip_row, slip_column):
                            
                            turn_right(vacuum,compass)
                            action = 'turn-right'
                            
                            #the robot turn right, the next location the the same location as now
                            update_row = vacuum[0]
                            update_column = vacuum[1]
                        
                        #the new location will meet another robot, turn left instead
                        elif check_robot(slip_row, slip_column):
                            
                            turn_left(vacuum,compass)
                            action = 'turn-left'
                            
                            #the robot turn left, the next location the the same location as now
                            update_row = vacuum[0]
                            update_column = vacuum[1]

                        #if the location slip into is not meet the wall and NOT LEAVE boundary
                        else:        

                            #if skip over location is dirt, smear the mud into the location it slip pass
                            if cleaning_space[update_row][update_column] == "d":
                                cleaning_space[update_row][update_column] = "m"    
                            
                            #if skip over location is clean, smear the water into the location it slip pass
                            elif cleaning_space[update_row][update_column] == None:
                                cleaning_space[update_row][update_column] = "l"
                            
                            #if skip over location is soap, set the location it slip pass to clean
                            elif cleaning_space[update_row][update_column] == "s":
                                cleaning_space[update_row][update_column] = None     
                            
                            #the robot slip, the next location is 2 step forward
                            update_row = slip_row
                            update_column = slip_column
                    
                    #if current location is soap, the location it skip over is set to clean
                    case "s":
                        
                        slip_row = update_row + step_forward[vacuum[2]][0]
                        slip_column = update_column + step_forward[vacuum[2]][1]

                        #the new location will meet the wall or out of boundary, turn right instead
                        if not within_boundary(slip_row, slip_column) or check_wall(slip_row, slip_column):
                            
                            turn_right(vacuum,compass)
                            action = 'turn-right'
                            
                            #the robot turn right, the next location the the same location as now
                            update_row = vacuum[0]
                            update_column = vacuum[1]

                        #the new location will meet another robot, turn left instead
                        elif check_robot(slip_row, slip_column):
                            
                            turn_left(vacuum,compass)
                            action = 'turn-left'
                            
                            #the robot turn left, the next location the the same location as now
                            update_row = vacuum[0]
                            update_column = vacuum[1]

                        #if the location slip into is NOT meet the wall and NOT LEAVE boundary
                        else:        
                            
                            #set the location it slip pass to clean
                            cleaning_space[update_row][update_column] = None     
                            
                            #the robot slip, the next location is 2 step forward
                            update_row = slip_row
                            update_column = slip_column
                    
                #update location of vacuum in obstruction space
                obstruction_space[vacuum[0]][vacuum[1]] = None
                obstruction_space[update_row][update_column] = "r" 
                
                #update the vacuum's position to new expected location  
                vacuum[0] = update_row
                vacuum[1] = update_column

    return action

def perform_cleaning(instructions:str, vacuums:list, logs:str)-> None:
    """
    This function will get instruction file, read file and let robot perform instruction according to file.
    Parameter
        instructions : str : instruction file contain instructions specifying what the vacuum should do    
        vacuums : list[int|int|str]: containing the vacuum's position and direction its facing
        logs : str : log file use for write the actions robot actually perform after receive instruction
    """
    #open instructions file to read
    with open(instructions, 'r') as instruction_file:
        #open logs files to write
        for log in logs:
          open(log, "w")

        #split vacuum id and list of instruction of each line 
        for line in instruction_file:
            if line[0].isnumeric():
                vacuum_id = int(line[0])
                instuction = line.strip().split(",")
                instuction[0] = instuction[0][2:]

            #open logs files of specified vacuum_id to append
            with open(logs[vacuum_id], "a") as logfile:
                
                #perform each command from list of instruction of each line 
                #then append actions robot actually perform after receive instruction in logfile 
                for command in instuction:
                    action_perform = vacuum_action(vacuums[vacuum_id],command)

                    logfile.write(action_perform + "\n")



if __name__ == "__main__":
    test_commands = "test_commands.txt"
    test_logs = ["test_log1.txt","test_log2.txt"]
    vacuums = [
            [2,2,"N"],
            [4,4,"NE"],
        ]

    print("INITIAL SPACE")
    for row_index,row in enumerate(cleaning_space):
        for col_index,cell in enumerate(row):
            if obstruction_space[row_index][col_index] is not None:
                print(obstruction_space[row_index][col_index],end='')
            elif cell is None:
                print(".",end='')
            else:
                print(cell,end='')
        print()

    print("CLEANING")
    perform_cleaning(test_commands,vacuums,test_logs)

    print("FINAL SPACE")
    for row_index,row in enumerate(cleaning_space):
        for col_index,cell in enumerate(row):
            if obstruction_space[row_index][col_index] is not None:
                print(obstruction_space[row_index][col_index],end='')
            elif cell is None:
                print(".",end='')
            else:
                print(cell,end='')
        print()

    print("ACTIONS")
    for log_file in test_logs:
        with open(log_file,"r") as log:
            print(f"FROM: {log_file}")
            print(log.read())