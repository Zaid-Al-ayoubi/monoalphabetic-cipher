import tkinter as tk
import random
import string


fixed_key ={'A':'Q','B':'W','C':'E','D':'R','E':'T','F':'Y','G':'U','H':'I','I':'O','J':'P','K':'A','L':'S','M':'D','N':'F','O':'G','P':'H','Q':'J','R':'K','S':'L','T':'Z','U':'X','V':'C','W':'V','X':'B','Y':'N','Z':'M'}
small_key = {k.lower(): v.lower() for k, v in fixed_key.items()}
reverse_fixed_key = {v: k for k, v in fixed_key.items()}
reverse_small_key = {v: k for k, v in small_key.items()}

def encrypt(plain_text):
    encrypted_text = ""
    for char in plain_text:
        if char.isupper():
            encrypted_text += fixed_key.get(char, char)
        elif char.islower():
            encrypted_text += small_key.get(char, char)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isupper():
            decrypted_text += reverse_fixed_key.get(char, char)
        elif char.islower():
            decrypted_text += reverse_small_key.get(char, char)
        else:
            decrypted_text += char
    return decrypted_text

def generate_random_key():
    global fixed_key, small_key, reverse_fixed_key, reverse_small_key

    letters = list(string.ascii_uppercase)  # ['A', 'B', ..., 'Z']
    shuffled = letters.copy()
    random.shuffle(shuffled)  # خلط عشوائي

    fixed_key = dict(zip(letters, shuffled))  # {'A': 'K', 'B': 'Q', ...}
    small_key = {k.lower(): v.lower() for k, v in fixed_key.items()}
    reverse_fixed_key = {v: k for k, v in fixed_key.items()}
    reverse_small_key = {v: k for k, v in small_key.items()}

    # إظهار نافذة تعلمك بالمفتاح الجديد
    show_key()

def show_key():
    key_window = tk.Toplevel(window)
    key_window.title("Substitution Key")
    key_window.geometry("200x500")

    key_text = ""
    for k in fixed_key:
        key_text += f"{k} → {fixed_key[k]}\n"

    label = tk.Label(key_window, text=key_text, justify="left", font=("Courier", 12))
    label.pack(padx=10, pady=10)

def encrypt_text():
    user_input = input_entry.get()
    result = encrypt(user_input)
    output_label.config(text="Encrypted: " + result)

def decrypt_text():
    user_input = input_entry.get()
    result = decrypt(user_input)
    output_label.config(text="Decrypted: " + result)

def clear_fields():
    input_entry.delete(0, tk.END)
    output_label.config(text="")

def copy_result():
    result_text = output_label.cget("text")
    if result_text.startswith("Encrypted: "):
        result_text = result_text.replace("Encrypted: ", "")
    elif result_text.startswith("Decrypted: "):
        result_text = result_text.replace("Decrypted: ", "")
    if result_text:
        window.clipboard_clear()
        window.clipboard_append(result_text)
        window.update()


window = tk.Tk()
window.title("Monoalphabetic Cipher")
window.geometry("400x400")


input_label = tk.Label(window, text="Enter text:")
input_label.pack()

input_entry = tk.Entry(window, width=50)
input_entry.pack()

output_label = tk.Label(window, text="")
output_label.pack(pady=10)


#frame one
frame_top = tk.Frame(window)
frame_top.pack(pady=5)

#frame tow
frame_middle = tk.Frame(window)
frame_middle.pack(pady=5)

#frame three
frame_bottom = tk.Frame(window)
frame_bottom.pack(pady=5)


tk.Button(frame_top, text="Encrypt", command=encrypt_text).pack(side="left", padx=5)
tk.Button(frame_top, text="Decrypt", command=decrypt_text).pack(side="left", padx=5)


tk.Button(frame_middle, text="Copy Result", command=copy_result).pack(side="left", padx=5)
tk.Button(frame_middle, text="Clear", command=clear_fields).pack(side="left", padx=5)


tk.Button(frame_bottom, text="Show Key", command=show_key).pack(side="left", padx=5)
tk.Button(frame_bottom, text="Generate Random Key", command=generate_random_key).pack(side="left", padx=5)


window.mainloop()


