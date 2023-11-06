import unittest, functions, main
from unittest.mock import patch
from random import randint

#FILEPATH = "../main.py"

# Test if names is turned into Players object and added to main. players_list
class Unittest_receive_guests(unittest.TestCase):
    
    names_pool = ["carlos", "maria", "joao", "daria", "jose", "jordana", "julia", "marcia", "paulo", "daniel", "gaia"]
    num_players = randint(2,5)
    # Sequence of inputs required in function
    test_input_seq = []

    test_input_seq.append(str(num_players))


    # Popula uma lista com N nomes, (N-1) sim e (N - [N-1]) sim
    for x in range(num_players):
        if x != (num_players - 1):
            # Choose an random numbert between 0 and 'names_pool' length 
            test_input_seq.append(names_pool[randint(0, len(names_pool) - 1)])
            test_input_seq.append('y')
            

        test_input_seq.append(names_pool[randint(0, (len(names_pool) - 1))])
        test_input_seq.append('n')


    @patch('builtins.input', side_effect=test_input_seq) # Side_effect são os inputs a serem passados. Deve receber uma lista

    def test_receive_guests(self, mock_input):
        
        result = functions.receive_guests()

        test_players_names = [x for x in mock_input if x%2 != 0]
        main_players_list_names = [x.name for x in main.players_list]

        # Checar se os nomes escolhidos foram instanciados em objetos
        self.assertEqual(test_players_names, main_players_list_names)

        # Checar se a função retorna o esperado
        self.assertEqual(result, "200 OK")


# class Unittest_create_party(unittest.TestCase):
#     def test_create_party():
#         pass

    # def test_menu_action():
    #     pass

    # def test_get_action():
    #     pass

    # def test_invest():
    #     pass

    # def test_hire():
    #     pass

    # def test_attack():
    #     pass

    # def test_queue_cleaner():
    #     pass

    # def test_get_time():
    #     pass

    # def test_generate_log():
    #     pass

if __name__ == '__main__':
    unittest.main()