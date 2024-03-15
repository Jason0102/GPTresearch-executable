import requests
import base64
import configparser

# testing lib
from pathlib import Path
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

class GPTimage():
    def __init__(self, openai_api_key, prompt, model_name, temperature = 0, memory=None, img_memory=None, save_stm=False) -> None:
        self.key = openai_api_key
        self.prompt = prompt
        self.text_stm = memory
        self.img_stm = img_memory
        self.temperature = temperature
        self.save_stm = save_stm
        self.model = model_name
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        

    def run(self, text_dict: dict, img_list:list) -> str:
        send = []
        # load img STM
        if self.img_stm != None:
            if img_list != []:
                self.img_stm.refresh()
            else: 
                for img in self.img_stm.get_img():
                    send.append({
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{img}",
                            "detail": "low"
                        }})
        # load text STM 
        if self.text_stm != None:
            chat_history = self.text_stm.load_memory_variables({})['chat_history']
        else:
            chat_history = None
        for img in img_list:
            send.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{img}",
                    "detail": "low"
            }})

        input_text = text_dict['language']
        send.append({
            "type": "text",
            "text": self.prompt.format(language=text_dict['language'], discription=text_dict['discription'])
        })
        message = []
        message.append({
            "role": "user",
            "content": send
            })
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}"
            }
        payload = {
            "model": self.model,
            "messages":  message,
            "temperature": self.temperature,
            "max_tokens": 4096
            }

        for i in range(3):
            try:
                response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
                j = response.json()
                output = str(j['choices'][0]['message']['content'])
                # save text and img to  STM
                if self.save_stm:
                    self.text_stm.save_context({"input": input_text}, {"output": output})
                    for img in img_list:
                        self.img_stm.save_img(img)

                return j['choices'][0]['message']['content']
            except Exception as e:
                print(e)
                print(j["error"]["message"])
                continue
        return 'gpt error'