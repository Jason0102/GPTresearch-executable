from toolbox.PaperSearchTool import search_paper_by_paragraph
from toolbox.PaperAnalyzeTool import  batch_analyze_paper
from toolbox.GrammarTool import grammar_check
from toolbox.SolverTool import solve_problem
from toolbox.TranslateTool import professinal_translation
from toolbox.CodingTool import coding, code_exchange
from toolbox.AbstractTool import abstract
from toolbox.IntroductionTool import reference_rearrange, write_introduction_by_reference
from toolbox.ResearchTrendTool import research_wrodcloud


import shutil
import os
import time
import threading
import configparser
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

config = configparser.ConfigParser()
config.read('config.ini')
INPUT_FOLDER = config.get('folder', 'input_folder')

class App():
    def __init__(self)-> None:
        self.app = tk.Tk()
        self.app.config(bg="white")
        self.app.title("GPTresearch v1.0")
        self.app.geometry('300x520+0+0')
        self.app.resizable( 0, 0)
        self.app.iconphoto(True, tk.PhotoImage(file='icon.png'))
        self.app.protocol("WM_DELETE_WINDOW", self.on_close_w0)
        self.mode = 0
        self.selected_option = tk.IntVar()
        self.language_option = tk.StringVar()
        self.Window2 = None
        self.state=0
        self.process_msg = "processing"
        self.t = threading.Thread(target=self.functions)
        self.t.start()

    def on_close_w0(self): 
            self.state=-1
            self.t.join()
            print("close")
            self.app.destroy()
            return 0

    def on_close_w1(self): 
            self.state=0
            self.Window1.destroy()
            return 0

    def on_close_w2(self): 
            return 0

    def functions(self):
        while True:
            time.sleep(0.001)
            if self.state == 2:
                try:
                    if self.mode == 1:
                        research_wrodcloud(topic=self.text_entry.get())
                    elif self.mode == 2:
                        search_paper_by_paragraph(paper_N=int(self.spinbox2.get()), keyword_N=int(self.spinbox1.get()))
                    elif self.mode == 3:
                        if self.language_option.get() == 'English/中文':
                            batch_analyze_paper(chinese=True)
                        else: 
                            batch_analyze_paper(chinese=False)
                    elif self.mode == 4:
                        grammar_check()  
                    elif self.mode == 5:
                        if self.language_option.get() == "English":
                            lang = 'en'
                        elif self.language_option.get() == "中文":
                            lang = 'ch'
                        elif self.language_option.get() == "日本語":
                            lang = 'jp'
                        elif self.language_option.get() == "Deutsch":
                            lang = 'de'
                        professinal_translation(domain=self.text_entry.get(), language=lang) 
                    elif self.mode == 6:
                        if self.language_option.get() == "English":
                            lang = 'en'
                        elif self.language_option.get() == "中文":
                            lang = 'ch'
                        solve_problem(language=lang)
                    elif self.mode == 7:
                        coding(self.text_entry1.get(), language=self.text_entry2.get())
                    elif self.mode == 8:
                        code_exchange(to_language=self.text_entry2.get())
                    elif self.mode == 9:
                        if self.language_option.get() == "English":
                            lang = 'en'
                        elif self.language_option.get() == "中文":
                            lang = 'ch'
                        if self.text_entry1.get() != int:
                            words = 100
                        elif int(self.text_entry1.get())>=0 and int(self.text_entry1.get())<10000:
                            words = int(self.text_entry1.get())
                        else:
                            words = 100
                        abstract(language=lang, word=words)
                    elif self.mode == 10:
                        if self.text_entry1.get() == "":
                            type = '[1] J.H. Lo, "Spatiotemporal Features of Working Memory EEG," NTUME Journal, Vol. 1, No. 1, pp.1-13, 2024.'
                        else: 
                            type = self.text_entry1.get()
                        reference_rearrange(reference_type=type)
                    elif self.mode == 11:
                        if self.text_entry1.get() != int:
                            words = 100
                        elif int(self.text_entry1.get())>=0 and int(self.text_entry1.get())<10000:
                            words = int(self.text_entry1.get())
                        else:
                            words = 100
                        if self.text_entry2.get() == "":
                            type = '[1] J.H. Lo, "Spatiotemporal Features of Working Memory EEG," NTUME Journal, Vol. 1, No. 1, pp.1-13, 2024.'
                        else: 
                            type = self.text_entry2.get()
                        write_introduction_by_reference(word=words, reference_type=type)
                    self.state = 1  
                except:
                    self.state = 1
            elif self.state == 1:
                if self.Window2 != None:
                    self.Window2.destroy()
                    self.Window2 = None
            elif self.state == 0:     
                self.mode = self.selected_option.get()
            elif self.state == -1:
                return 0

    def clean_input_folder(self):
        fileList = os.listdir(INPUT_FOLDER)
        for file in fileList:
            os.remove(INPUT_FOLDER + '/' + file)

    def load_single_file(self, type):
        if type == 'pdf':
            file_path = filedialog.askopenfilename(filetypes=(("PDF", "*.pdf"),))
        elif type == 'docx':
            file_path = filedialog.askopenfilename(filetypes=(("Word", "*.docx"),))
        elif type == 'png/jpg':
            file_path = filedialog.askopenfilename(filetypes=(("Files", "*.png \*.jpg"),))
        elif type == 'pdf/docx':
            file_path = filedialog.askopenfilename(filetypes=(("Files", "*.pdf \*.docx"),))
        else:
            file_path = filedialog.askopenfilename(filetypes=(("Files", "*.pdf \*.docx"),))
        if file_path:
            file_name = os.path.basename(file_path)
            shutil.copy(file_path, os.path.join(INPUT_FOLDER, file_name))
            return file_path
        else:
            return ""
    
    def load_multi_file(self, type):
        if type == 'pdf':
            file_paths = filedialog.askopenfilenames(filetypes=(("PDF", "*.pdf"), ))
        elif type == 'docx':
            file_paths = filedialog.askopenfilenames(filetypes=(("Word", "*.docx"), ))
        elif type == 'code':
            file_paths = filedialog.askopenfilenames(filetypes=(("Code", "*.*"), ))
        else:
            file_paths = filedialog.askopenfilenames(filetypes=(("Files", "*.pdf \*.docx"), ))
        if file_paths:
            for file_path in file_paths:
                # 獲取檔案名稱
                file_name = os.path.basename(file_path)
                # 複製檔案
                shutil.copy(file_path, os.path.join(INPUT_FOLDER, file_name))
            return file_paths
        else:
            return []

    def toggle(self):
        if self.toggle_text.cget("foreground") == "black":
            self.toggle_text.config(foreground="red")
        else:
            self.toggle_text.config(foreground="black")
        self.Window2.after(1000, self.toggle)

    def process_windows(self):
        if self.state != 1:
            return 0
        self.state = 2
        self.Window2 = tk.Toplevel(self.app)
        self.Window2.title("Don't close the window")
        self.Window2.protocol("WM_DELETE_WINDOW", self.on_close_w2)
        self.toggle_text = tk.Label(self.Window2, text=self.process_msg, font=("Arial", 16))
        self.toggle_text.pack()
        self.toggle()

    def submit_windows(self):
        if self.state != 0:
            return 0
        self.state = 1
        self.clean_input_folder()
        if self.selected_option.get() == 1:
            self.process_msg = "Generating wordcloud......................"
            self.Window1 = tk.Toplevel(self.app)
            self.Window1.protocol("WM_DELETE_WINDOW", self.on_close_w1)
            entry_label = tk.Label(self.Window1, text='Topic or keywords')
            entry_label.grid(row=0,column=0)
            self.text_entry = ttk.Entry(self.Window1)
            self.text_entry.grid(row=0,column=1)
            submit_button2 = ttk.Button(self.Window1, text="Submit", command=self.process_windows)
            submit_button2.grid(row=1,column=1)
        elif self.selected_option.get() == 2:
            filename = self.load_single_file('pdf/docx')
            if filename == "":
                self.state = 0
                return 
            self.process_msg = "Searching papers......................"
            self.Window1 = tk.Toplevel(self.app)
            self.Window1.protocol("WM_DELETE_WINDOW", self.on_close_w1)
            entry_label1 = tk.Label(self.Window1, text='Keywords')
            entry_label1.grid(row=0,column=0)
            self.spinbox1 = tk.Spinbox(self.Window1, from_=1, to=10)
            self.spinbox1.grid(row=0,column=1)
            self.spinbox1.configure(state="readonly")
            entry_label2 = tk.Label(self.Window1, text='Papers')
            entry_label2.grid(row=1,column=0)
            self.spinbox2 = tk.Spinbox(self.Window1, from_=1, to=100) 
            self.spinbox2.grid(row=1,column=1)
            self.spinbox2.configure(state="readonly")
            file_label1 = tk.Label(self.Window1, text='File: ')
            file_label1.grid(row=2,column=0)
            file_label2 = tk.Label(self.Window1, text=filename)
            file_label2.grid(row=2,column=1)
            submit_button2 = ttk.Button(self.Window1, text="Submit", command=self.process_windows)
            submit_button2.grid(row=3,column=1)
        elif self.selected_option.get() == 3:
            file_list = self.load_multi_file('pdf/docx')
            if file_list == []:
                self.state = 0
                return 
            filename = ""
            for file in file_list:
                filename = filename + file + '\n'
            self.process_msg = "Reading papers......................"
            self.Window1 = tk.Toplevel(self.app)
            self.Window1.protocol("WM_DELETE_WINDOW", self.on_close_w1)
            file_label1 = tk.Label(self.Window1, text='File: ')
            file_label1.grid(row=0,column=0)
            file_label2 = tk.Label(self.Window1, text=filename)
            file_label2.grid(row=0,column=1)
            options = ['English', 'English/中文']
            dropdown = ttk.Combobox(self.Window1, textvariable=self.language_option, values=options)
            dropdown.grid(row=0,column=2)
            dropdown.set('Choose a language')
            dropdown.configure(state="readonly")
            submit_button2 = ttk.Button(self.Window1, text="Submit", command=self.process_windows)
            submit_button2.grid(row=1,column=1)
        elif self.selected_option.get() == 4:
            filename = self.load_single_file('docx')
            if filename == "":
                self.state = 0
                return 
            self.process_msg = "Revising article......................"
            self.Window1 = tk.Toplevel(self.app)
            self.Window1.protocol("WM_DELETE_WINDOW", self.on_close_w1)
            file_label1 = tk.Label(self.Window1, text='File: ')
            file_label1.grid(row=0,column=0)
            file_label2 = tk.Label(self.Window1, text=filename)
            file_label2.grid(row=0,column=1)
            submit_button2 = ttk.Button(self.Window1, text="Submit", command=self.process_windows)
            submit_button2.grid(row=1,column=1)
            return
        elif self.selected_option.get() == 5:
            file_list = self.load_multi_file('docx')
            if file_list == []:
                self.state = 0
                return 
            filename = ""
            for file in file_list:
                filename = filename + file + '\n'
            self.process_msg = "Translating......................"
            self.Window1 = tk.Toplevel(self.app)
            self.Window1.protocol("WM_DELETE_WINDOW", self.on_close_w1)
            file_label1 = tk.Label(self.Window1, text='File: ')
            file_label1.grid(row=0,column=0)
            file_label2 = tk.Label(self.Window1, text=filename)
            file_label2.grid(row=0,column=1)    
            entry_label = tk.Label(self.Window1, text='Research domain')
            entry_label.grid(row=1,column=0)
            self.text_entry = ttk.Entry(self.Window1)
            self.text_entry.grid(row=1,column=1)
            options = ['English', '中文', '日本語', 'Deutsch']
            dropdown = ttk.Combobox(self.Window1, textvariable=self.language_option, values=options)
            dropdown.grid(row=2,column=0)
            dropdown.set('Choose a language')
            dropdown.configure(state="readonly")
            submit_button2 = ttk.Button(self.Window1, text="Submit", command=self.process_windows)
            submit_button2.grid(row=2,column=1)
        elif self.selected_option.get() == 6:
            filename = self.load_single_file('png/jpg')
            if filename == "":
                self.state = 0
                return 
            self.process_msg = "Solving problem......................"
            self.Window1 = tk.Toplevel(self.app)
            self.Window1.protocol("WM_DELETE_WINDOW", self.on_close_w1)
            file_label1 = tk.Label(self.Window1, text='File: ')
            file_label1.grid(row=0,column=0)
            file_label2 = tk.Label(self.Window1, text=filename)
            file_label2.grid(row=0,column=1)
            options = ['English', '中文']
            dropdown = ttk.Combobox(self.Window1, textvariable=self.language_option, values=options)
            dropdown.grid(row=1,column=0)
            dropdown.set('Language of problem?')
            dropdown.configure(state="readonly")
            submit_button2 = ttk.Button(self.Window1, text="Submit", command=self.process_windows)
            submit_button2.grid(row=1,column=1)
        elif self.selected_option.get() == 7:
            self.process_msg = "Generating code......................"
            self.Window1 = tk.Toplevel(self.app)
            self.Window1.protocol("WM_DELETE_WINDOW", self.on_close_w1)
            entry_label1 = tk.Label(self.Window1, text='Requirements')
            entry_label1.grid(row=0,column=0)
            self.text_entry1 = ttk.Entry(self.Window1)
            self.text_entry1.grid(row=0,column=1)
            entry_label2 = tk.Label(self.Window1, text='Programming language')
            entry_label2.grid(row=1,column=0)
            self.text_entry2 = ttk.Entry(self.Window1)
            self.text_entry2.grid(row=1,column=1)
            submit_button2 = ttk.Button(self.Window1, text="Submit", command=self.process_windows)
            submit_button2.grid(row=2,column=1)
        elif self.selected_option.get() == 8:
            file_list = self.load_multi_file('code')
            if file_list == []:
                self.state = 0
                return 
            filename = ""
            for file in file_list:
                filename = filename + file + '\n'
            self.process_msg = "Exchanging codes......................"
            self.Window1 = tk.Toplevel(self.app)
            self.Window1.protocol("WM_DELETE_WINDOW", self.on_close_w1)
            file_label1 = tk.Label(self.Window1, text='File: ')
            file_label1.grid(row=0,column=0)
            file_label2 = tk.Label(self.Window1, text=filename)
            file_label2.grid(row=0,column=1)  
            entry_label2 = tk.Label(self.Window1, text='To language: ')
            entry_label2.grid(row=1,column=0)
            self.text_entry2 = ttk.Entry(self.Window1)
            self.text_entry2.grid(row=1,column=1)  
            submit_button2 = ttk.Button(self.Window1, text="Submit", command=self.process_windows)
            submit_button2.grid(row=2,column=1)
        elif self.selected_option.get() == 9:
            file_list = self.load_multi_file('pdf/docx')
            if file_list == []:
                self.state = 0
                return 
            filename = ""
            for file in file_list:
                filename = filename + file + '\n'
            self.process_msg = "Condensing abstract......................"
            self.Window1 = tk.Toplevel(self.app)
            self.Window1.protocol("WM_DELETE_WINDOW", self.on_close_w1)
            file_label1 = tk.Label(self.Window1, text='File: ')
            file_label1.grid(row=0,column=0)
            file_label2 = tk.Label(self.Window1, text=filename)
            file_label2.grid(row=0,column=1)
            entry_label1 = tk.Label(self.Window1, text='Words: ')
            entry_label1.grid(row=1,column=0)
            self.text_entry1 = ttk.Entry(self.Window1)
            self.text_entry1.grid(row=1,column=1)
            options = ['English', '中文']
            dropdown = ttk.Combobox(self.Window1, textvariable=self.language_option, values=options)
            dropdown.grid(row=2,column=0)
            dropdown.set('Write in which language?')
            dropdown.configure(state="readonly")
            submit_button2 = ttk.Button(self.Window1, text="Submit", command=self.process_windows)
            submit_button2.grid(row=2,column=1)
        elif self.selected_option.get() == 10:
            filename = self.load_single_file('docx')
            if filename == "":
                self.state = 0
                return 
            self.process_msg = "Rearrange reference......................"
            self.Window1 = tk.Toplevel(self.app)
            self.Window1.protocol("WM_DELETE_WINDOW", self.on_close_w1)
            file_label1 = tk.Label(self.Window1, text='File: ')
            file_label1.grid(row=0,column=0)
            file_label2 = tk.Label(self.Window1, text=filename)
            file_label2.grid(row=0,column=1)
            entry_label1 = tk.Label(self.Window1, text='Reference example: ')
            entry_label1.grid(row=1,column=0)
            self.text_entry1 = ttk.Entry(self.Window1)
            self.text_entry1.grid(row=1,column=1)
            submit_button2 = ttk.Button(self.Window1, text="Submit", command=self.process_windows)
            submit_button2.grid(row=2,column=1)
        elif self.selected_option.get() == 11:
            filename = self.load_single_file('docx')
            if filename == "":
                self.state = 0
                return 
            self.process_msg = "Writing introduction......................"
            self.Window1 = tk.Toplevel(self.app)
            self.Window1.protocol("WM_DELETE_WINDOW", self.on_close_w1)
            file_label1 = tk.Label(self.Window1, text='File: ')
            file_label1.grid(row=0,column=0)
            file_label2 = tk.Label(self.Window1, text=filename)
            file_label2.grid(row=0,column=1)
            entry_label1 = tk.Label(self.Window1, text='Words: ')
            entry_label1.grid(row=1,column=0)
            self.text_entry1 = ttk.Entry(self.Window1)
            self.text_entry1.grid(row=1,column=1)
            entry_label2 = tk.Label(self.Window1, text='Reference example: ')
            entry_label2.grid(row=2,column=0)
            self.text_entry2 = ttk.Entry(self.Window1)
            self.text_entry2.grid(row=2,column=1)
            submit_button2 = ttk.Button(self.Window1, text="Submit", command=self.process_windows)
            submit_button2.grid(row=3,column=1)


    def run(self):
        # 主視窗
        frame = ttk.Frame(self.app)
        frame.pack()
        # frame.pack(padx=100, pady=100)
        # 標題
        label = tk.Label(frame, text = "GPTresearch v1.0")
        label.config(bg="white", font =("Courier", 14))
        label.pack()
        # 標誌
        img = Image.open('logo.png')        
        tk_img = ImageTk.PhotoImage(img) 
        logo = tk.Label(frame, image=tk_img, width=300, height=220)  
        logo.config(bg="white")
        logo.pack()
        # 選單
        radio1 = ttk.Radiobutton(frame, text="Research wordcloud/熱門研究方向", value=1, variable=self.selected_option)
        radio1.pack()
        radio2 = ttk.Radiobutton(frame, text="Search papers by paragraph/以文章蒐集論文", value=2, variable=self.selected_option)
        radio2.pack()
        radio3 = ttk.Radiobutton(frame, text="Analyze batch papers/論文分析", value=3, variable=self.selected_option)
        radio3.pack()
        radio4 = ttk.Radiobutton(frame, text="Check grammar/論文校稿", value=4, variable=self.selected_option)
        radio4.pack()
        radio5 = ttk.Radiobutton(frame, text="Domain translation/專業領域翻譯", value=5, variable=self.selected_option)
        radio5.pack()
        radio6 = ttk.Radiobutton(frame, text="Solve problem/解題助手", value=6, variable=self.selected_option)
        radio6.pack()
        radio7 = ttk.Radiobutton(frame, text="Coding/碼農代工", value=7, variable=self.selected_option)
        radio7.pack()
        radio8 = ttk.Radiobutton(frame, text="Exchange code with other language/程式翻譯員", value=8, variable=self.selected_option)
        radio8.pack()
        radio9 = ttk.Radiobutton(frame, text="Condense abstract/撰寫摘要", value=9, variable=self.selected_option)
        radio9.pack()
        radio10 = ttk.Radiobutton(frame, text="Rearrange reference type/調整引用格式", value=10, variable=self.selected_option)
        radio10.pack()
        radio11 = ttk.Radiobutton(frame, text="Write introduction by references/撰寫介紹", value=11, variable=self.selected_option)
        radio11.pack()
        submit_button1 = ttk.Button(frame, text="Submit", command=self.submit_windows)
        submit_button1.pack(pady=5)

        self.app.mainloop()



if __name__ == "__main__":
    app = App()
    app.run()


    # search_paper_by_paragraph(paper_N=2, keyword_N=2)
    # batch_analyze_paper(chinese=True)
    # grammar_check()
    # solve_problem(language='ch')
    # professinal_translation(domain="neurobiology", language='ch')
    # coding("請寫一個視窗包含一個文字輸入欄位、一個按鈕以及三個單選紐", language="python")
    # code_exchange(to_language="matlab")
    # abstract(language='en', word=200)
    # reference_rearrange(reference_type='[1] J.H. Lo, "Spatiotemporal Features of Working Memory EEG," NTUME Journal, Vol. 1, No. 1, pp.1-13, 2024.')
    # write_introduction_by_reference(word=250, reference_type='[1] J.H. Lo, "Spatiotemporal Features of Working Memory EEG," NTUME Journal, Vol. 1, No. 1, pp.1-13, 2024.')
    # research_wrodcloud(topic='Simultaneous localization and mapping', background_color='white')

