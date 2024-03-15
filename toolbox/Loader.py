from langchain.prompts import PromptTemplate
from pathlib import Path
import os
from langchain.document_loaders import PyPDFLoader
from docx import Document
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
INPUT_FOLDER = config.get('folder', 'input_folder')

def load_prompt(filename):
        path = Path('./prompts') / Path(filename)
        with open(path, 'r', encoding='utf-8') as f:
            p = f.read()
        if filename ==  "keyword_prompt_paper.txt":
            return PromptTemplate(
                        input_variables=["keywords_N", "human_input"],
                        template=p
                        )
        elif filename == "ch_prompt.txt":
            return PromptTemplate(
                        input_variables=["content"],
                        template=p
                        )
        elif filename == "reader_prompt.txt":
            return PromptTemplate(
                        input_variables=["content"],
                        template=p
                        )
        elif filename == "grammar_prompt.txt":
            return PromptTemplate(
                        input_variables=["content"],
                        template=p
                        )
        elif filename == "solver_prompt.txt":
            return PromptTemplate(
                        input_variables=["language", "discription"],
                        template=p
                        )
        elif filename == "translate_prompt.txt":
            return PromptTemplate(
                        input_variables=["domain", "language", "content"],
                        template=p
                        )
        elif filename == "coding_prompt.txt":
            return PromptTemplate(
                        input_variables=["language", "requirement"],
                        template=p
                        )
        elif filename == "coding_exchange_prompt.txt":
            return PromptTemplate(
                        input_variables=["language", "requirement"],
                        template=p
                        )
        elif filename == "abstract_prompt.txt":
            return PromptTemplate(
                        input_variables=["language", "word", "content"],
                        template=p
                        )
        elif filename == "introduction_prompt.txt":
            return PromptTemplate(
                        input_variables=["word", "reference", "reference list"],
                        template=p
                        )
        elif filename == "reference_prompt.txt":
            return PromptTemplate(
                        input_variables=["order", "reference", "type"],
                        template=p
                        )
        elif filename == "trendword_prompt.txt":
            return PromptTemplate(
                        input_variables=["content"],
                        template=p
                        )
        else:
            raise  TypeError("Prompt file 不合法")

def load_pdf() -> list:
    inputList = os.listdir(INPUT_FOLDER)
    textList = []
    for file in inputList:
        if file.find('.pdf') != -1:
            all_text = ""
            path = INPUT_FOLDER + "/" + file
            loader = PyPDFLoader(path)
            texts = loader.load()  
            for text in texts:
                all_text = all_text + text.page_content
            textList.append(all_text)
        else:
            continue
    return textList

def load_word() -> list:
    inputList = os.listdir(INPUT_FOLDER)
    textList = []
    for file in inputList:
        if file.find('.docx') != -1:
            all_text = ""
            doc = Document(INPUT_FOLDER + '/' + file)
            for para in doc.paragraphs:
                if para.style.name.startswith('Heading'):
                    continue       
                all_text = all_text  +  para.text + '\n'
            textList.append(all_text)
        else:
            continue
    return textList

def current_time():
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H-%M-%S")
    return currentTime