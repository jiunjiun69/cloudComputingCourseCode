import tkinter as tk
import jieba
import os
import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager
from wordcloud import WordCloud
import PIL
import numpy as np

root = tk.Tk()
root.geometry("400x240")

def textInputToImg():
    txt=textExample.get("1.0","end")
    words  = jieba.lcut(txt)
    
    counts = {}
    for word in words:
        if len(word) == 1: #排除單詞字數為1的詞
            continue 
        counts[word] = counts.get(word,0) + 1 #把單詞存進字典中
    
    items = list(counts.items()) #用items方法返回鍵值對
    items.sort(key=lambda x:x[1], reverse=True)
    
    printNumber = 10
    word = [None] * printNumber
    count = [None] * printNumber
    for i in range(printNumber):
        word[i], count[i] = items[i]
        
    path = '分析圖表'
    if not os.path.exists(path):
        os.mkdir(path)
        
    # 加入中文字型
    fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
    mpl.rc('font', family='Taipei Sans TC Beta')
        
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['figure.facecolor'] = 'white'
    plt.subplots(figsize=(10, 10))

    plt.barh(word,count) 
    plt.title("前十筆出現次數最多的單詞統計圖表") 
    plt.xlabel("出現次數") 
    plt.ylabel("單詞") 
    plt.savefig('分析圖表/高頻單詞統計圖表.png') #儲存高頻單詞統計圖表
    plt.show()
    
    #設定畫布大小
    mpl.rcParams['figure.figsize']=(20,20)

    #匯入圖片格式
    image1 = PIL.Image.open(r'leaf.png')
    MASK = np.array(image1)
    
    #獲取字型、設定背景顏色、設定字體size
    wordcloud=WordCloud(font_path='TaipeiSansTCBeta-Regular.ttf',background_color='white',max_font_size=80,mask = MASK)

    #利用前10個單詞畫圖
    word_frequence={x[0]:x[1] for x in items[0:printNumber]}
    wordcloud=wordcloud.fit_words(word_frequence)

    plt.imshow(wordcloud)
    plt.savefig('分析圖表/高頻單詞WordCloud詞雲圖.png') #儲存單詞WordCloud詞雲圖

    plt.axis("off")
    plt.show()
    
    

textExample=tk.Text(root, height=10)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="開始轉換", 
                    command=textInputToImg)

btnRead.pack()

root.mainloop()