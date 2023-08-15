from tkinter import *
from tkinter import font

root = Tk()
root.geometry("480x455")
root.title("SUDOKU SOLVER")
root.config(bg="black")

f = font.Font(size=15)

button_list = []
columns = []
rows = []
boxes = []

all_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def arrange_entries(i, j, b):
    if button_list != []:
        if button_list[-1][0] < i:
            button_list.append([i, j, b])
        elif button_list[-1][0] == i:
            if button_list[-1][1] < j:
                button_list.append([i, j, b])
            else:
                button_list.insert(-2, [i, j, b])
        else:
            for a in button_list:
                if a[0] == i:
                    if a[1] == j - 1:
                        button_list.insert(button_list.index(a) + 1, [i, j, b])

    else:
        button_list.append([i, j, b])


def get_info(i, j):
    info = [row_values[j - 1], column_values[i - 1]]

    for a in boxes:
        for s in a:
            if s[0] == i and s[1] == j:
                n = a.index(s)
                info.append(box_values[boxes.index(a)])
    return [info, n]


# checking what numbers cannot be placed on an i,j cell
def not_come(i, j):
    info = get_info(i, j)[0]
    present = []

    for m in info:
        for k in m:
            if k != 0 and k not in present:
                present.append(k)
    return present


def solve():
    change = 0

    # basic method
    for i in range(1, 10):
        for j in range(1, 10):

            cb = button_list[(i - 1) * 9 + j - 1][-1]

            if cb["text"] == "     ":
                if len(not_come(i, j)) == 8:
                    for k in all_num:
                        if k not in not_come(i, j):
                            cb["text"] = f" {k}  "
                            cb["fg"] = "blue"
                            change = 1
                            info = get_info(i, j)[0]
                            info[0][i - 1] = k
                            info[1][j - 1] = k
                            info[2][get_info(i, j)[-1]] = k
    # using rows
    for z in range(0, 9):
        row_v = row_values[z]
        row_b = rows[z]

        can_come = []
        for k in all_num:
            if k not in row_v:
                can_come.append(k)
        for num in can_come:
            check = []
            for b in row_b:
                i, j = b[0], b[1]
                if b[-1]["text"] == "     ":
                    present = not_come(i, j)
                    if num not in present:
                        check.append([num, b])
            if len(check) == 1:
                b = check[0][-1]
                i, j = b[0], b[1]

                b[-1]["text"] = f" {num}  "
                b[-1]["fg"] = "blue"

                change = 1
                info = get_info(i, j)[0]
                info[0][i - 1] = num
                info[1][j - 1] = num
                info[2][get_info(i, j)[-1]] = num
    # using columns
    for z in range(0, 9):
        row_v = column_values[z]
        row_b = columns[z]

        can_come = []
        for k in all_num:
            if k not in row_v:
                can_come.append(k)

        for num in can_come:
            check = []
            for b in row_b:
                i, j = b[0], b[1]
                if b[-1]["text"] == "     ":
                    present = not_come(i, j)
                    if num not in present:
                        check.append([num, b])
            if len(check) == 1:
                b = check[0][-1]
                i, j = b[0], b[1]

                b[-1]["text"] = f" {num}  "
                b[-1]["fg"] = "blue"
                change = 1
                info = get_info(i, j)[0]
                info[0][i - 1] = num
                info[1][j - 1] = num
                info[2][get_info(i, j)[-1]] = num
    # using boxes
    for z in range(0, 9):
        row_v = box_values[z]
        row_b = boxes[z]

        can_come = []
        for k in all_num:
            if k not in row_v:
                can_come.append(k)

        for num in can_come:
            check = []
            for b in row_b:
                i, j = b[0], b[1]
                if b[-1]["text"] == "     ":
                    present = not_come(i, j)
                    if num not in present:
                        check.append([num, b])
            if len(check) == 1:
                b = check[0][-1]
                i, j = b[0], b[1]

                b[-1]["text"] = f" {num}  "
                b[-1]["fg"] = "blue"
                change = 1
                info = get_info(i, j)[0]
                info[0][i - 1] = num
                info[1][j - 1] = num
                info[2][get_info(i, j)[-1]] = num

    if change == 1:
        solve()


def store():
    for i in rows:
        c = []
        for g in i:
            if g[-1]["text"] != "     ":
                c.append(int(g[-1]["text"]))
            else:
                c.append(0)
        row_values.append(c)

    for i in columns:
        c = []
        for g in i:
            if g[-1]["text"] != "     ":
                c.append(int(g[-1]["text"]))
            else:
                c.append(0)
        column_values.append(c)

    for i in boxes:
        c = []
        for g in i:
            if g[-1]["text"] != "     ":
                c.append(int(g[-1]["text"]))
            else:
                c.append(0)
        box_values.append(c)

    solve()


num_entry = Entry(root)
num_entry.grid(row=1, column=1, columnspan=9, pady=8)
num_entry.config(bg="black", borderwidth=0)

next_b = Button(root, text="solve", font=f, bg="black", fg="white", command=store)
next_b.grid(row=1, column=1, ipadx=5, columnspan=9)

# arranging and forming buttons
for i in range(1, 10):
    for j in range(1, 10):
        if i in [1, 2, 3, 7, 8, 9]:
            if j in [1, 2, 3, 7, 8, 9]:
                b = Button(root, text="     ", font=f, bg="light green")
                b.grid(row=i + 1, column=j, ipady=1, ipadx=1, padx=2, pady=2)
                arrange_entries(i, j, b)
            else:
                b = Button(root, text="     ", font=f, bg="#59990B")
                b.grid(row=i + 1, column=j, ipady=1, ipadx=1, padx=2, pady=2)
                arrange_entries(i, j, b)
        else:
            if j in [4, 5, 6]:
                b = Button(root, text="     ", font=f, bg="light green")
                b.grid(row=i + 1, column=j, ipady=1, ipadx=1, padx=2, pady=2)
                arrange_entries(i, j, b)
            else:
                b = Button(root, text="     ", font=f, bg="#59990B")
                b.grid(row=i + 1, column=j, ipady=1, ipadx=1, padx=2, pady=2)
                arrange_entries(i, j, b)

# forming columns
for i in range(1, 10):
    c = []
    for j in range(1, 10):
        c.append(button_list[(i - 1) * 9 + j - 1])
    columns.append(c)

# forming rows
for j in range(1, 10):
    c = []
    for i in range(1, 10):
        c.append(button_list[(i - 1) * 9 + j - 1])
    rows.append(c)

# forming boxes
b_1 = [0, 3, 6, 27, 30, 33, 54, 57, 60]
for ind in b_1:
    boxes.append(
        [button_list[ind], button_list[ind + 1], button_list[ind + 2], button_list[ind + 9], button_list[ind + 10],
         button_list[ind + 11], button_list[ind + 18], button_list[ind + 19], button_list[ind + 20]])

current_i = 0

prev_color = "light green"


# navigating
def change(ind, dir):
    global current_i
    global prev_color

    if num_entry.get() == "":
        pass
    elif not num_entry.get().isdigit():
        num_entry.delete(0, END)
        return

    if num_entry.get() == "0":
        a = "     "
    elif len(num_entry.get()) == 1:
        a = f"  {num_entry.get()} "
    elif len(num_entry.get()) == 0:
        a = "     "
    else:
        num_entry.delete(0, END)
        return

    if dir == "down":

        if button_list[ind][-1]["text"] != "     " and num_entry.get() == "":
            button_list[ind][-1].config(bg=prev_color)
        else:
            button_list[ind][-1].config(text=a, bg=prev_color)

        if button_list[ind][0] == 9 and button_list[ind][1] == 9:

            prev_color = button_list[0][-1]["bg"]
            button_list[0][-1].config(bg="yellow")
            current_i = 0
            num_entry.delete(0, END)

        elif button_list[ind][0] == 9 and button_list[ind][1] != 9:

            prev_color = button_list[button_list[ind][1]][-1]["bg"]
            button_list[button_list[ind][1]][-1].config(bg="yellow")
            current_i = button_list[ind][1]
            num_entry.delete(0, END)

        else:
            prev_color = button_list[ind + 9][-1]["bg"]
            button_list[ind + 9][-1].config(bg="yellow")
            current_i += 9
            num_entry.delete(0, END)

    elif dir == "up":

        if button_list[ind][-1]["text"] != "     " and num_entry.get() == "":
            button_list[ind][-1].config(bg=prev_color)
        else:
            button_list[ind][-1].config(text=a, bg=prev_color)

        if button_list[ind - 9][0] == 1 and button_list[ind - 9][1] == 1:
            prev_color = button_list[-1][-1]["bg"]
            button_list[-1][-1].config(bg="yellow")
            current_i = button_list.index(button_list[-1])
            num_entry.delete(0, END)

        elif button_list[ind][0] == 1 and button_list[ind - 9][1] != 1:
            prev_color = button_list[button_list[ind][1] + 70][-1]["bg"]
            button_list[button_list[ind][1] + 70][-1].config(bg="yellow")
            current_i = button_list[ind][1] + 70
            num_entry.delete(0, END)

        else:
            prev_color = button_list[ind - 9][-1]["bg"]
            button_list[ind - 9][-1].config(bg="yellow")
            current_i -= 9
            num_entry.delete(0, END)


    elif dir == "left":
        if button_list[ind][-1]["text"] != "     " and num_entry.get() == "":
            button_list[ind][-1].config(bg=prev_color)
        else:
            button_list[ind][-1].config(text=a, bg=prev_color)

        if button_list[ind][0] == 1 and button_list[ind][1] == 1:
            prev_color = button_list[-1][-1]["bg"]
            button_list[-1][-1].config(bg="yellow")
            current_i = button_list.index(button_list[-1])
            num_entry.delete(0, END)

        else:
            prev_color = button_list[ind - 1][-1]["bg"]
            button_list[ind - 1][-1].config(bg="yellow")
            current_i -= 1
            num_entry.delete(0, END)


    elif dir == "right":
        if button_list[ind][-1]["text"] != "     " and num_entry.get() == "":
            button_list[ind][-1].config(bg=prev_color)
        else:
            button_list[ind][-1].config(text=a, bg=prev_color)

        if button_list[ind][0] == 9 and button_list[ind][1] == 9:
            prev_color = button_list[0][-1]["bg"]
            button_list[0][-1].config(bg="yellow")
            current_i = 0
            num_entry.delete(0, END)

        else:
            prev_color = button_list[ind + 1][-1]["bg"]
            button_list[ind + 1][-1].config(bg="yellow")
            current_i += 1
            num_entry.delete(0, END)


def reset(event):
    new_v = event.char
    if new_v == "\r":
        store()
    if new_v == '\x1a':
        for i in range(1, 10):
            for j in range(1, 10):

                cb = button_list[(i - 1) * 9 + j - 1]

                if cb[-1]["fg"] == "blue":
                    cb[-1]["text"] = "     "
                    i, j = cb[0], cb[1]
                    info = get_info(i, j)[0]
                    info[0][i - 1] = 0
                    info[1][j - 1] = 0
                    info[2][get_info(i, j)[-1]] = 0


num_entry.bind("<Down>", lambda eff: change(current_i, "down"))
num_entry.bind("<Up>", lambda eff: change(current_i, "up"))
num_entry.bind("<Left>", lambda eff: change(current_i, "left"))
num_entry.bind("<Right>", lambda eff: change(current_i, "right"))
num_entry.bind("<Key>", reset)

num_entry.focus()

row_values = []
column_values = []
box_values = []

root.mainloop()
