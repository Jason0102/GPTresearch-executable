from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from docx import Document
import configparser
from toolbox.Loader import *

config = configparser.ConfigParser()
config.read('config.ini')
GPT_MODEL = config.get('openai', 'model')
OUTPUT_FOLDER = config.get('folder', 'output_folder')

class GrammarTool():
    def __init__(self, key: list, grammar_prompt) -> None:
        self.grammar_agent = LLMChain(
            llm=ChatOpenAI(temperature=0, model_name=GPT_MODEL, openai_api_key=key[0]),
            prompt=grammar_prompt,
            verbose=False
        )

    def run(self, text: str):
        result = self.grammar_agent.run({"content": text})
        return result

def grammar_check():
    agent = GrammarTool(
        key = [config.get('openai', 'key1')],
        grammar_prompt=load_prompt("grammar_prompt.txt")
    )
    texts = []
    texts.append(load_word())
    if len(texts) == 0:
        return -1
    inputList = os.listdir(INPUT_FOLDER)
    nameroot = inputList[0][:-4]
    doc = Document(INPUT_FOLDER + '/' + inputList[0])
    print("Grammar and phrase revising............")
    for para in doc.paragraphs:
        if para.style.name.startswith('Heading'):
            continue
        elif para.text == "":
            continue       
        result = agent.run(para.text)
        para.text = result
    doc.save(OUTPUT_FOLDER + '/' + nameroot + "_revised.docx")
    return 0