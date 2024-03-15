from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from docx import Document
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import datetime

import configparser
from scholarly import scholarly
from toolbox.Loader import *

config = configparser.ConfigParser()
config.read('config.ini')
GPT_MODEL = config.get('openai', 'model')
OUTPUT_FOLDER = config.get('folder', 'output_folder')

class ResearhTrendTool():
    def __init__(self, key: list, trendword_prompt) -> None:
        self.trendword_agent = LLMChain(
            llm=ChatOpenAI(temperature=0, model_name=GPT_MODEL, openai_api_key=key[0]),
            prompt=trendword_prompt,
            verbose=False
        )

    def run(self, text: str, interval: int, iteration=100) -> str:
        tonow = datetime.now()
        try:
            texture = ""
            search_query = scholarly.search_pubs(text, year_high=tonow.year, year_low=tonow.year-interval)
            for i in range(iteration):
                info = next(search_query)
                toGPT = info['bib']['title'] + ' ' + info['bib']['abstract']
                keyword = self.trendword_agent.run({"content": toGPT})
                texture = texture + keyword
            return texture
        except StopIteration:
            print(f"stop iteration {i}")
            return texture
        
def research_wrodcloud(topic='Simultaneous localization and mapping', background_color='black', interval=1):
    agent=ResearhTrendTool(
        key=[config.get('openai', 'key1')],
        trendword_prompt=load_prompt("trendword_prompt.txt"),
    )
    print("Generating wordcloud......................")
    result = agent.run(topic, interval)
    wordcloud = WordCloud(width=1024, height=768, max_words=100, min_font_size=12, background_color=background_color).generate(result)
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.imshow(wordcloud)
    # plt.axis("off")  
    filename = OUTPUT_FOLDER + '/' + topic + '.png'
    # plt.savefig(filename)
    wordcloud.to_file(filename)
    return 0
        
if __name__ == "__main__":
    research_wrodcloud()