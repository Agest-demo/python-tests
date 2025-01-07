import os
import yaml

class Hello():
    # __init__ is a definition runs itself. 
    def __init__(self): 
        print('Hello there')
        # Call another definition. 
        self.andBye()

    # This definition should be calles in order to be executed. 
    def andBye(self):
        print(os.getenv('MY_PARAM'))
        with open("env.yml") as stream:
            try:
                envs = (yaml.safe_load(stream))
                print(envs['env']['TOKEN'])
                print(envs['env']['TOKEN_2'])
            except yaml.YAMLError as exc:
                print(exc)

# Run class
def test_add_parameterized():
    hello = Hello()