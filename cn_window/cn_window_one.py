import tkinter as tk
import requests
from tkinter import scrolledtext
import threading

# 创建主窗口
root = tk.Tk()
# 设置窗口标题
root.title("我的窗口程序")
# 设置窗口大小
root.geometry("400x400")

# 在窗口中添加一个标签,创建一个欢迎信息
welcome_label = tk.Label(root, text="欢迎来到我的窗口程序！")
welcome_label.pack(pady=10)  # pack参数控制标签与窗口边缘的垂直间距

# 窗口扩展
# 文本框扩展，可以在其中输入文本
entry_label = tk.Label(root,text="请输入链接：")
entry_label.pack(pady=5)

# # 创建一个text控件用于多行输入
# text_entry = tk.Text(root,height=1,width=40)
# text_entry.pack(pady=10,expand=True,fill='both') # expand和fill确保Text控件随内容增长

#创建一个Entry控件用于输入链接
link_entry = tk.Entry(root,width=40)
link_entry.pack(pady=5)

# 创建一个按钮，点击后会将文本框的内容显示在下方的标签中
def show_entry_text():
    # text_to_show = text_entry.get() # 获取文本框中的内容
    # output_text.delete(1.0,tk.END) # 清空Text控件中的内容
    # output_text.insert(tk.END,text_to_show) # 在Text控件中插入文本
    # text_entry.delete(0,tk.END) # 清空Entry控件中的内容
    try:
        link_to_show = link_entry.get()
        if link_to_show:
            # 使用线程来避免阻塞GUI
            threading.Thread(target=show_link_content,args=(link_to_show,)).start()
        link_entry.delete('1.0', tk.END)
    except Exception as e:
        print(f"An error occurred: {e}")

button = tk.Button(root,text="完成",command = show_entry_text)
button.pack(pady=10)

# 创建显示区域的text控件，将输入的文本显示在下方的内容显示框中。
output_text = scrolledtext.ScrolledText(root,height=10,width=50)
output_text.pack(pady=10,expand=True,fill='both') # expand和fill确保Text控件随内容增长

# 定义一个函数，用于打开输入的内容
def show_link_content(link_to_show):
    try:
        # 使用requests库来获取链接内容
        response = requests.get(link_to_show)
        # 如果请求成功，则将内容显示在output_text中
        if response.status_code == 200:
            output_text.delete('1.0',tk.END)
            output_text.insert(tk.END,response.text)
    except Exception as e:
        # 如果发生错误，则在output_text中显示错误信息
        output_text.delete('1.0',tk.END)
        output_text.insert(tk.END,f"打开链接失败：{e}")

# 运行窗口程序
root.mainloop()