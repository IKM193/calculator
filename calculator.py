import tkinter as tk
from tkinter import ttk

# define
BUTTON = [
    ['','B','AC','='],
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['00','0','.','+']
]

SYMBOL = ['+','-','*','/']

class CalGUI(object):
    def __init__(self,app=None):
        # define
        self.cal_str = ''

        # Window Setting
        app.title("簡易的な電卓") # タイトル
        app.geometry("400x600") # サイズ

        # Frame Setting
        cal_frame = ttk.Frame(app,width=300,height=100) # 計算式と結果用のFrame
        cal_frame.propagate(False) # サイズが固定される
        cal_frame.pack(side=tk.TOP,padx=10,pady=20) # 余白の設定
        button_frame = ttk.Frame(app,width=300,height=400) # 計算ボタン用のFrame
        button_frame.propagate(False) # サイズが固定される
        button_frame.pack(side=tk.BOTTOM) # 余白の設定

        # Parts Setting
        self.cal_var = tk.StringVar() # 計算式用の動的変数
        self.ans_var = tk.StringVar() # 結果用の動的変数
        cal_label = tk.Label(cal_frame, textvariable=self.cal_var, font=("",20)) # 計算式用のLabel
        ans_label = tk.Label(cal_frame, textvariable=self.ans_var, font=("",15)) # 結果用のLabel
        cal_label.pack(anchor=tk.E) # 右揃えで配置
        ans_label.pack(anchor=tk.E) # 右揃えで配置

        for y,row in enumerate(BUTTON,1): # Buttonの配置
            for x,num in enumerate(row):
                button = tk.Button(button_frame,text=num,font=('',15),width=6,height=3)
                button.grid(row=y,column=x) # 列や行を指定して配置
                button.bind('<Button-1>',self.click_button) # Buttonが押された場合
    
    def click_button(self,event):
        check = event.widget['text'] # 押したボタンのCheck

        if check == '=': # イコールの場合
            if self.cal_str[-1:] in SYMBOL: # 記号の場合、記号よりも前で計算
                self.cal_str = self.cal_str[:-1]
            
            res = '=' + str(eval(self.cal_str)) # eval関数の利用
            self.ans_var.set(res)
        elif check == 'AC': # クリアの場合
            self.cal_str = ''
            self.ans_var.set('')
        elif check == 'B': # バックの場合
            self.cal_str == self.cal_str[:-1]
        elif check in SYMBOL: # 記号の場合
            if self.cal_str[-1:] not in SYMBOL and self.cal_str[-1:] !='':
                self.cal_str += check
            elif self.cal_str[-1:] in SYMBOL: # 記号の場合、入れ替える
                self.cal_str = self.cal_str[:-1] + check
        else: # 数字などの場合
            self.cal_str += check
        
        self.cal_var.set(self.cal_str)
def main():
    app = tk.Tk()
    app.resizable(width=False,height=False)
    CalGUI(app)
    app.mainloop()

if __name__ == "__main__":
    main()