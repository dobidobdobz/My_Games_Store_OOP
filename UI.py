from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from Search_epic import Search_epic
from search_steamdb import Search_steamdb
from search_GOG import Search_gog
from xboxgamepassPC import Search_Xbox
from io import BytesIO
import webbrowser

# Theme colors CONSTANTS
DARK_GREY = "#272727"
LOGO_GREEN = "#2df106"
DARKER_GREEN = "#31AF18"

# initializing OOP's
search_steam = Search_steamdb()
search_epic = Search_epic()
search_gog = Search_gog()
search_xbox = Search_Xbox()


# Function to update scroll region
def update_scroll_region():
    window.update()
    window.update_idletasks()  # Update all widgets first
    canvas.configure(scrollregion=canvas.bbox("all"))


# creates link that can be pressed
def open_link(url):
    webbrowser.open_new(url)


# converts url of img to the img object
def convert_img_url_to_img(url, reduction):
    headers = {"User-Agent": "Chrome/132.0.0.0"}
    response = requests.get(url, headers=headers, timeout=10, stream=True)

    if response.status_code != 200:
        print(f"Failed to download image: {url} (Status Code: {response.status_code})")
        return None
    response.raw.decode_content = True

    try:
        # open the data as image
        img = Image.open(BytesIO(response.content))

        # Calculate new size
        width, height = img.size
        new_width = int(width * (1 - reduction / 100))
        new_height = int(height * (1 - reduction / 100))

        # Resize the image
        img = img.resize((new_width, new_height))

        # Convert to Tkinter format
        img_to_display = ImageTk.PhotoImage(img)

        return img_to_display

    except:
        # open the data as image
        img = Image.open(response.raw)

        # Calculate new size
        width, height = img.size
        new_width = int(width * (1 - reduction / 100))
        new_height = int(height * (1 - reduction / 100))

        # Resize the image
        img = img.resize((new_width, new_height))

        # Convert to Tkinter format
        img_to_display = ImageTk.PhotoImage(img)

        return img_to_display


def search():
    global img_to_display, img_display, epic_games_image_1, epic_games_image_2, epic_games_label_game_image, epic_games_image_3
    global epic_games_image_4, gog_game_1_image, gog_game_2_image, gog_game_3_image, gog_game_4_image, gog_game_image
    global x_game_1_image, x_game_2_image, x_game_center_image, x_game_3_image, x_game_4_image

    # if no text in textbox display error
    if not search_bar_textbox.get():
        messagebox.showerror("Error", "You Must enter a name of game to search for you cannot search for game with a empty text field!")

    else:
        # resets labels and images if any
        steam_Label.config(text="STEAM")
        steam_game_data_label.configure(text="Please wait loading data...")
        epic_games_label.config(text="EPIC GAMES")
        epic_games_label_game_data.config(text="Please wait loading data...")
        gog_games_label.config(text="GOG GAMES")
        gog_games_label_game_data.configure(text="Please wait loading data...")
        steam_game_image.config(image=blank_photo)
        epic_games_label_game_data_image.config(image=blank_photo_for_steam)
        img_to_display = None
        epic_games_label_game_1.config(text="")
        epic_games_label_game_2.config(text="")
        epic_games_label_game_data.config( font=("Arial", 15, "bold"))
        epic_games_label_game_3.config(text="")
        epic_games_label_game_4.config(text="")
        purchase_epic_game_link_1.config(fg="black")
        purchase_epic_game_link_2.config(fg="black")
        purchase_epic_game_link.config(fg="black")
        purchase_epic_game_link_3.config(fg="black")
        purchase_epic_game_link_4.config(fg="black")
        epic_games_label_game_1_image.config(image=blank_photo_for_steam)
        epic_games_label_game_2_image.config(image=blank_photo_for_steam)
        epic_games_label_game_data_image.config(image=blank_photo_for_steam)
        epic_games_label_game_3_image.config(image=blank_photo_for_steam)
        epic_games_label_game_4_image.config(image=blank_photo_for_steam)
        gog_games_label_game_1.config(text="")
        gog_games_label_game_2.config(text="")
        gog_games_label_game_data.config(font=("Arial", 15, "bold"))
        gog_games_label_game_3.config(text="")
        gog_games_label_game_4.config(text="")
        purchase_gog_game_link_1.config(fg="black")
        purchase_gog_game_link_2.config(fg="black")
        purchase_gog_game_link.config(fg="black")
        purchase_gog_game_link_3.config(fg="black")
        purchase_gog_game_link_4.config(fg="black")
        gog_games_label_game_1_image.config(image=blank_photo_for_gog)
        gog_games_label_game_2_image.config(image=blank_photo_for_gog)
        gog_games_data_label_image.config(image=blank_photo_for_gog)
        gog_games_label_game_3_image.config(image=blank_photo_for_gog)
        gog_games_label_game_4_image.config(image=blank_photo_for_gog)
        xbox_game_pass_label.config(text="XBOX GAME PASS PC")
        xbox_game_center_info.configure(text="Please wait loading data...")
        xbox_game_1_info.config(text="")
        xbox_game_2_info.config(text="")
        xbox_game_3_info.config(text="")
        xbox_game_4_info.config(text="")
        purchase_xbox_subscript_link.config(fg="black")
        xbox_game_image_1.config(image=blank_photo_for_steam)
        xbox_game_image_2.config(image=blank_photo_for_steam)
        xbox_game_image_center.config(image=blank_photo_for_steam)
        xbox_game_image_3.config(image=blank_photo_for_steam)
        xbox_game_image_4.config(image=blank_photo_for_steam)
        window.geometry("1900x1080")
        window.update()

        # Create a separate Label for the clickable link
        purchase_link_label = Label(
            scrollable_frame,
            text="Purchase here",
            fg="black",  # Blue color to indicate a link
            bg="black",
            font=("Arial", 14, "underline"),
            cursor="hand2"
        )
        purchase_link_label.grid(column=2, row=6, pady=0)
        # Bind the label to the open_link function
        purchase_link_label.bind("<Button-1>", lambda e: open_link(steamdb_game_data[3]))

        window.update()

        # search steam for game
        steamdb_game_data = search_steam.search_steamdb(user_input=search_bar_textbox.get())

        # display image and reduce size by 10 percent
        img_display = convert_img_url_to_img(url=steamdb_game_data[0], reduction=10)

        # display image in label
        steam_game_image.config(image=img_display)

        # update label
        steam_game_data_label.configure(text=f"Title: {steamdb_game_data[1]} \n Price: {steamdb_game_data[2]}")

        # change link label to green from black to be visible
        purchase_link_label.config(fg=DARKER_GREEN)
        # refresh/update screen
        window.update()

        # search Epic Store
        epic_game_data = search_epic.search_epic(user_input=search_bar_textbox.get())
        if epic_game_data.__class__ == str:
            # display error no games found
            window.geometry("1900x1080")
            split = epic_game_data.split()
            split.insert(9, "\n")
            result = " ".join(split)
            epic_games_label_game_data.config(text=f"{result}")
            epic_games_label_game_1_image.config(image=game_not_found_image2port)
            epic_games_label_game_2_image.config(image=game_not_found_image2port)
            epic_games_label_game_data_image.config(image=game_not_found_image2port)
            epic_games_label_game_3_image.config(image=game_not_found_image2port)
            epic_games_label_game_4_image.config(image=game_not_found_image2port)
            window.geometry("1900x1080")
            window.update()

        else:
            window.geometry("1900x1080")
            # display epic games, first epic game
            try:
                epic_games_image_1 = convert_img_url_to_img(url=epic_game_data[0], reduction=35)
                epic_games_label_game_1_image.config(image=epic_games_image_1)
                epic_games_label_game_1.config(text=f"{epic_game_data[1]}")
                purchase_epic_game_link_1.config(fg=DARKER_GREEN)
                purchase_epic_game_link_1.bind("<Button-1>", lambda e: open_link(epic_game_data[2]))
                window.update()
            except:
                epic_games_label_game_1_image.config(image=game_not_found_image2port)
                epic_games_label_game_1.config(text=f"image\nno game found\nno price found")
                window.update()

            # second epic game
            try:
                epic_games_image_2 = convert_img_url_to_img(url=epic_game_data[3], reduction=35)
                epic_games_label_game_2_image.config(image=epic_games_image_2)
                epic_games_label_game_2.config(text=f"{epic_game_data[4]}")
                purchase_epic_game_link_2.config(fg=DARKER_GREEN)
                purchase_epic_game_link_2.bind("<Button-1>", lambda e: open_link(epic_game_data[5]))
                window.update()
            except:
                epic_games_label_game_2_image.config(image=game_not_found_image2port)
                epic_games_label_game_2.config(text=f"no game found\nno price found")
                window.update()

            # third epic game
            try:
                epic_games_label_game_image = convert_img_url_to_img(url=epic_game_data[6], reduction=35)
                epic_games_label_game_data_image.config(image=epic_games_label_game_image)
                epic_games_label_game_data.config(text=f"{epic_game_data[7]}", font=("Arial", 8, "bold"))
                epic_games_label_game_data.grid(column=2, row=9, pady=10)
                purchase_epic_game_link.config(fg=DARKER_GREEN)
                purchase_epic_game_link.bind("<Button-1>", lambda e: open_link(epic_game_data[8]))
                window.update()
            except:
                epic_games_label_game_data_image.config(image=game_not_found_image2port)
                epic_games_label_game_data.config(text=f"image\nno game found\nno price found")
                window.update()

            # fourth epic game
            try:
                epic_games_image_3 = convert_img_url_to_img(url=epic_game_data[9], reduction=35)
                epic_games_label_game_3_image.config(image=epic_games_image_3)
                epic_games_label_game_3.config(text=f"{epic_game_data[10]}")
                purchase_epic_game_link_3.config(fg=DARKER_GREEN)
                purchase_epic_game_link_3.bind("<Button-1>", lambda e: open_link(epic_game_data[11]))
                window.update()
            except:
                epic_games_label_game_3_image.config(image=game_not_found_image2port)
                epic_games_label_game_3.config(text=f"no game found\nno price found")
                window.update()

            # fifth epic game
            try:
                epic_games_image_4 = convert_img_url_to_img(url=epic_game_data[12], reduction=35)
                epic_games_label_game_4_image.config(image=epic_games_image_4)
                epic_games_label_game_4.config(text=f"{epic_game_data[13]}")
                purchase_epic_game_link_4.config(fg=DARKER_GREEN)
                purchase_epic_game_link_4.bind("<Button-1>", lambda e: open_link(epic_game_data[14]))
                window.update()
            except:
                epic_games_label_game_4_image.config(image=game_not_found_image2port)
                epic_games_label_game_4.config(text=f"no game found\nno price found")
                window.update()
            window.geometry("1900x1080")
            window.update()

        # search GOG games
        gog_game_data = search_gog.search_gog(user_input=search_bar_textbox.get())
        print(gog_game_data)

        if gog_game_data.__class__ == str:
            window.geometry("1900x1080")
            print('yes it is a str')
            # display error no games found
            gog_games_label_game_data.config(text=f"{gog_game_data}")
            gog_games_label_game_1_image.config(image=game_not_found_imagelandscape)
            gog_games_label_game_2_image.config(image=game_not_found_imagelandscape)
            gog_games_data_label_image.config(image=game_not_found_imagelandscape)
            gog_games_label_game_3_image.config(image=game_not_found_imagelandscape)
            gog_games_label_game_4_image.config(image=game_not_found_imagelandscape)
            window.geometry("1900x1080")
            window.update()

        else:
            window.geometry("1900x1080")
            # display games, GOG 1st game
            try:
                gog_game_1_image = convert_img_url_to_img(url=gog_game_data[0][1], reduction=60)
                gog_games_label_game_1_image.config(image=gog_game_1_image)
                gog_games_label_game_1.config(text=f"{gog_game_data[1]}")
                purchase_gog_game_link_1.config(fg=DARKER_GREEN)
                purchase_gog_game_link_1.bind("<Button-1>", lambda e: open_link(gog_game_data[2]))
                window.update()
            except:
                gog_games_label_game_1_image.config(image=game_not_found_imagelandscape)
                gog_games_label_game_1.config(text=f"no game found\nno price found")
                window.update()

            # GOG 2nd game
            try:
                gog_game_2_image = convert_img_url_to_img(url=gog_game_data[3][1], reduction=60)
                gog_games_label_game_2_image.config(image=gog_game_2_image)
                gog_games_label_game_2.config(text=f"{gog_game_data[4]}")
                purchase_gog_game_link_2.config(fg=DARKER_GREEN)
                purchase_gog_game_link_2.bind("<Button-1>", lambda e: open_link(gog_game_data[5]))
                window.update()
            except:
                gog_games_label_game_2_image.config(image=game_not_found_imagelandscape)
                gog_games_label_game_2.config(text=f"no game found\nno price found")
                window.update()

            # GOG 3rd game
            try:
                gog_game_image = convert_img_url_to_img(url=gog_game_data[6][1], reduction=60)
                gog_games_data_label_image.config(image=gog_game_image)
                gog_games_label_game_data.config(text=f"{gog_game_data[7]}", font=("Arial", 8, "bold"))
                gog_games_label_game_data.grid(column=2, row=13, pady=10)
                purchase_gog_game_link.config(fg=DARKER_GREEN)
                purchase_gog_game_link.bind("<Button-1>", lambda e: open_link(gog_game_data[8]))
                window.update()
            except:
                gog_games_data_label_image.config(image=game_not_found_imagelandscape)
                gog_games_label_game_data.config(text=f"no game found\nno price found", font=("Arial", 8, "bold"))
                window.update()

            # GOG 4th game
            try:
                gog_game_3_image = convert_img_url_to_img(url=gog_game_data[9][1], reduction=60)
                gog_games_label_game_3_image.config(image=gog_game_3_image)
                gog_games_label_game_3.config(text=f"{gog_game_data[10]}")
                purchase_gog_game_link_3.config(fg=DARKER_GREEN)
                purchase_gog_game_link_3.bind("<Button-1>", lambda e: open_link(gog_game_data[11]))
                window.update()
            except:
                gog_games_label_game_3_image.config(image=game_not_found_imagelandscape)
                gog_games_label_game_3.config(text=f"no game found\nno price found")
                window.update()

            # GOG 5th game
            try:
                gog_game_4_image = convert_img_url_to_img(url=gog_game_data[12][1], reduction=60)
                gog_games_label_game_4_image.config(image=gog_game_4_image)
                gog_games_label_game_4.config(text=f"{gog_game_data[13]}")
                purchase_gog_game_link_4.config(fg=DARKER_GREEN)
                purchase_gog_game_link_4.bind("<Button-1>", lambda e: open_link(gog_game_data[14]))
                window.update()
            except:
                gog_games_label_game_4_image.config(image=game_not_found_imagelandscape)
                gog_games_label_game_4.config(text=f"no game found\nno price found")
                window.update()
        window.geometry("1900x1080")
        window.update()

        # search for xbox games
        xbox_game_data = search_xbox.search_xbox(user_input=search_bar_textbox.get())
        print(xbox_game_data)

        # check if data is only a str no game found,  display it & images
        if xbox_game_data.__class__ == str:
            window.geometry("1900x1080")
            print('yes it is a str')
            # display error no games found
            xbox_game_center_info.config(text=f"{xbox_game_data}\non xbox game pass PC")
            xbox_game_image_1.config(image=game_not_found_image2port)
            xbox_game_image_2.config(image=game_not_found_image2port)
            xbox_game_image_center.config(image=game_not_found_image2port)
            xbox_game_image_3.config(image=game_not_found_image2port)
            xbox_game_image_4.config(image=game_not_found_image2port)
            window.update()

        else:
            # display games xbox 1st game
            try:
                x_game_1_image = convert_img_url_to_img(url=xbox_game_data[0], reduction=20)
                xbox_game_image_1.config(image=x_game_1_image)
                xbox_game_1_info.config(text=f"{xbox_game_data[1]}")
                window.update()
            except:
                xbox_game_image_1.config(image=game_not_found_image2port)
                xbox_game_1_info.config(text=f"no game found\nno price found")
                window.update()

            # xbox 2nd game
            try:
                x_game_2_image = convert_img_url_to_img(url=xbox_game_data[2], reduction=20)
                xbox_game_image_2.config(image=x_game_2_image)
                xbox_game_2_info.config(text=f"{xbox_game_data[3]}")
                window.update()
            except:
                xbox_game_image_2.config(image=game_not_found_image2port)
                xbox_game_2_info.config(text=f"no game found\nno price found")
                window.update()

            # xbox 3rd game
            try:
                x_game_center_image = convert_img_url_to_img(url=xbox_game_data[4], reduction=20)
                xbox_game_image_center.config(image=x_game_center_image)
                xbox_game_center_info.config(text=f"{xbox_game_data[5]}", font=("Arial", 8, "bold"))
                purchase_xbox_subscript_link.config(fg=DARKER_GREEN)
                window.update()
            except:
                xbox_game_image_center.config(image=game_not_found_image2port)
                xbox_game_center_info.config(text=f"no game found\nno price found", font=("Arial", 8, "bold"))
                window.update()

            # xbox 4th game
            try:
                x_game_3_image = convert_img_url_to_img(url=xbox_game_data[6], reduction=20)
                xbox_game_image_3.config(image=x_game_3_image)
                xbox_game_3_info.config(text=f"{xbox_game_data[7]}")
                window.update()
            except:
                xbox_game_image_3.config(image=game_not_found_image2port)
                xbox_game_3_info.config(text=f"no game found\nno price found")
                window.update()

            # xbox 5th game
            try:
                x_game_4_image = convert_img_url_to_img(url=xbox_game_data[8], reduction=20)
                xbox_game_image_4.config(image=x_game_4_image)
                xbox_game_4_info.config(text=f"{xbox_game_data[9]}")
                window.update()
            except:
                xbox_game_image_4.config(image=game_not_found_image2port)
                xbox_game_4_info.config(text=f"no game found\nno price found")
                window.update()

        window.geometry("1900x1080")
        window.update()


# Initialize the main window and setup
window = Tk()
window.title("My Games Store")
window.maxsize(1980, 1080)
window.geometry("1500x800")
window.config(bg="black")
window.iconbitmap('joystick.ico')

# create canvas for scrollbar
canvas = Canvas(window, bg="black")
canvas.grid(column=0, row=0, sticky="nsew")
# scrollbar
scrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
# Create a Frame inside the Canvas to hold all widgets
scrollable_frame = Frame(canvas, bg="black", pady=10)
# Link the scrollbar to the canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
# Create a window inside the canvas
canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="center")
# Configure grid to expand properly
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


# blank images for UI
# Create a blank (transparent) image
blank_image = Image.new("RGBA", (25, 25), (0, 0, 0, 0))  # Transparent 500x500
blank_photo = ImageTk.PhotoImage(blank_image)  # Convert to Tkinter-compatible image
# Create a blank (transparent) image
blank_image_for_steam = Image.new("RGBA", (200, 10), (0, 0, 0, 0))
blank_photo_for_steam = ImageTk.PhotoImage(blank_image_for_steam)  # Convert to Tkinter-compatible image
# Create blank (transparent) image
blank_image_for_gog = Image.new("RGBA", (275, 10), (0, 0, 0, 0))
blank_photo_for_gog = ImageTk.PhotoImage(blank_image_for_gog)  # Convert to Tkinter-compatible image
# game not found image landscape
default_image = Image.open("GAME NOT FOUND portrait.png")
default_image = default_image.resize(size=(300, 200))
game_not_found_imagelandscape = ImageTk.PhotoImage(default_image)
# game not found image portrait
default_image2port = Image.open("GAME NOT FOUND (1).png")
default_image2port = default_image2port.resize(size=(200, 300))
game_not_found_image2port = ImageTk.PhotoImage(default_image2port)
# Open and resize the image
original_image = Image.open("EPICcopy2.png")
resized_image = original_image.resize((250, 500))  # Adjust width and height as needed
My_logo = ImageTk.PhotoImage(resized_image)

# UI setup
logo_label = Label(scrollable_frame, image=My_logo, bg="black")
logo_label.grid(column=2, row=0)

# search bar
search_bar_textbox = Entry(scrollable_frame, width=28, bg=DARK_GREY, fg=DARKER_GREEN, borderwidth=0, insertbackground=LOGO_GREEN, font=("Arial", 13), justify="center")
search_bar_textbox.grid(row=2, column=2, pady=10)

# search button
search_button = Button(scrollable_frame, text="Search", font=("Arial", 15, "bold"), command=lambda: search(), width=20, borderwidth=0, bg=DARKER_GREEN)
search_button.grid(column=2, row=1, pady=12)

# search button
steam_Label = Label(scrollable_frame, text="", foreground=LOGO_GREEN, bg="black", font=("Arial", 15, "bold"))
steam_Label.grid(column=2, row=3, pady=10)

# steam image labels & data labels
steam_game_image = Label(scrollable_frame, bg="black", image=blank_photo)
steam_game_image.grid(column=2, row=4)
steam_game_data_label = Label(scrollable_frame, text="", bg="black", font=("Arial", 15, "bold"), foreground=LOGO_GREEN)
steam_game_data_label.grid(column=2, row=5)

# epic game label's
epic_games_label = Label(scrollable_frame, text="", bg="black", font=("Arial", 15, "bold"), foreground=LOGO_GREEN)
epic_games_label.grid(column=2, row=7, pady=10)

# center image, game info, purchase link,
epic_games_label_game_data_image = Label(scrollable_frame, bg="black", image=blank_photo_for_steam)
epic_games_label_game_data_image.grid(column=2, row=8, pady=5)
epic_games_label_game_data = Label(scrollable_frame, text="", bg="black", font=("Arial", 15, "bold"), foreground=LOGO_GREEN)
epic_games_label_game_data.grid(column=2, row=9, pady=5)
purchase_epic_game_link = Label(scrollable_frame, text="Purchase here", fg="black", bg="black", font=("Arial", 8, "underline"), cursor="hand2")
purchase_epic_game_link.grid(column=2, row=10, pady=0)

epic_games_label_game_1 = Label(scrollable_frame, text="", bg="black", font=("Arial", 8, "bold"), foreground=LOGO_GREEN)
epic_games_label_game_1.grid(column=0, row=9, padx=0)
purchase_epic_game_link_1 = Label(scrollable_frame, text="Purchase here", fg="black", bg="black", font=("Arial", 8, "underline"), cursor="hand2")
purchase_epic_game_link_1.grid(column=0, row=10, pady=0)
epic_games_label_game_1_image = Label(scrollable_frame, bg="black", image=blank_photo_for_steam)
epic_games_label_game_1_image.grid(column=0, row=8, pady=5, padx=(0, 0))

epic_games_label_game_2 = Label(scrollable_frame, text="", bg="black", font=("Arial", 8, "bold"), foreground=LOGO_GREEN)
epic_games_label_game_2.grid(column=1, row=9, padx=0)
purchase_epic_game_link_2 = Label(scrollable_frame, text="Purchase here", fg="black", bg="black", font=("Arial", 8, "underline"), cursor="hand2")
purchase_epic_game_link_2.grid(column=1, row=10, pady=0)
epic_games_label_game_2_image = Label(scrollable_frame, bg="black", image=blank_photo_for_steam)
epic_games_label_game_2_image.grid(column=1, row=8, pady=5, padx=70)

epic_games_label_game_3 = Label(scrollable_frame, text="", bg="black", font=("Arial", 8, "bold"), foreground=LOGO_GREEN)
epic_games_label_game_3.grid(column=3, row=9, padx=0)
purchase_epic_game_link_3 = Label(scrollable_frame, text="Purchase here", fg="black", bg="black", font=("Arial", 8, "underline"), cursor="hand2")
purchase_epic_game_link_3.grid(column=3, row=10, pady=0)
epic_games_label_game_3_image = Label(scrollable_frame, bg="black", image=blank_photo_for_steam)
epic_games_label_game_3_image.grid(column=3, row=8, pady=5, padx=70)

epic_games_label_game_4 = Label(scrollable_frame, text="", bg="black", font=("Arial", 8, "bold"), foreground=LOGO_GREEN)
epic_games_label_game_4.grid(column=4, row=9, padx=0)
purchase_epic_game_link_4 = Label(scrollable_frame, text="Purchase here", fg="black", bg="black", font=("Arial", 8, "underline"), cursor="hand2")
purchase_epic_game_link_4.grid(column=4, row=10, pady=0)
epic_games_label_game_4_image = Label(scrollable_frame, bg="black", image=blank_photo_for_steam)
epic_games_label_game_4_image.grid(column=4, row=8, pady=5, padx=(0, 0))

# gog games label divider
gog_games_label = Label(scrollable_frame, text="", bg="black", font=("Arial", 15, "bold"), foreground=LOGO_GREEN)
gog_games_label.grid(column=2, row=11, pady=10)

# center game data
gog_games_data_label_image = Label(scrollable_frame, bg="black", image=blank_photo_for_gog)
gog_games_data_label_image.grid(column=2, row=12, pady=5)
gog_games_label_game_data = Label(scrollable_frame, text="", bg="black", font=("Arial", 15, "bold"), foreground=LOGO_GREEN)
gog_games_label_game_data.grid(column=2, row=13, pady=5)
purchase_gog_game_link = Label(scrollable_frame, text="Purchase here", fg="black", bg="black", font=("Arial", 8, "underline"), cursor="hand2")
purchase_gog_game_link.grid(column=2, row=14, pady=0)

# game data left
gog_games_label_game_1_image = Label(scrollable_frame, bg="black", image=blank_photo_for_gog)
gog_games_label_game_1_image.grid(column=0, row=12, pady=5, padx=0)
gog_games_label_game_1 = Label(scrollable_frame, text="", bg="black", font=("Arial", 8, "bold"), foreground=LOGO_GREEN)
gog_games_label_game_1.grid(column=0, row=13, padx=0)
purchase_gog_game_link_1 = Label(scrollable_frame, text="Purchase here", fg="black", bg="black", font=("Arial", 8, "underline"), cursor="hand2")
purchase_gog_game_link_1.grid(column=0, row=14, pady=0)

# game data left 2
gog_games_label_game_2_image = Label(scrollable_frame, bg="black", image=blank_photo_for_gog)
gog_games_label_game_2_image.grid(column=1, row=12, pady=5, padx=0)
gog_games_label_game_2 = Label(scrollable_frame, text="", bg="black", font=("Arial", 8, "bold"), foreground=LOGO_GREEN)
gog_games_label_game_2.grid(column=1, row=13, padx=0)
purchase_gog_game_link_2 = Label(scrollable_frame, text="Purchase here", fg="black", bg="black", font=("Arial", 8, "underline"), cursor="hand2")
purchase_gog_game_link_2.grid(column=1, row=14, pady=0)

# game data right
gog_games_label_game_3_image = Label(scrollable_frame, bg="black", image=blank_photo_for_gog)
gog_games_label_game_3_image.grid(column=3, row=12, pady=5, padx=0)
gog_games_label_game_3 = Label(scrollable_frame, text="", bg="black", font=("Arial", 8, "bold"), foreground=LOGO_GREEN)
gog_games_label_game_3.grid(column=3, row=13, padx=0)
purchase_gog_game_link_3 = Label(scrollable_frame, text="Purchase here", fg="black", bg="black", font=("Arial", 8, "underline"), cursor="hand2")
purchase_gog_game_link_3.grid(column=3, row=14, pady=0)

# game data right 2
gog_games_label_game_4_image = Label(scrollable_frame, bg="black", image=blank_photo_for_gog)
gog_games_label_game_4_image.grid(column=4, row=12, pady=5, padx=(0, 0))
gog_games_label_game_4 = Label(scrollable_frame, text="", bg="black", font=("Arial", 8, "bold"), foreground=LOGO_GREEN)
gog_games_label_game_4.grid(column=4, row=13, padx=0)
purchase_gog_game_link_4 = Label(scrollable_frame, text="Purchase here", fg="black", bg="black", font=("Arial", 8, "underline"), cursor="hand2")
purchase_gog_game_link_4.grid(column=4, row=14, pady=0)

# XBOX GAME PASS PC version
xbox_game_pass_label = Label(scrollable_frame, text="", bg="black", font=("Arial", 15, "bold"), foreground=LOGO_GREEN)
xbox_game_pass_label.grid(column=2, row=15, pady=10)

# link for xbox subscription
purchase_xbox_subscript_link = Label(scrollable_frame, text="Purchase subscription", fg="black", bg="black", font=("Arial", 13, "underline"), cursor="hand2")
purchase_xbox_subscript_link.bind("<Button-1>", lambda e: open_link(url="https://www.xbox.com/en-GB/xbox-game-pass/pc-game-pass?xr=shellnav#pcgames"))
purchase_xbox_subscript_link.grid(column=2, row=16, pady=0)

# 1 xbox game
xbox_game_image_1 = Label(scrollable_frame, bg="black", image=blank_photo_for_steam)
xbox_game_image_1.grid(column=0, row=17, pady=5)
xbox_game_1_info = Label(scrollable_frame, text="", bg="black", font=("Arial", 8, "bold"), foreground=LOGO_GREEN)
xbox_game_1_info.grid(column=0, row=18, pady=5)

# 2 xbox game
xbox_game_image_2 = Label(scrollable_frame, bg="black", image=blank_photo_for_steam)
xbox_game_image_2.grid(column=1, row=17, pady=5)
xbox_game_2_info = Label(scrollable_frame, text="", bg="black", font=("Arial", 8, "bold"), foreground=LOGO_GREEN)
xbox_game_2_info.grid(column=1, row=18, pady=5)

# center xbox game
xbox_game_image_center = Label(scrollable_frame, bg="black", image=blank_photo_for_steam)
xbox_game_image_center.grid(column=2, row=17, pady=5)
xbox_game_center_info = Label(scrollable_frame, text="", bg="black", font=("Arial", 15, "bold"), foreground=LOGO_GREEN)
xbox_game_center_info.grid(column=2, row=18, pady=5)

# 3 xbox game
xbox_game_image_3 = Label(scrollable_frame, bg="black", image=blank_photo_for_steam)
xbox_game_image_3.grid(column=3, row=17, pady=5)
xbox_game_3_info = Label(scrollable_frame, text="", bg="black", font=("Arial", 8, "bold"), foreground=LOGO_GREEN)
xbox_game_3_info.grid(column=3, row=18, pady=5)

# 4 xbox game
xbox_game_image_4 = Label(scrollable_frame, bg="black", image=blank_photo_for_steam)
xbox_game_image_4.grid(column=4, row=17, pady=5)
xbox_game_4_info = Label(scrollable_frame, text="", bg="black", font=("Arial", 8, "bold"), foreground=LOGO_GREEN)
xbox_game_4_info.grid(column=4, row=18, pady=5)

window.update_idletasks()

window.mainloop()
