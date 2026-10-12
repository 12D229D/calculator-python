
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.geometry("350x480")
        master.minsize(280, 380)
        master.configure(bg="#212121")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()
        
        # Bind keyboard events
        self.master.bind("<Key>", self.key_press)

    def create_widgets(self):
        # Configure main grid weights for responsiveness
        self.master.grid_rowconfigure(0, weight=1)  # Display area
        self.master.grid_rowconfigure(1, weight=5)  # Buttons area
        self.master.grid_columnconfigure(0, weight=1)

        # Display frame
        input_frame = tk.Frame(self.master, bd=0, relief="flat", bg="#212121")
        input_frame.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)
        input_frame.grid_columnconfigure(0, weight=1)
        input_frame.grid_rowconfigure(0, weight=1)

        # Display field (sleek entry with generous padding)
        input_field = tk.Entry(
            input_frame, 
            font=('Segoe UI', 26, 'bold'), 
            textvariable=self.input_text, 
            bg="#2d2d2d", 
            fg="#ffffff", 
            bd=0, 
            justify=tk.RIGHT,
            insertbackground="white" # cursor color
        )
        input_field.grid(row=0, column=0, sticky="nsew", ipady=12)

        # Buttons frame
        btns_frame = tk.Frame(self.master, bg="#212121")
        btns_frame.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 12))

        # Row & Column weights for button grid scaling
        for i in range(4):
            btns_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            btns_frame.grid_rowconfigure(i, weight=1)

        # Row 1: C (columnspan 3) and /
        self.create_button(btns_frame, "C", 0, 0, command=self.clear_button, bg_color="#d32f2f", fg_color="white", columnspan=3)
        self.create_button(btns_frame, "/", 0, 3, command=lambda: self.button_click('/'), bg_color="#f57c00")

        # Row 2: 7, 8, 9, *
        self.create_button(btns_frame, "7", 1, 0)
        self.create_button(btns_frame, "8", 1, 1)
        self.create_button(btns_frame, "9", 1, 2)
        self.create_button(btns_frame, "*", 1, 3, command=lambda: self.button_click('*'), bg_color="#f57c00")

        # Row 3: 4, 5, 6, -
        self.create_button(btns_frame, "4", 2, 0)
        self.create_button(btns_frame, "5", 2, 1)
        self.create_button(btns_frame, "6", 2, 2)
        self.create_button(btns_frame, "-", 2, 3, command=lambda: self.button_click('-'), bg_color="#f57c00")

        # Row 4: 1, 2, 3, +
        self.create_button(btns_frame, "1", 3, 0)
        self.create_button(btns_frame, "2", 3, 1)
        self.create_button(btns_frame, "3", 3, 2)
        self.create_button(btns_frame, "+", 3, 3, command=lambda: self.button_click('+'), bg_color="#f57c00")

        # Row 5: 0 (columnspan 2), ., =
        self.create_button(btns_frame, "0", 4, 0, columnspan=2)
        self.create_button(btns_frame, ".", 4, 2, command=lambda: self.button_click('.'))
        self.create_button(btns_frame, "=", 4, 3, command=self.equals_button, bg_color="#388e3c", fg_color="white")

    def create_button(self, frame, text, row, column, command=None, bg_color="#424242", fg_color="white", columnspan=1, rowspan=1):
        button = tk.Button(
            frame, 
            text=text, 
            fg=fg_color, 
            bg=bg_color,
            font=('Segoe UI', 14, 'bold'), 
            bd=0,
            activebackground=self.get_active_color(bg_color),
            activeforeground="white",
            command=command if command else lambda: self.button_click(text)
        )
        button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, padx=3, pady=3, sticky="nsew")

        # Visual micro-animations: smooth hover effect
        button.bind("<Enter>", lambda e: button.configure(bg=self.get_hover_color(bg_color)))
        button.bind("<Leave>", lambda e: button.configure(bg=bg_color))

        return button

    def get_hover_color(self, hex_color):
        hover_map = {
            "#424242": "#505050",
            "#f57c00": "#ff9800",
            "#d32f2f": "#e53935",
            "#388e3c": "#4caf50",
        }
        return hover_map.get(hex_color, hex_color)

    def get_active_color(self, hex_color):
        active_map = {
            "#424242": "#616161",
            "#f57c00": "#ffb74d",
            "#d32f2f": "#ef5350",
            "#388e3c": "#81c784",
        }
        return active_map.get(hex_color, hex_color)

    def button_click(self, item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def clear_button(self):
        self.expression = ""
        self.input_text.set("")

    def equals_button(self):
        try:
            # Replaces custom display characters if needed, then evaluates
            expr = self.expression
            result = str(eval(expr))
            self.input_text.set(result)
            self.expression = result
        except ZeroDivisionError:
            self.input_text.set("Error: Div/0")
            self.expression = ""
        except Exception:
            self.input_text.set("Error")
            self.expression = ""

    def key_press(self, event):
        char = event.char
        keysym = event.keysym

        if char in "0123456789.+-*/":
            self.button_click(char)
        elif keysym == "Return" or char == "=":
            self.equals_button()
        elif keysym == "BackSpace":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif keysym == "Escape":
            self.clear_button()

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
