import unittest, random
from unittest.mock import patch
import utils.functions as functions, utils.models as models, settings

class TestReceiveGuests(unittest.TestCase):

    # Lista de 10 nomes para o teste
    test_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Harry', 'Ivy', 'Jack']

    def test_receive_guests_successful(self):
        # Sortear um número entre 1 e 4
        num_names_to_choose = random.randint(1, 4)

        # Sortear essa quantidade de nomes da lista
        selected_names = [num_names_to_choose] + random.sample(self.test_names, num_names_to_choose)

        with patch('builtins.input', side_effect=map(str, selected_names)):
            result = functions.receive_guests()

            # Verificar se a função retorna "200 OK"
            self.assertEqual(result, "200 OK")

            # Verificar se cada nome passado se torna um objeto Player em settings.players_list
            for name in selected_names[1:]:
                player_instance = next((p for p in settings.players_list if p.name == name), None)
                self.assertIsNotNone(player_instance)
                self.assertIsInstance(player_instance, models.Player)
                

class TestCreateParty(unittest.TestCase):

    def test_create_party_successful(self):
        # Criar uma lista de objetos Player para o teste
        players_list = [models.Player('Alice'), models.Player('Bob'), models.Player('Charlie')]

        # Substituir a função append de settings.current_party para verificar se é chamada corretamente
        with patch('settings.current_party.append') as mock_party:
            result = functions.create_party(players_list)

            # Verificar se a função retorna "200 OK"
            self.assertEqual(result, "200 OK")

            # Verificar se um objeto Party foi instanciado corretamente
            mock_party.assert_called_once_with(players_list)
            mock_party_instance = mock_party.return_value
            self.assertEqual(settings.current_party[0], mock_party_instance)
            

class TestMenuAction(unittest.TestCase):

    def test_menu_action_successful(self):
        # Criar um objeto Player para o teste
        test_player = models.Player('Alice')

        # Substituir a função input para fornecer uma escolha específica
        with patch('builtins.input', return_value='1'):
            result = functions.menu_action(test_player)

            # Verificar se a função retorna "200 1"
            self.assertTrue(result.startswith("200 "))
            self.assertEqual(int(result.split()[1]), 1)

        # Substituir a função input para fornecer um input não válido
        with patch('builtins.input', return_value='invalid_input'):
            result = functions.menu_action(test_player)

            # Verificar se a função retorna "400 ERROR"
            self.assertEqual(result, "400 ERROR")
            

class TestGetAction(unittest.TestCase):

    @patch('builtins.input', side_effect=["10", "3"])
    def test_invest_action(self, mock_input):
        player = models.Player(name="TestPlayer", money=100, military=50)
        return_code = "ACTION 1"
        result = functions.get_action(player, return_code)
        self.assertEqual(result, "200 OK")

    @patch('builtins.input', side_effect=["5"])
    def test_hire_action(self, mock_input):
        player = models.Player(name="TestPlayer", money=100, military=50)
        return_code = "ACTION 2"
        result = functions.get_action(player, return_code)
        self.assertEqual(result, "200 OK")

    @patch('builtins.input', side_effect=["3", "Player2", "10"])
    def test_attack_action(self, mock_input):
        player = models.Player(name="TestPlayer", money=100, military=50)
        player2 = models.Player(name="Player2", money=100, military=50)
        settings = {'players_list': [player, player2], 'current_party': [{'round': 1}]}
        return_code = "ACTION 3"
        with patch.dict('your_module.settings', settings):  # Substitua 'your_module' pelo nome do seu módulo
            result = functions.get_action(player, return_code)
        self.assertEqual(result, "200,OK")

    def test_invalid_action(self):
        player = models.Player(name="TestPlayer", money=100, military=50)
        return_code = "ACTION 5"
        result = functions.get_action(player, return_code)
        self.assertEqual(result, "400 ERROR")


if __name__ == '__main__':
    unittest.main()