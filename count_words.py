import tkinter as tk
import string

def count_chars(text, weights):
    count = 0
    for char in text:
        if char == '\n':
            count += weights['newline']
        elif char in string.ascii_letters:
            count += weights['eng']
        elif char in string.punctuation:
            count += weights['punct']
        elif char == ' ':
            count += weights['space']
        else:
            count += weights['char']
    return count

def update_count(*args):
    input_text = text_box.get("1.0", tk.END).strip()
    total_count = count_chars(input_text, {
        'char': char_weight.get(),
        'space': space_weight.get(),
        'eng': eng_weight.get(),
        'punct': punct_weight.get(),
        'newline': newline_weight.get()
    })
    count_label.config(text=f"총 문자 수: {total_count:.2f}")

def set_weights():
    weights = [
        char_weight_entry,
        space_weight_entry,
        eng_weight_entry,
        punct_weight_entry,
        newline_weight_entry
    ]
    for var in weights:
        value = float(var.get()) if var.get() else 1.0
        if var == char_weight_entry:
            char_weight.set(value)
        elif var == space_weight_entry:
            space_weight.set(value)
        elif var == eng_weight_entry:
            eng_weight.set(value)
        elif var == punct_weight_entry:
            punct_weight.set(value)
        elif var == newline_weight_entry:
            newline_weight.set(value)
    update_count()

# GUI 설정
root = tk.Tk()
root.title("글자수 세기")

# 가중치 입력 레이블과 엔트리
char_weight = tk.DoubleVar(value=1.0)
space_weight = tk.DoubleVar(value=1.0)
eng_weight = tk.DoubleVar(value=1.0)
punct_weight = tk.DoubleVar(value=1.0)
newline_weight = tk.DoubleVar(value=1.0)

weights = {
    'char': "글자 수:",
    'space': "공백 수:",
    'eng': "영문자 수:",
    'punct': "문장부호 수:",
    'newline': "줄바꿈 수:"
}

for key, label in weights.items():
    tk.Label(root, text=label).pack()
    entry = tk.Entry(root)
    entry.pack()
    entry.insert(0, "1")
    if key == 'char':
        char_weight_entry = entry
    elif key == 'space':
        space_weight_entry = entry
    elif key == 'eng':
        eng_weight_entry = entry
    elif key == 'punct':
        punct_weight_entry = entry
    elif key == 'newline':
        newline_weight_entry = entry

# 글자수 설정
set_weights_button = tk.Button(root, text="글자수 설정", command=set_weights)
set_weights_button.pack()

# 텍스트 박스
text_box = tk.Text(root)
text_box.pack(expand=True, fill=tk.BOTH)

count_label = tk.Label(root, text="총 글자수: 0.00")
count_label.pack()

# 실시간 업데이트
text_box.bind("<KeyRelease>", update_count)

# GUI 실행
root.mainloop()