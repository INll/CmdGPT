import os
import sys
import myconstants
import json
import shutil
from typing import Union, Callable
from seleniumbase import BaseCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from pytest import main

poe_url = 'https://poe.com/ChatGPT'

# Commandline methods 
class Wrapper:
    def __init__(self, constants: list[Union[dict[str, int], dict[str, str], list[int]]], url: str) -> None:
        self.constants, self.url = constants, url
        self.headful, self.debug = '--headful' in sys.argv, '--debug' in sys.argv
        self.paths, self.final_input, self.is_first_query = {}, '', True
        self.final_output = ''

    def get_prompt(self) -> None:
        prompts = os.listdir(self.constants.DIR)
        for index, fileName in enumerate(prompts):
            prompt_name = fileName.split('.', 1)[0]
            print(f'{index:03d} -- {prompt_name}')
            self.paths[f'{index:03d}'] = prompt_name
        while True:
            try:
                code = input('\nEnter a 3-digit prompt code. (optional)\n')
                if code == '':
                    self.final_input = code
                    break
                if not len(code) == 3 or code not in self.paths:
                    continue
                else:
                    print(f'\n\n\nPrompt selected: {self.paths[code]}\n\n')
                    with open(f'{self.constants.DIR}\{self.paths[code]}.txt') as f:
                        self.final_input = f.read() + '\n'
                    break
            except EOFError:
                pass
    
    def build_input(self, teardown: Callable, clear_context: Callable) -> None:
        if self.is_first_query:
            os.system('cls')
            print("Select your starting prompt:\n")
            self.get_prompt()
        else:
            self.final_input = ''
        print('Type or paste input, then Ctrl + Z on a new line to submit. /exit + Enter to quit, /clear + Enter to restart conversation.\n')
        input_str, text = '', ''
        while True:
            try:
                input_str = input()
                if input_str == '/exit':
                    teardown()
                    sys.exit(1)
                elif input_str == '/clear':
                    clear_context(True)
                    print('\nContinue input.\n')
                    continue
                text += input_str + '\n'
            except EOFError:
                break
        self.final_input += text.replace('\t', '    ')
        
    def edit_preferences(path: str, mode: str) -> None:
        with open(file=path, mode=mode) as file:
            for line in file:
                new_config = line.replace('Crashed', 'none')  # No "Restore Page" popup
            file.seek(0)  # set pointer to start of file before truncating
            file.truncate()
            file.write(new_config)

class Poe(BaseCase):
    def test_poe(self) -> None:
        try:
            self.wrapper = Wrapper(myconstants, poe_url)

            while True:
                self.wrapper.build_input(self.tearDown, self.clear_context)
                # reject illegal strings
                if self.wrapper.final_input == '' or self.wrapper.final_input.isspace():
                    self.wrapper.is_first_query = False
                    print('Empty input!\n')
                    continue
                
                # connect to site
                if self.wrapper.is_first_query:
                    print('\nConnecting...')
                    self.open(self.wrapper.url)
                    print('Done.\n')
                
                # execute functions
                modules = self.clear_context, self.input_text, self.handle_response
                for i, module in enumerate(modules):
                    attempts = 0
                    while True:     # retry module
                        try:
                            module(attempts)
                            break
                        except Exception:
                            print(f'Exception thrown while executing {module.__name__}.\n')
                            if attempts == self.wrapper.constants.ATTEMPTS[i]:
                                print("Maximum retries reached. Exiting program.")
                                self.tearDown()
                                sys.exit()
                            print(f'Retrying...({attempts+1}/{self.wrapper.constants.ATTEMPTS[i]+1})\n')
                            attempts+=1
                            pass
        except KeyboardInterrupt:
            self.tearDown()
            sys.exit(1)
                    
    # click clear context button
    def clear_context(self, is_forced_clear = False) -> None:
        if self.wrapper.is_first_query or is_forced_clear == True:
            self.click(self.wrapper.constants.SELECTORS['clearContextBtn'])
            self.wrapper.is_first_query = False
            print('Context cleared.\n')
    
    # inject input then submit    
    def input_text(self, attempts: int) -> None:
        print('\nSubmitting prompt... ')
        segments = self.wrapper.final_input.split('\n')
        for segment in segments:
            action = ActionChains(self.driver)
            script = """document.querySelector('%s').value+=%s;""" % (
                self.wrapper.constants.SELECTORS['inputTextarea'],
                json.dumps(segment),
            )
            self.execute_script(script)
            action.key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).perform()
            action.reset_actions()
        self.add_text(self.wrapper.constants.SELECTORS['inputTextarea'], '\n')
        print('Success.\n')
            
    # wait then handle generated paragraphs
    def handle_response(self, attempts: int) -> None:
        print('Waiting for response... ')
        if self.assert_elements_present(self.wrapper.constants.SELECTORS['allResponseParagraphs'], timeout=15):
            print('Success\n\nParsing response...\n\n\nvvvvvvvvvvv\n\n')
            
            # implement a stack to print received paragraphs one by one
            response_timeout = self.wrapper.constants.TIMEOUTS['RESPONSE']
            stack = []
            while response_timeout:
                try:
                    self.assert_element_present(self.wrapper.constants.SELECTORS['feedbackBtnsPrefix'], timeout=0.1)
                    break
                except:  # find_visible_elements is less accurate
                    stack = self.print_and_track_response(self.wrapper.constants.SELECTORS['allResponseParagraphs'], stack)
                    response_timeout -= 1
                    pass
            # print the final paragraph once all paragraphs have been generated
            if attempts == 0:
                last_paragraph = self.parse_response_to_string(self.find_element(self.wrapper.constants.SELECTORS['lastResponseParagraph']))
                print(f'{last_paragraph}\n\n^^^^^^^^^^^\n\n')
            elif attempts > 0:
                stack = self.print_and_track_response(self.wrapper.constants.SELECTORS['allResponseParagraphs'], stack)
                print('\n\n^^^^^^^^^^^\n\n')

    # implement a stack to record and print received paragraphs
    def print_and_track_response(self, selector: str, stack: list[str]) -> list[str]:
        paragraphs = self.find_elements(selector)
        while len(stack) < len(paragraphs) - 1:
            print(self.parse_response_to_string(paragraphs[len(stack)]))
            stack.append(paragraphs[len(stack)])
        return stack

    # Handle Poe formatting and return parsed string
    def parse_response_to_string(self, element: WebElement) -> str:
        response = element.get_attribute('innerText')
        if element.tag_name == 'div':
            response = response.split('Copy', 1)[1]
        return response + '\n'

        
if __name__ == "__main__":
    # Configure preferences before driver initialization
    file_path = f'{myconstants.USER_DIR}/{myconstants.PROFILE}/Preferences'
    backup_path = f'{myconstants.USER_DIR}/{myconstants.PROFILE}/Preferences_backup'
    
    if(os.path.exists(file_path)):
        shutil.copyfile(file_path, backup_path)  # Backup
    else:
        shutil.copyfile(backup_path. file_path)  # Restore
    Wrapper.edit_preferences(file_path, 'r+')
    os.system('cls')
    print('Initializing...')

    main([__file__, f"--user-data-dir={myconstants.USER_DIR}", "-s", "--rs", "--uc",
        "--tb=no", "-p no:warnings", "--no-header", "--no-summary", "-q", "--quiet", "--show-capture=no", "--disable-warnings", 
        "--headless"
        ])