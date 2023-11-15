import unittest, functions, settings
from unittest.mock import patch
from random import randint

#FILEPATH = "../main.py"

# Test if names is turned into Players object and added to main. players_list
class Unittest_receive_guests(unittest.TestCase):
    
    names_pool = ["carlos", "maria", "joao", "daria", "jose", "jordana", "julia", "marcia", "paulo", "daniel", "gaia"]
    num_players = randint(2,5)

    # Sequence of inputs required in function
    global test_input_seq
    test_input_seq = []

    test_input_seq.append(str(num_players))


    # Popula uma lista com N nomes, (N-1) sim e 1 não
    lista = range(num_players)  # Range(2) = [0,1]
        
        #Verificar duas condições: x é o ultimo ou não?
        
    for x in lista:

        # Se o index do elemento x em lista for diferente do comprimento -1
        if lista.index(x) != (len(lista)-1):
            # Choose an random numbert between 0 and 'names_pool' length 
            test_input_seq.append(names_pool[randint(0, len(names_pool) - 1)])
            
        else: 
            test_input_seq.append(names_pool[randint(0, (len(names_pool) - 1))])


    @patch('builtins.input', side_effect=test_input_seq) # Side_effect são os inputs a serem passados. Deve receber uma lista

    def test_receive_guests(self, mock_input):
        

        print("TESTE: test_input_seq")
        print(test_input_seq)

        result = functions.receive_guests()
        test_players_names = []
        mock_side_effects = mock_input.call_args_list

        print("-------------------------------")
        print(x for x in mock_side_effects)
        print("-------------------------------")

        # Isso aqui não está funcionando
        for x,y in enumerate(mock_input):
            
            print("TESTE: x,y do enumerate(mockinput)")
            print(x,y)

            if x%2 != 0:
                
                test_players_names.append(y) # Não está populando


        print("TESTE: test_players_names depois") # Aqui deve estar populado
        print(test_players_names)

        settings_players_list_names = [x.name for x in settings.players_list]

        # Checar se os nomes escolhidos foram instanciados em objetos
        self.assertEqual(test_players_names, settings_players_list_names)

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