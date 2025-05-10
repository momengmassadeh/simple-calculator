import tkinter as tk
from tkinter import messagebox

# دالة لإجراء العملية الحسابية
def perform_calculation():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
            symbol = "+"
        elif operation == "-":
            result = num1 - num2
            symbol = "-"
        elif operation == "*":
            result = num1 * num2
            symbol = "×"
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("خطأ", "لا يمكن القسمة على صفر!")
                return
            result = num1 / num2
            symbol = "÷"
        else:
            messagebox.showerror("خطأ", "يرجى اختيار عملية صحيحة.")
            return

        result_label.config(text=f"النتيجة: {result}")
        explain_operation(num1, num2, symbol, result)

    except ValueError:
        messagebox.showerror("خطأ", "يرجى إدخال أرقام صحيحة.")

# دالة لشرح العملية بطريقة مبسطة بدون ذكاء اصطناعي
def explain_operation(num1, num2, symbol, result):
    if symbol == "+":
        explanation = f"عندما نضيف {num1} إلى {num2}، كأننا نضع {num1} تفاحة مع {num2} تفاحة، فيصبح لدينا {result} تفاحة!"
    elif symbol == "-":
        explanation = f"عندما نطرح {num2} من {num1}، كأن معنا {num1} قطعة حلوى وأخذنا منها {num2}، يبقى معنا {result}."
    elif symbol == "×":
        explanation = f"الضرب يعني التكرار. {num1} × {num2} يعني أن نكرر {num1} عدد {num2} مرات، والناتج هو {result}."
    elif symbol == "÷":
        explanation = f"القسمة تعني توزيع. إذا وزعنا {num1} على {num2} أشخاص بالتساوي، كل واحد يأخذ {result}."
    else:
        explanation = "لا يمكن شرح هذه العملية."

    explanation_label.config(text=f"الشرح:\n{explanation}")

# دالة لمسح الحقول
def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="النتيجة:")
    explanation_label.config(text="الشرح:")

# إعداد الواجهة الرسومية
def setup_gui():
    global entry1, entry2, operation_var, result_label, explanation_label

    window = tk.Tk()
    window.title("آلة حاسبة ذكية للأطفال")
    window.geometry("400x400")
    window.configure(bg="#f0f8ff")

    tk.Label(window, text="مرحبًا بك في الآلة الحاسبة التعليمية", font=("Arial", 14, "bold"), bg="#f0f8ff", fg="#333").pack(pady=10)
    tk.Label(window, text="أدخل رقمين واختر عملية حسابية، وسنشرح لك النتيجة", bg="#f0f8ff", fg="blue").pack(pady=5)

    tk.Label(window, text="الرقم الأول:", bg="#f0f8ff").pack()
    entry1 = tk.Entry(window)
    entry1.pack()

    tk.Label(window, text="اختر العملية:", bg="#f0f8ff").pack()
    operation_var = tk.StringVar(window)
    operation_var.set("+")
    tk.OptionMenu(window, operation_var, "+", "-", "*", "/").pack()

    tk.Label(window, text="الرقم الثاني:", bg="#f0f8ff").pack()
    entry2 = tk.Entry(window)
    entry2.pack()

    tk.Button(window, text="احسب", command=perform_calculation).pack(pady=5)
    tk.Button(window, text="مسح", command=clear_fields).pack()

    result_label = tk.Label(window, text="النتيجة:", font=("Arial", 12), bg="#f0f8ff")
    result_label.pack(pady=10)

    explanation_label = tk.Label(window, text="الشرح:", wraplength=350, justify="right", bg="#f0f8ff")
    explanation_label.pack(pady=10)

    window.mainloop()

# تشغيل التطبيق
setup_gui()

