def getAction(state):
    Curr_State=state

    #We make use of Conditional Statement To Get the Next Action Given current State.
    if Curr_State[0]=='R' and Curr_State[1][1]==1:
        return "SUCK"
    elif Curr_State[0]=='L' and Curr_State[1][0]==1:
         return "SUCK"
    elif Curr_State[0]=='R' and Curr_State[1][1]==0:
         return "MOVELEFT"
    elif Curr_State[0]=='L' and Curr_State[1][0]==0:
         return "MOVERIGHT"
    else:
       return None


def updateState(state, action):
    Curr_State=state

    #Here, given Current State and Action we Update the State for Next Action.
    if Curr_State[0]=='R' and action=="SUCK":
        Curr_State[1][1]=0
    elif Curr_State[0]=='L' and action=="SUCK":
        Curr_State[1][0]=0
    elif Curr_State[0]=='R' and action=="MOVELEFT":
        Curr_State[0]='L'
    elif Curr_State[0]=='L' and action=="MOVERIGHT":
        Curr_State[0]='R'

    return Curr_State


def bool_all_rooms_clean(state):

    #If all room are clean then we Return True or else False.
    if state[1][0]==0 and state[1][1]==0:
        return True
    else:
        return False


def run_vacuum(start_state):
    state = start_state
    loop_count = 0  # counter to stop program when it goes wrong

    # run the simulation until all rooms clean
    while not bool_all_rooms_clean(state):
        action = getAction(state)
        state = updateState(state, action)

        # show state and stop if too many loops
        print(f"cycle:{loop_count}\taction={action}\t\tstate={state}")
        loop_count += 1

        if loop_count > 20:
            print(
                "Uh oh ! Code stuck in a state ... program terminated")
            return

    print("All rooms clean!")
    return


def main():
    # when you run this code without implementing above functions
    # the program will stop after 20 cycles
    # Part 1: Start in room R
    start_state = ['R', [1, 1]]
    print(f"\nPart1. Start in room R\nStart State: {start_state}")
    run_vacuum(start_state)

    # Part 2: Start in room L
    start_state = ['L', [1, 1]]
    print(f"\nPart2. Start in room L\nStart State: {start_state}")
    run_vacuum(start_state)


if __name__ == '__main__':
    main()
