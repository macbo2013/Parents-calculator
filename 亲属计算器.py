import tkinter as tk
from tkinter import ttk, messagebox

RELATION_MAP = {
    ("爸爸", "爸爸"): ("爷爷", "爸爸的爸爸是什么？爸爸的爸爸是爷爷。"),
    ("爸爸", "妈妈"): ("奶奶", "爸爸的妈妈是什么？爸爸的妈妈是奶奶。"),
    ("妈妈", "爸爸"): ("外公", "妈妈的爸爸是什么？妈妈的爸爸是外公。"),
    ("妈妈", "妈妈"): ("外婆", "妈妈的妈妈是什么？妈妈的妈妈是外婆。"),
    ("哥哥", "妈妈"): ("妈妈", "哥哥的妈妈是什么？哥哥的妈妈是妈妈。"),
    ("姐姐", "爸爸"): ("爸爸", "姐姐的爸爸是什么？姐姐的爸爸是爸爸。"),
    ("爸爸", "哥哥"): ("伯伯", "爸爸的哥哥是什么？爸爸的哥哥是伯伯。"),
    ("爸爸", "弟弟"): ("叔叔", "爸爸的弟弟是什么？爸爸的弟弟是叔叔。"),
    ("爸爸", "姐姐"): ("姑姑", "爸爸的姐姐是什么？爸爸的姐姐是姑姑。"),
    ("爸爸", "妹妹"): ("姑姑", "爸爸的妹妹是什么？爸爸的妹妹是姑姑。"),
    ("妈妈", "姐姐"): ("姨妈", "妈妈的姐姐是什么？妈妈的姐姐是姨妈。"),
    ("妈妈", "妹妹"): ("姨妈", "妈妈的妹妹是什么？妈妈的妹妹是姨妈。"),
    ("妈妈", "哥哥"): ("舅舅", "妈妈的哥哥是什么？妈妈的哥哥是舅舅。"),
    ("妈妈", "弟弟"): ("舅舅", "妈妈的弟弟是什么？妈妈的弟弟是舅舅。"),
    ("爷爷", "爸爸"): ("曾祖父", "爷爷的爸爸是什么？爷爷的爸爸是曾祖父。"),
    ("奶奶", "爸爸"): ("曾祖父", "奶奶的爸爸是什么？奶奶的爸爸是曾祖父。"),
    ("爷爷", "妈妈"): ("曾祖母", "爷爷的妈妈是什么？爷爷的妈妈是曾祖母。"),
    ("奶奶", "妈妈"): ("曾祖母", "奶奶的妈妈是什么？奶奶的妈妈是曾祖母。"),
    ("外公", "爸爸"): ("外曾祖父", "外公的爸爸是什么？外公的爸爸是外曾祖父。"),
    ("外婆", "妈妈"): ("外曾祖母", "外婆的妈妈是什么？外婆的妈妈是外曾祖母。"),
    ("哥哥", "哥哥"): ("哥哥", "哥哥的哥哥是什么？哥哥的哥哥还是哥哥。"),
    ("姐姐", "姐姐"): ("姐姐", "姐姐的姐姐是什么？姐姐的姐姐还是姐姐。"),
    ("弟弟", "弟弟"): ("弟弟", "弟弟的弟弟是什么？弟弟的弟弟还是弟弟。"),
    ("妹妹", "妹妹"): ("妹妹", "妹妹的妹妹是什么？妹妹的妹妹还是妹妹。"),
    ("哥哥", "弟弟"): ("弟弟", "哥哥的弟弟是什么？哥哥的弟弟是弟弟。"),
    ("姐姐", "妹妹"): ("妹妹", "姐姐的妹妹是什么？姐姐的妹妹是妹妹。"),
    ("弟弟", "哥哥"): ("哥哥", "弟弟的哥哥是什么？弟弟的哥哥是哥哥。"),
    ("妹妹", "姐姐"): ("姐姐", "妹妹的姐姐是什么？妹妹的姐姐是姐姐。"),
    ("姑姑", "爸爸"): ("爷爷", "姑姑的爸爸是什么？姑姑的爸爸是爷爷。"),
    ("伯伯", "爸爸"): ("爷爷", "伯伯的爸爸是什么？伯伯的爸爸是爷爷。"),
    ("叔叔", "爸爸"): ("爷爷", "叔叔的爸爸是什么？叔叔的爸爸是爷爷。"),
    ("舅舅", "妈妈"): ("外公", "舅舅的妈妈是什么？舅舅的妈妈是外公。"),
    ("姨妈", "妈妈"): ("外婆", "姨妈的妈妈是什么？姨妈的妈妈是外婆。"),

}

RELATIONS = [
    "爸爸", "妈妈", "爷爷", "奶奶", "外公", "外婆", "哥哥", "姐姐", "弟弟", "妹妹", "姑姑", "伯伯", "叔叔", "舅舅", "姨妈", "曾祖父", "曾祖母", "外曾祖父", "外曾祖母"
]

RELATION_GROUPS = {
    "父母": ["爸爸", "妈妈"],
    "祖辈": ["爷爷", "奶奶", "外公", "外婆", "曾祖父", "曾祖母", "外曾祖父", "外曾祖母"],
    "兄弟姐妹": ["哥哥", "姐姐", "弟弟", "妹妹"],
    "旁系": ["姑姑", "伯伯", "叔叔", "舅舅", "姨妈",],
}

class RelativeCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("亲属计算器")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)


        self.step = 1
        self.first_var = tk.StringVar()
        self.second_var = tk.StringVar()
        self.first_selected = None
        self.second_selected = None

        self.label_step = ttk.Label(self.main_frame, text="请选择第一个亲属分组:")
        self.label_step.pack(pady=10)

        self.group_frame = tk.Frame(self.main_frame)
        self.group_frame.pack(pady=5)
        for group in RELATION_GROUPS:
            btn = ttk.Button(self.group_frame, text=group, command=lambda g=group: self.show_options(g))
            btn.pack(side=tk.LEFT, padx=5)

        self.option_frame = tk.Frame(self.main_frame)
        self.option_frame.pack(pady=5)

        self.confirm_btn = ttk.Button(self.main_frame, text="确定", command=self.confirm_option)
        self.confirm_btn.pack(pady=5)
        self.confirm_btn.pack_forget()

        self.label_step2 = ttk.Label(self.main_frame, text="请选择第二个亲属分组:")
        self.group_frame2 = tk.Frame(self.main_frame)
        self.option_frame2 = tk.Frame(self.main_frame)
        self.confirm_btn2 = ttk.Button(self.main_frame, text="确定", command=self.confirm_option2)
        self.confirm_btn2.pack_forget()

        self.result_label = ttk.Label(self.main_frame, text="结果将在这里显示", font=("微软雅黑", 12))
        self.result_label.pack(pady=20)

        self.think_label = ttk.Label(self.main_frame, text="思考过程将在这里显示", wraplength=350, font=("微软雅黑", 10))
        self.think_label.pack(pady=10)

        self.fullscreen_frame = None
        self.after_id = None

    def show_options(self, group):
        for widget in self.option_frame.winfo_children():
            widget.destroy()
        self.first_var.set("")
        for relation in RELATION_GROUPS[group]:
            btn = ttk.Button(self.option_frame, text=relation, command=lambda r=relation: self.select_first(r))
            btn.pack(side=tk.LEFT, padx=5)
        self.confirm_btn.pack()

    def select_first(self, relation):
        self.first_var.set(relation)
        self.first_selected = relation

    def confirm_option(self):
        if not self.first_var.get():
            messagebox.showwarning("提示", "请选择第一个亲属！")
            return
        self.label_step.pack_forget()
        self.group_frame.pack_forget()
        self.option_frame.pack_forget()
        self.confirm_btn.pack_forget()

        self.label_step2.pack(pady=10)
        self.group_frame2.pack(pady=5)
        for widget in self.group_frame2.winfo_children():
            widget.destroy()
        for group in RELATION_GROUPS:
            btn = ttk.Button(self.group_frame2, text=group, command=lambda g=group: self.show_options2(g))
            btn.pack(side=tk.LEFT, padx=5)
        self.option_frame2.pack(pady=5)

    def show_options2(self, group):
        for widget in self.option_frame2.winfo_children():
            widget.destroy()
        self.second_var.set("")
        for relation in RELATION_GROUPS[group]:
            btn = ttk.Button(self.option_frame2, text=relation, command=lambda r=relation: self.select_second(r))
            btn.pack(side=tk.LEFT, padx=5)
        self.confirm_btn2.pack()

    def select_second(self, relation):
        self.second_var.set(relation)
        self.second_selected = relation

    def confirm_option2(self):
        if not self.second_var.get():
            messagebox.showwarning("提示", "请选择第二个亲属！")
            return
        self.label_step2.pack_forget()
        self.group_frame2.pack_forget()
        self.option_frame2.pack_forget()
        self.confirm_btn2.pack_forget()
        self.calculate()

    def show_first_options(self, group):
        for widget in self.first_option_frame.winfo_children():
            widget.destroy()
        for relation in RELATION_GROUPS[group]:
            btn = ttk.Button(self.first_option_frame, text=relation, command=lambda r=relation: self.select_first(r))
            btn.pack(side=tk.LEFT, padx=5)

    def select_first(self, relation):
        self.first_var.set(relation)
        self.first_selected = relation

    def show_second_options(self, group):
        for widget in self.second_option_frame.winfo_children():
            widget.destroy()
        for relation in RELATION_GROUPS[group]:
            btn = ttk.Button(self.second_option_frame, text=relation, command=lambda r=relation: self.select_second(r))
            btn.pack(side=tk.LEFT, padx=5)

    def select_second(self, relation):
        self.second_var.set(relation)
        self.second_selected = relation

    def calculate(self):
        first = self.first_var.get()
        second = self.second_var.get()
        if not first or not second:
            messagebox.showwarning("提示", "请选择两个亲属！")
            return
        self.result, self.thinking = RELATION_MAP.get((first, second), ("未知", self.generate_thinking(first, second)))
        self.show_fullscreen_thinking(self.thinking)

    def show_fullscreen_thinking(self, text):
        self.main_frame.pack_forget()
        messagebox.showwarning("友情提示","等着，就快要摇到了")
        self.fullscreen_frame = tk.Frame(self)
        self.fullscreen_frame.pack(fill=tk.BOTH, expand=True)
        self.fullscreen_label = tk.Label(self.fullscreen_frame, text="", font=("微软雅黑", 32), wraplength=self.winfo_screenwidth()-100)
        self.fullscreen_label.pack(expand=True)
        self.animate_thinking_fullscreen(text)

    def animate_thinking_fullscreen(self, text, idx=0):
        if self.after_id:
            self.after_cancel(self.after_id)
        if idx <= len(text):
            self.fullscreen_label.config(text=text[:idx])
            self.after_id = self.after(1000, self.animate_thinking_fullscreen, text, idx+1)
        else:
            self.after_id = None
            self.after(1000, self.show_result_after_thinking)

    def show_result_after_thinking(self):
        self.fullscreen_frame.destroy()
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.result_label.config(text=f"结果：{self.result}")
        self.think_label.config(text=f"思考过程：{self.thinking}")

    def generate_thinking(self, first, second):
        return f"{first}的{second}是什么？{first}的{second}是……（暂未收录）"

if __name__ == "__main__":
    app = RelativeCalculator()
    app.mainloop()
