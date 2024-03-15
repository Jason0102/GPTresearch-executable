from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from docx import Document
import configparser
from toolbox.Loader import *

config = configparser.ConfigParser()
config.read('config.ini')
GPT_MODEL = config.get('openai', 'model')
OUTPUT_FOLDER = config.get('folder', 'output_folder')

class CodingTool():
    def __init__(self, key: list, coding_prompt) -> None:
        self.coding_agent = LLMChain(
            llm=ChatOpenAI(temperature=0, model_name=GPT_MODEL, openai_api_key=key[0]),
            prompt=coding_prompt,
            verbose=False
        )

    def run(self, language:str, text: str):
        result = self.coding_agent.run({"language": language, "requirement": text})
        return result
    
def coding(text, language="Python"):
    agent = CodingTool(
        key = [config.get('openai', 'key1')],
        coding_prompt=load_prompt("coding_prompt.txt"),
    )
    print("Coding............")
    result = agent.run(language, text)
    path = OUTPUT_FOLDER + '/' +  current_time() + '_' + language + '.txt'
    with open(path,'w', encoding='utf-8') as f:
        f.write(result)
    return 0

def code_exchange(to_language="python"):
    agent = CodingTool(
        key = [config.get('openai', 'key1')],
        coding_prompt=load_prompt("coding_exchange_prompt.txt"),
    )
    inputList = os.listdir(INPUT_FOLDER)
    print("Exchanging............")
    i = 0
    for input in inputList:
        path = INPUT_FOLDER + '/' + input
        with open(path,'r', encoding='utf-8') as f:
            text = f.read()
        result = agent.run(to_language, text)
        path = OUTPUT_FOLDER + '/' +  input.split('.')[0] + '_' + to_language + '.txt'
        with open(path,'w', encoding='utf-8') as f:
            f.write(result)
        percentage = 100*(i+1)/len(inputList)
        msg = f"File exchanged complete {percentage}%."
        print(msg)
        i = i+1
    return 0