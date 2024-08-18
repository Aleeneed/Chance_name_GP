import tkinter as tk
from tkinter import filedialog
import os
import time

window=tk.Tk()
window.title('GP Chance Name Png')
window.geometry('380x400')
window.resizable(False, False)
def loadFile():
    if loadFile_en.get() is None:
        file_path = filedialog.askopenfilename(filetypes = (("png files","*.png"),("all files","*.*")))
        loadFile_en.insert(0,file_path) 
    else:
        file_path = filedialog.askopenfilename(filetypes = (("png files","*.png"),("all files","*.*")))
        loadFile_en.delete(0,'end')
        loadFile_en.insert(0,file_path)
lb = tk.Label(text="請選取檔案 :  ")
lb.grid(row=0, column=0)
loadFile_en = tk.Entry()
loadFile_en.grid(row=0, column=1)
rename_lb=tk.Label(text='遊戲名稱 :  ')
rename_lb.grid(row=1, column=0)
rename_entry = tk.Entry(window)
rename_entry.grid(row=1, column=1)


#GP Mode Type
gp_radioVar = tk.IntVar()
gp_radio1 = tk.Radiobutton(text='GP',variable=gp_radioVar, value=0)
gp_radio1.grid(row=2, column=0)
gp_radio2 = tk.Radiobutton(text='FAN GP',variable=gp_radioVar, value=1)
gp_radio2.grid(row=2, column=1)

#Mode Type
gp_version_radioVar = tk.IntVar()
gp_version_radio1 = tk.Radiobutton(text='default',variable=gp_version_radioVar, value=0)
gp_version_radio1.grid(row=3, column=0)
gp_version_radio2 = tk.Radiobutton(text='original',variable=gp_version_radioVar, value=1)
gp_version_radio2.grid(row=3, column=1)
gp_version_radio3 = tk.Radiobutton(text='xmode',variable=gp_version_radioVar, value=2)
gp_version_radio3.grid(row=3, column=2)
gp_version_radio4 = tk.Radiobutton(text='balanced',variable=gp_version_radioVar, value=3)
gp_version_radio4.grid(row=4, column=0)
gp_version_radio5 = tk.Radiobutton(text='performance',variable=gp_version_radioVar, value=4)
gp_version_radio5.grid(row=4, column=1)

#Time 
get_time=time.strftime("%m%d", time.localtime())
Time_set_radioVar=tk.IntVar()
Time_set_radioVar1 = tk.Radiobutton(text='當下時間',variable=Time_set_radioVar, value=0)
Time_set_radioVar1.grid(row=5, column=0)
Time_set_radioVar1 = tk.Radiobutton(text='自行輸入時間',variable=Time_set_radioVar, value=1)
Time_set_radioVar1.grid(row=5, column=1)
retime_lb=tk.Label(text='輸入時間  :  ')
retime_lb.grid(row=5, column=2)
retime_entry = tk.Entry(window)
retime_entry.insert(0,get_time)
retime_entry.grid(row=5, column=3)


def output():
    if Time_set_radioVar.get() == 0:
        if gp_version_radioVar.get() == 0 and gp_radioVar.get() == 0: #GP Mode and GP type is 0 
            os.rename(loadFile_en.get(),get_time+'_default_'+rename_entry.get().strip() +'.png')
        if gp_version_radioVar.get() == 0 and gp_radioVar.get() == 1:
            os.rename(loadFile_en.get(),get_time+'_default_Fan_'+rename_entry.get().strip() +'.png')
        if gp_version_radioVar.get() == 1 and gp_radioVar.get() == 0:
            os.rename(loadFile_en.get(),get_time+'_original_'+rename_entry.get().strip()+'.png')
        if gp_version_radioVar.get() == 1 and gp_radioVar.get() == 1:
            os.rename(loadFile_en.get(),get_time+'_original_Fan_'+rename_entry.get().strip()+'.png')
        if gp_version_radioVar.get() == 2 and gp_radioVar.get() == 0:
            os.rename(loadFile_en.get(),get_time+'_xmode_'+rename_entry.get().strip()+'.png')
        if gp_version_radioVar.get() == 2 and gp_radioVar.get()==1:
            os.rename(loadFile_en.get(),get_time+'_xmode_Fan_'+rename_entry.get().strip()+'.png')
        if gp_version_radioVar.get() == 3 and gp_radioVar.get()==0:
            os.rename(loadFile_en.get(),get_time+'_balanced_'+rename_entry.get().strip()+'.png')
        if gp_version_radioVar.get() == 3 and gp_radioVar.get()==1:
            os.rename(loadFile_en.get(),get_time+'_balanced_Fan_'+rename_entry.get().strip()+'.png')
        if gp_version_radioVar.get() == 4 and gp_radioVar.get()==0:
            os.rename(loadFile_en.get(),get_time+'_performace_'+rename_entry.get().strip()+'.png') 
        if gp_version_radioVar.get() == 4 and gp_radioVar.get()==1:    
            os.rename(loadFile_en.get(),get_time+'_performace_Fan_'+rename_entry.get().strip()+'.png')  
    else: 
        if gp_version_radioVar.get() == 0 and gp_radioVar.get()==0:
            os.rename(loadFile_en.get(),retime_entry.get()+'_default_'+rename_entry.get().strip() +'.png')        
        if gp_version_radioVar.get() == 0 and gp_radioVar.get()==1:
            os.rename(loadFile_en.get(),retime_entry.get()+'_default_Fan_'+rename_entry.get().strip() +'.png')
        if gp_version_radioVar.get() == 1 and gp_radioVar.get()==0:
            os.rename(loadFile_en.get(),retime_entry.get()+'_original_'+rename_entry.get().strip()+'.png')        
        if gp_version_radioVar.get() == 1 and gp_radioVar.get()==1:
            os.rename(loadFile_en.get(),retime_entry.get()+'_original_Fan_'+rename_entry.get().strip()+'.png')
        if gp_version_radioVar.get() == 2 and gp_radioVar.get()==0:
            os.rename(loadFile_en.get(),retime_entry.get()+'_xmode_'+rename_entry.get().strip()+'.png')
        if gp_version_radioVar.get() == 2 and gp_radioVar.get()==1:
            os.rename(loadFile_en.get(),retime_entry.get()+'_xmode_Fan_'+rename_entry.get().strip()+'.png')
        if gp_version_radioVar.get() == 3 and gp_radioVar.get()==0:
            os.rename(loadFile_en.get(),retime_entry.get()+'_balanced_'+rename_entry.get().strip()+'.png')
        if gp_version_radioVar.get() == 3 and gp_radioVar.get()==1:
            os.rename(loadFile_en.get(),retime_entry.get()+'_balanced_Fan_'+rename_entry.get().strip()+'.png')
        if gp_version_radioVar.get() == 4 and gp_radioVar.get()==1:
            os.rename(loadFile_en.get(),retime_entry.get()+'_performace_Fan_'+rename_entry.get().strip()+'.png') 
        if gp_version_radioVar.get() == 4 and gp_radioVar.get()==0:
            os.rename(loadFile_en.get(),retime_entry.get()+'_performace_'+rename_entry.get().strip()+'.png') 
            
loadFile_btn = tk.Button(text=".......",command=loadFile)
loadFile_btn.grid(row=0, column=2)
output_btn = tk.Button(text="改名",command=output)
output_btn.grid(row=6, column=1)
window.mainloop()
