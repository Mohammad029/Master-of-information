import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import pygame.mixer
import threading



class QuizApp: #
    
    def __init__(self, root) :
        self.root = root
        self.root.title("Master of information")

        
        
        
        self.question_label = None # لعرض الأسئلة 
        self.answer_buttons = [] # للاختيار من بين الخيارات المتاحة.
        self.next_button = None # للانتقال إلى السؤال التالي
        self.name_label = None #   يستخدم لعرض اسم المستخدم


        # حجم الشاشه 
    # def load_interface(self):
        window_width = 1000
        window_height = 700

        # لتوسيط البرنامج في الشاشه
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width - window_width) / 2
        y_coordinate = (screen_height - window_height) / 9
        self.root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

        # تحميل صوره خلفيه وضبط حجمها 
        self.bg_image = Image.open("C:\\Users\\Administrator\\Desktop\\pic2.jpg") 
        self.bg_image = self.bg_image.resize((window_width, window_height), Image.LANCZOS)
 # يقوم بتغيير حجم الصورة إلى الأبعاد المطلوبة باستخدام الطريقة resize من مكتبة PIL
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
#  لاستخدام الصور في واجهة  tkinter.
#  ثم تحويلها إلى PhotoImage , لانه هي الصيغة المطلوبه
                # Add Canvas background image
        self.canvas = tk.Canvas(root, width=window_width, height=window_height)
        self.canvas.pack()
        # ويتم تعيين عرضه وارتفاعه root في نافذة التطبيق  Canvas يُنشأ العنصر 
        # canvas ضروري انشاء كانفاس لاضافه الصور في مكتبه تي كنتر

        self.canvas.create_image(0, 0, anchor= tk.NW, image= self.bg_photo)
# anchor= يحدد موضع تثبيت الصورة / يعني أن الصورة ستكون مثبتة في الزاوية الشمالية الغربية
# يتم إنشاء صورة خلفية Canvas،  بعد إنشاء عنصر 

        
                # في الدالة __init__ أو في المكان المناسب، أضف الزر الجديد
        self.restart_button = tk.Button(self.canvas, text="إعادة الاختبار", bg="red", fg="white", cursor="hand2", command=self.restart_quiz)
        self.restart_button.place(relx=0.5, rely=0.96, anchor=tk.CENTER)


# الرساله الترحيبيه 
        
        self.label = tk.Label(self.canvas, text="!مرحبًا بك في لعبة الأسئلة", font=("Arial", 16, "bold"))
        self.label.place(relx= 0.5, rely= 0.1, anchor= tk.CENTER)
        #هو عنصر تسمية (Label) يستخدم لعرض نص الترحيب
        # يتم تعيين النص والخط والموقع النسبي (relx و rely) 

        # "أضف عنصر إدخال لاسم المستخدم"

        self.name_entry = tk.Entry(self.canvas, bg= "blue", fg= "white", font=("Helvetica", 12))
        self.name_entry.place(relx= 0.5, rely= 0.15, anchor= tk.CENTER)
        #  يسمح للمستخدم بإدخال اسمه. يتم تعيين خط النص والحجم 
        self.name_entry.insert(0, "Enter your name :")
# هنا اضفت داخل المربع اكتب اسمك هنا كرساله توضيحيه للمستخد
        
        def restart_quiz(self):
            pygame.mixer.music.stop()  # إيقاف الموسيقى عند إعادة الاختبار
            # قم بتدمير النافذة الحالية
            self.root.destroy()
            # إنشاء نافذة جديدة
            root = tk.Tk()
            # إعادة إنشاء التطبيق
            app = QuizApp(root)
            # تشغيل التطبيق
            root.mainloop()





        def clear_placeholder(event):
            if self.name_entry.get() == "Enter your name :": 
                self.name_entry.delete(0, tk.END)   
        
        self.name_entry.bind("<Button-1>", clear_placeholder)
# هون عندما يتم النقر للكتابه سيتم حذف المكتوب

        self.confirm_button = tk.Button(self.canvas, text="Confirm", bg="red", fg="white", cursor="hand2", command=self.show_name)
        self.confirm_button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
# هذا  يقوم بإنشاء زر في واجهة المستخدم
    def show_name(self):
        name = self.name_entry.get()
        if name:
            self.name_label = tk.Label(self.canvas, text=f"Hello *{name}*", font=("Helvetica", 18))
            self.name_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
            # self.start_button.config(state=tk.NORMAL)
        

        self.category_label = tk.Label(self.canvas, text="اختر فئة الأسئلة:", font=("Helvetica", 14))
        self.category_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        self.category_var = tk.StringVar()
        self.category_var.set(" Click",)

        self.category_options = ["المعرفة العامة", "التاريخ" ,"الذكاء", "الدين"]
        self.category_menu = tk.OptionMenu(self.canvas, self.category_var, *self.category_options) # tk.OptionMenu: يستخدم لإنشاء قائمة منسدلة.
    #  يظهر قائمة منسدلة تُسمى self.category_menu تحتوي على خيارات  من self.category_options، وتخزن القيمة المحددة في المتغير self.category_var.
        self.category_menu.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.start_button = tk.Button(self.canvas, text="ابدأ الاختبار", command=self.start_quiz)
        self.start_button.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        self.questions = []


    def start_quiz(self):

        pygame.init()  # تهيئة pygame
        pygame.mixer.music.load("C:\\Users\\Administrator\\Desktop\\videoplayback.mp3")  
          # تحميل ملف الموسيقى
        pygame.mixer.music.play(-1)  # تشغيل الموسيقى بشكل مستمر (-1)
        
        category = self.category_var.get()
        if category == "":
            messagebox.showerror(" !خطأ, الرجاء اختيار فئة")
        else:
            if category == "المعرفة العامة":
                self.questions = [
                    ("ما هي عاصمة فرنسا ؟", ["باريس", "لندن", "روما", "مدريد"]),
                    ("من الرسّام الذي رسم لوحة الموناليزا ؟  ", [" تيتيان ", "رافايلو ", " ليوناردو دا فينشي ", "مايكل أنجلو "]),
                    ("ما هو الرمز الكيميائي للماء ؟", ["CO2", "H2O", "O2", "HCl"]),
                    ("من هو الملاكم الذي انتصر أمام اللاعب محمد علي كلاي؟", [" روكي مارسيانو  ", "مايك تايسون", "جورج فورمان", "جو فرايزر  "]),
                    ("ما اسم أكبر دولة في العالم؟", ["كندا", "الصين", "روسيا", "الولايات المتحدة"])
                ]
            elif category == "التاريخ":
                self.questions = [
                    ("متى احتلت فلسطين؟", ["عام 1973  ", "عام 1967", "عام 1948", " عام 1987 "]),
                    ("متى انتهت الحرب العالمية الثانية؟", ["1950", "1939", "1918", "1945"]),
                    ("من هو الفرعون الذي بدأ ببناء أهرامات الجيزة؟", [" خوفو", "خفرع ", "خوني ", "خوفون "]),
                    ("متى تم تأسيس المملكة الأردنية الهاشمية؟  ", [" 22 مايو 1947", " 28 مايو 1946", " 25 مايو 1946", " 23 مايو 1947"]),
                    ("متى وقعت الثورة الفرنسية؟", ["1789", "1804", "1765", "1820"]),
                    ("ما هي أول حضارة معروفة في التاريخ؟ ", ["حضارة اليونان القديمة", "حضارة الهندوس في وادي السند ", " حضارة الفراعنة في مصر القديمة", "حضارة سومر في بلاد ما بين النهرين"])
                ]
            elif category == "الذكاء":
                self.questions = [
                    ("ما هو العاصمة الرسمية لليابان؟", ["طوكيو", "كيوتو", "أوساكا", "سيول"]),
                    ("ما هو ناتج جمع 2 + 2 * 2؟", ["6", "8", "4", "10"]),
                    ("ما هو الحيوان الذي يعتبر أسرع حيوان على وجه الأرض؟", ["الفهد", "الأفعى", "الثعلب", "الغزال"]),
                    ("ما هو العنصر الذي يشير إليه الرمز 'Fe' في الجدول الدوري؟", ["الحديد", "الزنك", "الكالسيوم", "الألمونيوم"]),
                    ("إذا كانت 10% من عدد ما تساوي 50، فما هو العدد؟", ["500", "100", "50", "200"]),
                    ("ما هو العضو الذي يقوم بتصفية الدم في جسم الإنسان؟", ["الكبد", "الكلى", "الطحال", "الرئتين"])
                ]

            elif category == "الدين":
                self.questions = [
                    ("ما هي أوَّل سورةٍ قرآنيَّةٍ نزلت على رسول الله -صلّى الله عليه وسلّم-؟", ["سورة الناس", "سورة العلق ", "سورة البقرة", "سورة الفاتحة"]),
                    ("كم مرَّة جاء ذكر الجنَّة في القرآن الكريم؟", [" 125 مرة", "137 مرة", "141 مرة", "139 مرة"]),
                    ("ما هي أوَّل صلاة صلَّيت في الإسلام بعد فرضها؟", ["صلاة المغرب", "صلاة العصر", "صلاة الظُّهر", "صلاة الفجر"]),
                    ("ما هي السورة الأولى في القرآن الكريم؟", ["الفاتحة", "البقرة", "العلق", "الإخلاص"]),
                    ("من هو النَّبيُّ الذّي ابتلعه الحوت؟", [" يونس - عليه السّلام", " موسى - عليه السّلام", " إسماعيل - عليه السّلام", "نوح - عليه السّلام"])
                ]
            # self.quiz_started = True

            self.display_questions()

    def display_questions(self):
        self.label.place_forget()
        self.name_entry.place_forget()
        self.confirm_button.place_forget()
        self.category_label.place_forget()
        self.category_menu.place_forget()
        self.start_button.place_forget()


        self.question_index = 0
        self.correct_answers = 0
        self.user_answers = []

        self.question_label = tk.Label(self.canvas, text=self.questions[self.question_index][0], font=("Helvetica", 18))  # تكبير حجم السؤال
        self.question_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)  # عرض السؤال في الوسط

        self.answer_buttons = []
        for i, answer in enumerate(self.questions[self.question_index][1]): #enumerate() تستخدم للحصول على كل عنصر في القائمة مع مؤشره. حيث يتم تخزين المؤشر في i والقيمة في answer
            button = tk.Button(self.canvas, text=answer, font=("Helvetica", 16), command=lambda idx=i: self.check_answer(idx),bg="lightgray" )
            button.place(relx=0.5, rely=0.5 + i * 0.1, anchor=tk.CENTER)
            button.config(cursor="hand2")  # تعيين شكل المؤشر لكل زر بعد إنشائه
            self.answer_buttons.append(button)

        self.next_button = tk.Button(self.canvas, text="التالي", font=("Helvetica", 14), command=self.next_question, state=tk.DISABLED) #  هذا الكود يقوم بإنشاء زر التالي  باستخدام عنصر تحكم Button في واجهة المستخدم 
        self.next_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        self.set_button_colors()



    def check_answer(self, selected_index): # هذه الدالة check_answer تقوم بفحص الإجابة التي اختارها المستخدم للسؤال الحالي.

        selected_answer = self.questions[self.question_index][1][selected_index]                 #selected_index: هو المؤشر (index) للإجابة التي اختارها المستخدم.
        correct_answer = self.get_correct_answer(self.category_var.get(), self.question_index)  #selected_answer: هو الإجابة التي اختارها المستخدم بناءً على المؤشر المحدد
        self.user_answers.append((self.questions[self.question_index][0], selected_answer))     #correct_answer: هو الإجابة الصحيحة للسؤال الحالي
                                                                                                #self.user_answers: قائمة تحتوي على إجابات المستخدم لكل سؤال
        if selected_answer == correct_answer:
            self.correct_answers += 1
        else:
            messagebox.showinfo("خطأ", f"الإجابة الصحيحة هي: {correct_answer}")  # في حالة أن الإجابة التي اختارها المستخدم تطابق الإجابة الصحيحة، يتم زيادة عدد الإجابات الصحيحة self.correct_answers بواحد. إذا كانت الإجابة غير صحيحة، ستظهر رسالة توضح الإجابة الصحيحة باستخدام messagebox.showinfo

        for button in self.answer_buttons:         #هذه الجزء من الشيفرة يقوم بتعطيل أزرار الإجابة بعد اختيار المستخدم لإجابة واحدة وتمكين زر التالي للانتقال إلى السؤال التالي
            button.config(state=tk.DISABLED)       # يتم تعطيله باستخدام button.config(state=tk.DISABLED)، مما يجعله غير قابل للنقر
        self.next_button.config(state=tk.NORMAL)   # يتم تمكين زر التالي باستخدام self.next_button.config(state=tk.NORMAL) للسماح للمستخدم بالانتقال إلى السؤال التالي 


    def next_question(self):  # هذا الدالة تقوم بالتبديل إلى السؤال التالي عندما ينقر المستخدم على زر "التالي".
        self.question_index += 1
        if self.question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.question_index][0])
            for button in self.answer_buttons:
                button.destroy()  # حذف أزرار الإجابة القديمة
            self.answer_buttons = []
            for i, answer in enumerate(self.questions[self.question_index][1]):
                button= tk.Button(self.canvas, text=answer, font=("Helvetica", 16), command=lambda idx=i: self.check_answer(idx), bg="lightgray")   

                button.place(relx=0.5, rely=0.5 + i * 0.1, anchor=tk.CENTER)
                button.config(cursor="hand2")  # تعيين شكل المؤشر لكل زر بعد إنشائه
                self.answer_buttons.append(button) # يضع زر الإجابة في المكان المناسب داخل النافذة
            self.next_button.config(state=tk.DISABLED) 
        else:
            self.show_results()

    def show_results(self):         # هذا الكود يقوم بإنشاء نص يحتوي على نتائج الاختبار بناءً على المعلومات التي تم جمعها خلال الاختبار

        pygame.mixer.music.stop()  # إيقاف الموسيقى عند عرض النتائج

        result_text = f"لقد أجبت {self.correct_answers} من أصل {len(self.questions)} إجابة صحيحة."
        result_text += "\n\nالإجابات الصحيحة:"
        for question, answer in self.user_answers:
            result_text += f"\n{question}: {self.get_correct_answer(self.category_var.get(), self.user_answers.index((question, answer)))}"
        messagebox.showinfo("النتيجة", result_text)

    def get_correct_answer(self, category, index):
        if category == "المعرفة العامة":
            return ["باريس", " ليوناردو دا فينشي ", "H2O", "جو فرايزر  ", "روسيا"][index]
        elif category == "التاريخ":
            return ["عام 1948", "1945", " خوفو", " 25 مايو 1946", "1789", "حضارة سومر في بلاد ما بين النهرين"][index]
        elif category == "الدين":
            return ["سورة العلق ", "139 مرة", "صلاة الظُّهر", "الفاتحة", " يونس - عليه السّلام"][index]
        elif category == "الذكاء":
            return ["طوكيو", "6", "الفهد", "الحديد", "500", "الكبد"][index]


    def set_button_colors(self):
        self.confirm_button.config(bg="blue", fg="white")
        self.start_button.config(bg="green", fg="white")
    def restart_quiz(self):
        # قم بغلق النافذة الحالية
        self.root.destroy()
        # إنشاء نافذة جديدة
        root = tk.Tk()
        # إعادة إنشاء التطبيق
        app = QuizApp(root)
        # تشغيل التطبيق
        # root.mainloop()




# Main

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
