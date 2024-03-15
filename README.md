# GPTresearch執行版 使用指南
GPTresearch 是一款基於Open AI GPT-4 多模態大型語言模型所開發的研究輔助工具，旨在協助研究人員完成各項學術工作，可有效填補語言鴻溝，並縮減從發想到學術著作的研發週期。

![螢幕擷取畫面 2024-03-15 134410](https://github.com/Jason0102/GPT-research-executable/assets/57864575/50f2f0e4-02bd-4b7e-9d11-da2fc30c0242)

下載地址(請先連絡管理者取得檔名與密碼)

https://drive.google.com/drive/folders/1AOQoYaXLslQTJ89NRsKChc3JD1IYiWuL?usp=sharing

## 環境
* 必要: Windows 10/11, Microsoft Word
* 選配: pytesseract，下載安裝 https://digi.bib.uni-mannheim.de/tesseract/

## 使用 
步驟2~5避免執行檔被windows防毒軟體擋掉
1. 開一個資料夾
2. 開始選單中搜尋「病毒」，並點選「病毒與威脅防護」。
3. 在「病毒與威脅防護設定」中，點選「管理設定」。
4. 捲動到底部，找到「排除項目」，點擊「新增或移除排除項目」。
5. 點選「新增排除範圍」，選擇你該資料夾。
6. 將檔案解壓縮至該資料夾。
7. 用文字文件開啟config.ini內部openai金鑰 [openai]key1, key2
8. 點選GPTresearch.exe即可執行。

## 檔案語路徑
* output_folder: 輸出的檔案在這裡
* config.ini: 設定檔

## 功能
從下列功能中擇一，修改並執行main.py
### 熱門研究方向 
    research_wordcloud(topic=研究領域, background_color='black', interval=1)
* 給定一個領域主題，搜尋近一年來的相關文章找出熱門研究方法，並繪製關鍵詞雲圖
* 一次一個領域主題
* background_color: 背景顏色
* interval: 搜尋時間範圍(年)
* 輸出檔案: 領域主題.png

![working memory eeg](https://github.com/Jason0102/GPTresearch/assets/57864575/4b4a885c-21f5-4bda-aea3-77a87d9599f6)

### 參考文獻蒐集 
    search_paper_by_paragraph(paper_N=2, keyword_N=2)
* 給定一個文章、關鍵字數量與需要的文獻數量，從文字中提取關鍵字並搜尋相關聯的文獻
* 一次一個文件(.pdf/.docx)
* keyword_N: 要提取幾個關鍵字，paper_N: 每個關鍵字要找幾個文獻
* 輸出檔案: 輸入檔名_reference.docx
    
![圖片1](https://github.com/Jason0102/GPTresearch/assets/57864575/5bd8249e-d621-42cb-b0f7-32fe7fc5dea0)

### 論文分析 
    batch_analyze_paper(chinese=True)
* 給定論文內容，以英文找出該的資訊並分析該論文的方法、實驗、貢獻(0~100分)、缺點
* 一次多個文獻(.pdf/.docx)
* 可製作中文分析(chinese=True)
* 輸出檔案: Reading.docx / Reading_ch.docx

![圖片2](https://github.com/Jason0102/GPTresearch/assets/57864575/9b7670ec-7696-4904-befc-925b80501ced)


### 論文校稿 
    grammar_check()
* 給定論文內容，修正文法錯誤並改用較學術的表達方式英文潤稿
* 一次一個文獻(.docx)
* 輸出檔案: 輸入檔名_revised.docx

### 專業領域翻譯 
    professinal_translation(domain="neurobiology", language='ch')
* 在指定範圍內將輸入翻譯成特定語言，範圍可自行輸入
* 支援中文(ch)、英文(en)、日文(jp)、德文(de)雙向翻譯
* 一次多個檔案(.docx)
* 輸出檔案: 輸入檔名_語言.docx
    
### 解題助手 
    solve_problem(language='en')
* 給定題目的圖片，回覆該題目的解法與可能的答案
* 一次一個照片(.jpg/.png)
* 未安裝pytesseract不可使用 (安裝步驟2、3)
* 輸出檔案: 圖片檔名_answer.docx
* 題目是中文(ch)或者英文(en)
    
<img width="539" alt="圖片3" src="https://github.com/Jason0102/GPTresearch/assets/57864575/a1b3a061-8418-4c9d-a420-7830a8cfa5c0">

### 碼農代工 
    coding(text1, language="C++")
* 產出符合要求的程式碼，所有流通的程式語言都可以
* 輸出檔案: 時間_程式語言.txt

### 程式翻譯員 
    code_exchange(to_language="python")
* 將輸入的程式碼轉換成相同功能的其他程式語言
* 一次多個檔案(一般程式碼腳本)
* 輸出檔案: 輸入檔名_程式語言.txt

### 撰寫摘要 
    abstract(language='en', word=200)
* 輸入文章，依照字數要求產出摘要
* 一次多個檔案(.pdf/.docx)
* 可支援中文(ch)英文(en)
* 輸出檔案: 輸入檔名_abstract.txt

### 調整引用格式 
    reference_rearrange(reference_type=格式範例)
* 給定引用格式範例，將參考文獻的閱讀報告以出現順序做成引用列表
* 一次一個檔案(.docx)
* 輸出檔案: 輸入檔名_rereference.docx

### 撰寫介紹 
    write_introduction_by_reference(word=1000, reference_type=格式範例)
* 輸入文獻閱讀的報告，以其中的文獻撰寫指定字數的Introduction，並在結尾以出現順序編排引用清單
* 一次一個檔案(.docx)
* 輸出檔案: 輸入檔名_introduction.docx

<img width="521" alt="圖片4" src="https://github.com/Jason0102/GPTresearch/assets/57864575/97d644cf-57a5-407b-9641-fb059fba9593">

## 備註
GPTresearch僅作為研究活動上的輔助角色，研究過程中的實驗、論證還需仰賴學者自身的學養與智識，任何產出的結果須經過人為查驗以確保知識的正確性。

## 資訊
CONTACT: d11522006@ntu.edu.tw
This work is supported by National Taiwan University Robotics Lab.

![logo](https://github.com/Jason0102/GPTresearch/assets/57864575/0f5ad3ab-5cab-48ef-9cc6-51f0195e0220)
    
