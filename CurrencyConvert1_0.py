from tkinter import Tk, ttk
from tkinter import *
import requests
import json

root = Tk()
root.geometry('320x320')
root.title('Currency Converter')
#root.resizable(False,False)

# colorscu
cor0 = "#FFFFFF"  # WHITE
cor1 = "#333333"  # black
cor2 = "#EB5D51"  # red

# frames
top = Frame(root, width=320, height=60, bg=cor2)
top.grid(row=0, column=0)

main = Frame(root, width=320, height=260, bg=cor0)
main.grid(row=1, column=0)

def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1= combo1.get()
    currency_2= combo2.get()
    amount = value.get()

    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    headers = {
	    "X-RapidAPI-Key": "6a3e0eb192msh3595f8c74ed8f91p180bdajsne9bf14dfda1b",
	    "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
     }

    response = requests.get(url, headers=headers, params=querystring)

    data =json.loads(response.text)
    converted_amt  = data["result"]["convertedAmount"]
    formatted = "{:,.2f}".format(converted_amt)
    result['text']= formatted

    print(converted_amt,formatted)

app_name = Label( top, text="Currency Converter",font=('Arial 18 bold'),anchor=CENTER,bg=cor2,fg=cor1)
app_name.place(x=20, y=10)


result = Label(main, text="", width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Arial 15 bold'),
               bg=cor0, fg=cor1)    
result.place(x=50, y=10)

currency = ['CAD', 'GBP', 'EUR', 'INR', 'USD','AUD','JPY','CHF','NZD']

from_label = Label(main, text="From",relief="flat",anchor=NW,font=('Arial 10 bold'),bg=cor0,fg=cor1)
from_label.place(x=50, y=90)

combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=('Arial 10 bold'))
combo1['values'] = (currency)
combo1.place(x=50, y=120)

to_label = Label(main, text = "To", width=8, height=1, relief="flat", anchor=NW,
                   font=('Arial 10 bold'), bg=cor0, fg=cor1)
to_label.place(x=158, y=90)

combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=('Arial 10 bold'))
combo2['values'] = (currency)
combo2.place(x=160, y=120)

value = Entry(main,width=22,justify=CENTER,font=('Arial 10'),relief='solid')
value.place(x=50, y=155)

button = Button(main,text='Converter',width=19,padx=5,height=1,bg=cor2,fg=cor0,font=('Arial 10'),command=convert)
button.place(x=50, y=210)

root.mainloop()