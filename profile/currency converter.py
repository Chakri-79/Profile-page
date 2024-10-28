import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import requests
from PIL import ImageTk, Image
import urllib.request

root = tk.Tk()
root.geometry("800x350")
root.title("Currency Converter")
root.maxsize(1000, 370)
root.minsize(600, 270)

# Fetch and resize image
url = "https://xp.io/storage/ADnRjfM.jpg"
res = urllib.request.urlopen(url)
img = Image.open(res)
resized = img.resize((300, 150), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)

def show_data():
    amount = E1.get()
    from_currency = c1.get()
    to_currency = c2.get()

    if not amount:
        messagebox.showerror("Currency Converter", "Please fill in the amount")
        return
    if not to_currency:
        messagebox.showerror("Currency Converter", "Please choose the currency")
        return

    try:
        amount = float(amount)
        url = 'http://api.currencylayer.com/live?access_key=YOUR_VALID_ACCESS_KEY'
        data = requests.get(url).json()
        
        # Combine from_currency and to_currency codes
        currency = from_currency.strip() + to_currency.strip()
        if currency in data['quotes']:
            cc = data['quotes'][currency]
            cur_conv = cc * amount
            E2.delete(0, "end")
            E2.insert(0, cur_conv)
            text.delete(1.0, 'end')
            text.insert('end', f'{amount} United States Dollar Equals = {cur_conv}\n\nLast time update: {datetime.now()}')
        else:
            messagebox.showerror("Currency Converter", "Conversion rate not available")
    except Exception as e:
        messagebox.showerror("Currency Converter", f"An error occurred: {e}")

def clear():
    E1.delete(0, "end")
    E2.delete(0, 'end')
    text.delete(1.0, 'end')

# GUI layout
Label(root, text="USD CURRENCY CONVERSION", font=('roboto', '12', 'bold')).place(x=200, y=8)
Label(root, text='Amount', font=('roboto', 11, 'bold')).place(x=20, y=10)
E1 = tk.Entry(root, width=20, borderwidth=2, font=('roboto', 11, 'bold'))
E1.place(x=20, y=40)

c1 = tk.StringVar(value="USD")
c2 = tk.StringVar()
currencychoose1 = ttk.Combobox(root, width=25, textvariable=c1, state='readonly', font=('roboto', 11, 'bold'))
currencychoose1['values'] = ['USD']
currencychoose1.place(x=300, y=40)

E2 = tk.Entry(root, width=20, borderwidth=1, font=('roboto', 11, 'bold'))
E2.place(x=20, y=80)

currencychoose2 = ttk.Combobox(root, width=25, textvariable=c2, state='readonly', font=('roboto', 11, 'bold'))
currencychoose2['values'] = (
    'ALL', 'AFN', 'ARS', 'AWG', 'AUD', 'AZN', 'BSD', 'BBD', 'BYN', 'BZD', 'BMD', 'BOB', 'BAM', 'BWP', 'BGN', 'BND',
    'KHR', 'CAD', 'KYD', 'CLP', 'CNY', 'COP', 'CRC', 'HRK', 'CUP', 'CZK', 'DKK', 'DOP', 'XCD', 'EGP', 'SVC', 'EUR',
    'FKP', 'FJD', 'GHS', 'GIP', 'GTQ', 'GGP', 'GYD', 'HNL', 'HKD', 'HUF', 'ISK', 'INR', 'IDR', 'IRR', 'IMP', 'ILS',
    'JMD', 'JPY', 'KZT', 'KPW', 'KRW', 'KGS', 'LAK', 'LBP', 'LRD', 'MKD', 'MYR', 'MUR', 'MXN', 'MNT', 'MZN', 'NAD',
    'NPR', 'ANG', 'NZD', 'NIO', 'NGN', 'NOK', 'OMR', 'PKR', 'PAB', 'PYG', 'PEN', 'PHP', 'PLN', 'QAR', 'RON', 'RUB',
    'SHP', 'SAR', 'RSD', 'SCR', 'SGD', 'SBD', 'SOS', 'ZAR', 'LKR', 'SEK', 'CHF', 'SRD', 'SYP', 'TWD', 'THD', 'TTD',
    'TRY', 'TVD', 'UAH', 'GPA', 'UYU', 'UZS', 'VEF', 'VND', 'YER', 'ZWD'
)
currencychoose2.place(x=300, y=90)

text = tk.Text(root, height=15, width=75, font=('verdana', '9', 'bold'))
text.place(x=100, y=120)
Button(root, text='Search', bg='green', command=show_data, font=('verdana', '10', 'bold')).place(x=20, y=120)
Button(root, text='Clear', bg='red', command=clear, font=('verdana', '10', 'bold')).place(x=20, y=170)

root.mainloop()
