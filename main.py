from functions import create_party, menu_action
import db

players_list = []
action_queue = []


def main():
    
    print('-----> Welcome to War Games <-----')

    # Get players

    global current_party 
    
    # Initiate the party
    current_party = create_party(players_list)

    while current_party.status is True:
        # Get action for every player
        for turn_player in db.players:
            menu_action(turn_player)

        
        # Read and execute action queue
        for action in action_queue:
            if action.type == "invest":
                if (action.expire) != (current_party.round): # Time to execute action
                    continue
                else:
                    investment_return = ((action.quantity)/100 ** (action.ttl)) + (action.quantity)/10
                    action.executor.money += investment_return
                    
                    print(f'{action.executor} just received ${investment_return} back!')
                    continue
                    
            elif action.type == "hire":
                pass
            elif action.type == "attack":
                pass
            else:
                pass
        
        current_party.round += 1

if __name__ == '__main__':
    main()