import os
import argparse
import subprocess
from langchain.llms import HuggingFaceTextGenInference
from IPython.display import display, Markdown
from langchain import PromptTemplate
from langchain.chains import LLMChain
from colorama import init, deinit, Cursor, Fore, Back

init(autoreset=True)
def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')


inference_server_url = os.getenv("INFERENCE_SERVER_URL", "your_production_LLM")
llm = HuggingFaceTextGenInference(
    inference_server_url=inference_server_url,
    max_new_tokens=512,
    top_k=10,
    top_p=0.95,
    typical_p=0.95,
    temperature=0.01,
    repetition_penalty=1.03,
)

try :
    while True: 
        clear_terminal()
        print(Cursor.POS(0, 0), end='')
        print(Fore.GREEN + "**********************************************************************")
        print(Fore.GREEN + f"""  /$$$$$$                        /$$               /$$                
 /$$__  $$                      | $$              |__/                
| $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$  /$$ /$$$$$$$       
| $$       |____  $$ /$$__  $$|_  $$_/   |____  $$| $$| $$__  $$      
| $$        /$$$$$$$| $$  \ $$  | $$      /$$$$$$$| $$| $$  \ $$      
| $$    $$ /$$__  $$| $$  | $$  | $$ /$$ /$$__  $$| $$| $$  | $$      
|  $$$$$$/|  $$$$$$$| $$$$$$$/  |  $$$$/|  $$$$$$$| $$| $$  | $$      
 \______/  \_______/| $$____/    \___/   \_______/|__/|__/  |__/      
                    | $$                                              
                    | $$                                              
                    |__/                                              
 /$$$$$$$                      /$$                                    
| $$__  $$                    | $$                                    
| $$  \ $$  /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$           
| $$  | $$ /$$__  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$          
| $$  | $$| $$  \ $$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/          
| $$  | $$| $$  | $$| $$      | $$_  $$ | $$_____/| $$                
| $$$$$$$/|  $$$$$$/|  $$$$$$$| $$ \  $$|  $$$$$$$| $$                
|_______/  \______/  \_______/|__/  \__/ \_______/|__/                
                                                                                                         
""")
        print(Fore.GREEN + "**********************************************************************")
        user_input = input(Fore.GREEN + "Enter a command to translate to Docker, or type 'exit' to quit: ")

        request = f"""System:Below is an instruction that describes a task, paired with an input that provides further context. Write an output that appropriately completes the request.
        Instruction: translate this sentence in docker command
        Input:{user_input}
        Output:"""
        

        try:
            response = llm(request)
        except Exception as e:
            print(f"An error occurred: {e}")

        if user_input.lower() == 'exit':
            break
        
        cmd = response[1:]
        if cmd.startswith('"') and cmd.endswith('"'):
            cmd = cmd[1:-1]
        print(Fore.GREEN + f"Translated Docker command: {cmd}")
        
        subprocess.run(cmd, shell=True)
        print(Fore.GREEN + "***********************************************") 
        continue_choice = input(Fore.GREEN + "Would you like to continue? (yes/no): ").lower()
        if continue_choice not in ['yes', 'y']:
            break
finally:
     deinit()
