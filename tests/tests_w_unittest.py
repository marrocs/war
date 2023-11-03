import unittest, time, subprocess


FILEPATH = "../main.py"
debug_process = subprocess.Popen(["python3", FILEPATH], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)


class Unit_test_functions(unittest.TestCase):
    
    def test_receive_guests(self):
        
        # Test if names is turned into Players object and added to main. players_list

        names_pool = ["carlos", "maria", "joao", "daria", "jose", "jordana", "julia", "marcia", "paulo", "daniel", "gaia"]

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

    def test_create_party():
        pass

    def test_menu_action():
        pass

    def test_get_action():
        pass

    def test_invest():
        pass

    def test_hire():
        pass

    def test_attack():
        pass

    def test_queue_cleaner():
        pass

    def test_get_time():
        pass

    def test_generate_log():
        pass

if __name__ == '__main__':
    unittest.main()