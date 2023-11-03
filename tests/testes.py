import subprocess, time
from random import randint

'''
Quais inputs necessários?

1os: nomes dos jogadores

2os: primeira ação

    1 - invest

        quantity_to_invest = input("How much to invest?")
        investment_time = input("How many turns money should be invested?")

    2 - Hire

        quantity_to_hire = input("how many soldiers to hire?")

    3 - Attack

        target_player = input("Who do you attack?")

        force_employed = input("\n\nHow many soldiers will be deployed?")

    4 - Pass

    
    ------------------ INICIO ESTRUTURA QUERY -----------------
    

                # Waits for main.py request input
                time.sleep(1)

                # Answer the 1st input
                input1 = "Esse é o input1"
                debug_process.stdin.write(input1)
                debug_process.stdin.flush()

                # Close the stdin of main.py and wait for output
                debug_process.stdin.close()
                debug_process.wait()

                # Get output of main.py
                debug_output = debug_process.stdout.read()

                
    ------------------- FIM ESTRUTURA QUERY --------------------

    
'''

# 1 - Create inputs

names_pool = ["carlos", "maria", "joao", "daria", "jose", "jordana", "julia", "marcia", "paulo", "daniel", "gaia"]


# 2 - Execute the code being tested, capturing the output


# 3 - Compare the output


# Path to main.py
FILEPATH = "./war/main.py"


# Init main.py
debug_process = subprocess.Popen(["python3", FILEPATH], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

# Waits for main.py request input
time.sleep(1)

# <-----> 1 - players name <----->
# <-----> 1.1 - Player 1 <----->
try:

    # Answer the 1st input
    player1 = names_pool[randint(0,len(names_pool))]
    debug_process.stdin.write(player1)
    debug_process.stdin.flush()

    # Close the stdin of main.py and 
    debug_process.stdin.close()

    # Wait for output (in this case, none)
    #debug_process.wait()

    # Get output of main.py
    #debug_output = debug_process.stdout.read()

except Exception:
    pass

# <-----> 1.2 - Player 2 <----->
try:

    # Answer the 1st input
    player2 = names_pool[randint(0,len(names_pool))]
    debug_process.stdin.write(player2)
    debug_process.stdin.flush()

    # Close the stdin of main.py and 
    debug_process.stdin.close()

    # Wait for output (in this case, none)
    #debug_process.wait()

    # Get output of main.py
    #debug_output = debug_process.stdout.read()

except Exception as error:

    print(error)
    pass



# <-----> 2 - Menu's choice <----->
# It doesn't need to write tests for both players, only one. The other just need to pass (4)


# <-----> Player's 1 choice: Invest <----->
# <-----> 2.1 - Invest choice <----->
try:

    # Answer the 2.1 input
    menu_choice1 = 1
    debug_process.stdin.write(menu_choice1)
    debug_process.stdin.flush()

    # <-----> 2.1 - Investment money <----->
    # After flushing, main.py will expect input for quantity_to_invest and than investment_time

    try:

        # Answer the 1st input
        quantity_to_invest = randint(0,101)
        debug_process.stdin.write(quantity_to_invest)
        debug_process.stdin.flush()

        # <-----> 2.1.1 - Investment time <----->
        # After flushing, main.py will expect input for investment_time

        try:

            # Answer the 2st input
            investment_time = randint(1,5)
            debug_process.stdin.write(investment_time)
            debug_process.stdin.flush()

            # Close the stdin of main.py and 
            debug_process.stdin.close()

            # Wait for output (in this case, none)
            #debug_process.wait()

            # Get output of main.py
            #debug_output = debug_process.stdout.read()

        except Exception:
            pass

        # Close the stdin of main.py and 
        debug_process.stdin.close()

        # Wait for output (in this case, none)
        #debug_process.wait()

        # Get output of main.py
        #debug_output = debug_process.stdout.read()

    except Exception:
        pass


    # Close the stdin of main.py and 
    debug_process.stdin.close()

    # Wait for output (in this case, none)
    #debug_process.wait()

    # Get output of main.py
    #debug_output = debug_process.stdout.read()

except Exception:
    pass

# <-----> Player's 2 choice: Pass <----->
try:

    # Answer the 2st input
    menu_choice2 = 4
    debug_process.stdin.write(menu_choice2)
    debug_process.stdin.flush()

    # Close the stdin of main.py and 
    debug_process.stdin.close()

    # Wait for output (in this case, none)
    #debug_process.wait()

    # Get output of main.py
    #debug_output = debug_process.stdout.read()

except Exception:
    pass


'''
ESTRUTURA - COPIAR E COLAR




# <-----> [ITEM CHOICE] <----->
# It doesn't need to write tests for both players, only one. The other just need to pass (4)

# <-----> [INPUT DESCRIPTION] <----->
try:

    # Answer the 2.1 input
    [VAR] = 1
    debug_process.stdin.write([VAR])
    debug_process.stdin.flush()

    # <-----> 2.1 - Investment money <----->
    # After flushing, main.py will expect input for quantity_to_invest and than investment_time

    # SUBSEQUENCE INPUT's COME BELOW:


    # SUBSEQUENCE INPUTS GOES ABOVE

    # Close the stdin of main.py and 
    debug_process.stdin.close()

    # Wait for output (in this case, none)
    #debug_process.wait()

    # Get output of main.py
    #debug_output = debug_process.stdout.read()

except Exception:
    pass

# <-----> Player 2 <----->
try:

    # Answer the 2st input
    menu_choice2 = 4
    debug_process.stdin.write(menu_choice2)
    debug_process.stdin.flush()

    # Close the stdin of main.py and 
    debug_process.stdin.close()

    # Wait for output (in this case, none)
    #debug_process.wait()

    # Get output of main.py
    #debug_output = debug_process.stdout.read()

except Exception:
    pass




'''