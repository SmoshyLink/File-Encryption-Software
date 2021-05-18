import tkinter as tk
from tkinter.filedialog import askopenfilename
import aes
import des
import rsa

def browse():
    allowed_filetypes = (
        ('Text files', '*.txt'),
        ('JPEG images', '*.jpg'),
        ('MS Word Documents', '*.docx')
    )

    picked_filename = askopenfilename(
        filetypes=allowed_filetypes
    )

    file_name.delete(0)
    file_name.insert(0, picked_filename)

def encrypt():
    file_to_encrypt = file_name.get()

    if algo.get() == 0: # AES
        key = aes_des_key.get()
        aes.encryptImage(file_to_encrypt, key)

    elif algo.get() == 1: # DES
        key = aes_des_key.get()
        key = des.get_key(key)
        key = des.get_round_keys(key)
        des.create_enc_file(des.run_des(des.get_file(file_to_encrypt), key),
                            file_to_encrypt)

    elif algo.get() == 2: # RSA
        key = rsa_privkey_pair.get()

def decrypt():
    file_to_decrypt = file_name.get()

    if algo.get() == 0: # AES
        key = aes_des_key.get()
        aes.decryptImage(file_to_decrypt, key)

    elif algo.get() == 1: # DES
        key = aes_des_key.get()
        key = des.get_key(key)
        key = des.get_round_keys(key)
        des.create_dec_file(des.decrypt_des(des.get_file(file_to_decrypt), key),
                        file_to_decrypt)

    elif algo.get() == 2: # RSA
        key = rsa_privkey_pair.get()

def run_app():
    window = tk.Tk()
    window.tk.call("tk", "scaling", 2.0)
    window.title("Multi-Algorithm Encryption / Decryption")
    window.resizable(False, False)

    file_name_label = tk.Label(window, text="File Name")
    file_name_label.grid(row=0, column=0)

    file_select_frame = tk.Frame(window)

    global file_name
    file_name = tk.Entry(file_select_frame)
    file_name.grid(row=0, column=0)
    browse_button = tk.Button(file_select_frame, text="Browse...",
                              command=browse)
    browse_button.grid(row=0, column=1)

    file_select_frame.grid(row=0, column=1)

    enc_dec_frame = tk.Frame(window)

    encrypt_button = tk.Button(enc_dec_frame, text="Encrypt", command=encrypt)
    decrypt_button = tk.Button(enc_dec_frame, text="Decrypt", command=decrypt)

    encrypt_button.grid(row=0, column=0)
    decrypt_button.grid(row=0, column=1)

    enc_dec_frame.grid(row=1, column=1)

    button_frame = tk.LabelFrame(window, text="Algorithm")
    global algo
    algo = tk.IntVar()

    aes_button = tk.Radiobutton(button_frame, text="AES", variable=algo, value=0)
    des_button = tk.Radiobutton(button_frame, text="DES", variable=algo, value=1)
    rsa_button = tk.Radiobutton(button_frame, text="RSA", variable=algo, value=2)

    aes_button.pack()
    des_button.pack()
    rsa_button.pack()

    button_frame.grid(row=2, column=0)

    key_frame = tk.LabelFrame(window, text="Keys")

    aes_des_key_label = tk.Label(key_frame, text="AES/DES Key")
    global aes_des_key
    aes_des_key = tk.Entry(key_frame)
    aes_info_label = tk.Label(key_frame, text="AES key: 32 or 64 hex chars")
    des_info_label = tk.Label(key_frame, text="DES keys: 16 hex chars")
    rsa_pubkey_pair_label = tk.Label(key_frame, text="RSA Public Key")
    rsa_pubkey_pair = tk.Entry(key_frame)
    rsa_privkey_pair_label = tk.Label(key_frame, text="RSA Private Key")
    rsa_privkey_pair = tk.Entry(key_frame)
    rsa_info_label = tk.Label(key_frame, text="RSA keys in the format of x,y")

    aes_des_key_label.grid(row=0, column=0)
    aes_des_key.grid(row=0, column=1)
    aes_info_label.grid(row=1, column=0)
    des_info_label.grid(row=1, column=1)
    rsa_pubkey_pair_label.grid(row=2, column=0)
    rsa_pubkey_pair.grid(row=2, column=1)
    rsa_privkey_pair_label.grid(row=3, column=0)
    rsa_privkey_pair.grid(row=3, column=1)
    rsa_info_label.grid(row=4, column=0)

    key_frame.grid(row=2, column=1)

    window.mainloop()

if __name__ == '__main__':
    run_app()
