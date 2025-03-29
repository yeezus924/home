import tkinter as tk

def draw_square():
    # Создаем квадрат
    square = canvas.create_rectangle(180, 250, 250, 300, fill="yellow")

def draw_house(canvas):
    # Рисуем основание домика (квадрат)
    canvas.create_rectangle(100, 150, 300, 350, fill="white", outline="black")

    # Рисуем крышу (треугольник)
    canvas.create_polygon(100, 150, 200, 50, 300, 150, fill="white", outline="black")

    # Рисуем окно (квадрат)
    canvas.create_rectangle(180, 250, 250, 300, fill="white", outline="black")

# Создаем главное окно
root = tk.Tk()
root.title("Домик")

# Создаем холст для рисования
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

button = tk.Button(root, text="Включить свет", command=draw_square)
button.pack()


# Рисуем домик
draw_house(canvas)

# Запускаем главный цикл
root.mainloop()