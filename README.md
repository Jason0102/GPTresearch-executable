# GPTresearch 使用指南
GPTresearch 是一款基於Open AI GPT-4 多模態大型語言模型所開發的研究輔助工具，旨在協助研究人員完成各項學術工作，可有效填補語言鴻溝，並縮減從發想到學術著作的研發週期。

![螢幕擷取畫面 2024-03-15 134410](https://github.com/Jason0102/GPT-research-executable/assets/57864575/50f2f0e4-02bd-4b7e-9d11-da2fc30c0242)

## 環境
* 必要: Windows 10/11, Microsoft Word
* 選配: pytesseract，下載安裝 https://digi.bib.uni-mannheim.de/tesseract/

## 執行版 (.exe)
步驟3~6為避免執行檔被windows 11防毒軟體擋掉，windows 10 可跳過
1. 連絡管理者取得授權並下載檔案: https://drive.google.com/drive/folders/1AOQoYaXLslQTJ89NRsKChc3JD1IYiWuL?usp=sharing
2. 開一個資料夾
3. 開始選單中搜尋「病毒」，並點選「病毒與威脅防護」。
4. 在「病毒與威脅防護設定」中，點選「管理設定」。
5. 捲動到底部，找到「排除項目」，點擊「新增或移除排除項目」。
6. 點選「新增排除範圍」，選擇你該資料夾。
7. 將檔案解壓縮至該資料夾。
8. 用文字文件開啟config.ini設定openai金鑰 [openai]key1, key2

![螢幕擷取畫面 2024-03-15 141215](https://github.com/Jason0102/GPT-research-executable/assets/57864575/24e01e10-6beb-4a57-9935-7ced28ee3d4c)

   
9. 用文字文件開啟config.ini設定pytesseract 路徑

![螢幕擷取畫面 2024-03-15 141233](https://github.com/Jason0102/GPT-research-executable/assets/57864575/2bf5efd1-113b-49d6-89f4-7251c7a9076a)

10. 點選GPTresearch.exe即可執行。

## 編譯版 (.py) 
1. 在python3.8的環境下執行:
   
    pip install -r requirements.txt
   
2. 新增資料夾./input_folder ./output_folder
3. 修改config.ini內部openai金鑰
4. 修改config.ini內部pytesseract的路徑 (optional)

## 檔案語路徑
* output_folder: 輸出的檔案在這裡
* config.ini: 設定檔

## 功能
執行版從介面選擇功能並輸入需要要求；編譯版從下列功能中擇一，修改並執行main.py。

### 1. 研究熱門關鍵字
    research_wordcloud(topic=研究領域, background_color='black', interval=1)
* 給定一個領域主題，搜尋近一年來的相關文章找出熱門研究方法，並繪製關鍵詞雲圖
* 一次一個領域主題
* background_color: 背景顏色
* interval: 搜尋時間範圍(年)
* 輸出檔案: 領域主題.png
* 執行版影片: https://youtu.be/s8YgKynFv3g

![Autonomous mobile robot_](https://github.com/Jason0102/GPTresearch-executable/assets/57864575/133752e3-40c0-4630-b37c-f354e904ad9c)


### 2. 以文章搜尋相關文獻
    search_paper_by_paragraph(paper_N=2, keyword_N=2)
* 給定一個文章、關鍵字數量與需要的文獻數量，從文字中提取關鍵字並搜尋相關聯的文獻
* 一次一個文件(.pdf/.docx)
* keyword_N: 要提取幾個關鍵字，paper_N: 每個關鍵字要找幾個文獻
* 輸出檔案: 輸入檔名_reference.docx
* 執行版影片: https://youtu.be/wJvj5dmvHR8
    
![螢幕擷取畫面 2024-03-05 150810](https://github.com/Jason0102/GPTresearch-executable/assets/57864575/cbcd7fd6-fdc6-4b15-806b-c470b76fe999)

### 3. 多論文閱讀分析 
    batch_analyze_paper(chinese=True)
* 給定論文內容，以英文找出該的資訊並分析該論文的方法、實驗、貢獻(0~100分)、缺點
* 一次多個文獻(.pdf/.docx)
* 可製作中文分析(chinese=True)
* 輸出檔案: Reading.docx / Reading_ch.docx
* 執行版影片: https://youtu.be/mWo5Ex-q-bc

![螢幕擷取畫面 2024-03-05 151453](https://github.com/Jason0102/GPTresearch-executable/assets/57864575/138dbbfe-f9d2-44bd-80f8-d012702439fd)

### 4. 論文英文校稿 
    grammar_check()
* 給定論文內容，修正文法錯誤並改用較學術的表達方式英文潤稿
* 一次一個文獻(.docx)
* 輸出檔案: 輸入檔名_revised.docx
* 執行版影片: https://youtu.be/IcUN8Xl_1ls

### 5. 專業領域翻譯 
    professinal_translation(domain="neurobiology", language='ch')
* 在指定範圍內將輸入翻譯成特定語言，範圍可自行輸入
* 支援中文(ch)、英文(en)、日文(jp)、德文(de)雙向翻譯
* 一次多個檔案(.docx)
* 輸出檔案: 輸入檔名_語言.docx
* 執行版影片: https://youtu.be/AxUKeB1OTyU
    
### 6. 解題助手 
    solve_problem(language='en')
* 給定題目的圖片，回覆該題目的解法與可能的答案
* 一次一個照片(.jpg/.png)
* 未安裝pytesseract不可使用 (安裝步驟2、3)
* 輸出檔案: 圖片檔名_answer.docx
* 題目是中文(ch)或者英文(en)
* 執行版影片: https://youtu.be/jINbLh1Feqk

![螢幕擷取畫面 2024-03-05 153429](https://github.com/Jason0102/GPTresearch-executable/assets/57864575/fe42e80e-78c7-4b39-bd47-acf2596fb448)

### 7. 碼農代工 
    coding(text1, language="C++")
* 產出符合要求的程式碼，所有流通的程式語言都可以
* 輸出檔案: 時間_程式語言.txt
* 執行版影片: https://youtu.be/A2X7DiNZQbw

### 8. 程式翻譯員 
    code_exchange(to_language="python")
* 將輸入的程式碼轉換成相同功能的其他程式語言
* 一次多個檔案(一般程式碼腳本)
* 輸出檔案: 輸入檔名_程式語言.txt
* 執行版影片: https://youtu.be/NsO7_za1y7E

### 9. 撰寫摘要 
    abstract(language='en', word=200)
* 輸入文章，依照字數要求產出摘要
* 一次多個檔案(.pdf/.docx)
* 可支援中文(ch)英文(en)
* 輸出檔案: 輸入檔名_abstract.txt
* 執行版影片: https://youtu.be/n9n4JuQq974

![螢幕擷取畫面 2024-03-05 154623](https://github.com/Jason0102/GPTresearch-executable/assets/57864575/42773c65-c403-45cd-8bf8-b60c636b593d)


### 10. 調整引用格式 
    reference_rearrange(reference_type=格式範例)
* 給定引用格式範例，將參考文獻的閱讀報告以出現順序做成引用列表
* 一次一個檔案(.docx)
* 輸出檔案: 輸入檔名_rereference.docx
* 執行版影片: https://youtu.be/8Yo3UFeYOiI

![螢幕擷取畫面 2024-03-05 155648](https://github.com/Jason0102/GPTresearch-executable/assets/57864575/6992dc28-d065-48cf-8a45-5623f4bd4b70)

### 11. 撰寫論文介紹章節 
    write_introduction_by_reference(word=1000, reference_type=格式範例)
* 輸入文獻閱讀的報告，以其中的文獻撰寫指定字數的Introduction，並在結尾以出現順序編排引用清單
* 一次一個檔案(.docx)
* 輸出檔案: 輸入檔名_introduction.docx
* 執行版影片: https://youtu.be/r8v-9UXeVtE

![螢幕擷取畫面 2024-03-05 163015](https://github.com/Jason0102/GPTresearch-executable/assets/57864575/3f416f96-6c5d-4c72-98e9-4d9ef44b799f)


## 備註
GPTresearch僅作為研究活動上的輔助工具，研究過程中的實驗、論證還需仰賴學者自身的學養與智識，任何產出的結果須經過人為查驗以確保知識的正確性。

## 資訊
CONTACT: d11522006@ntu.edu.tw

This work is supported by National Taiwan University Robotics Lab.

![logo](https://github.com/Jason0102/GPTresearch-executable/assets/57864575/4c975a44-2ef0-4e48-acdd-b52ec2173000)


    
