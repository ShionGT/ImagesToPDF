import tkinter
import tkinter as tk
import os
from PIL import Image

class GUI:

    def __init__(self):

        # directories
        self.output_dir = "./PDFs"
        self.source_dir = "./Images"

        # buttons
        self.convert_button = None
        self.has_converted = False
        self.open_images_file_button = None
        self.open_pdf_file_button = None

        self.root = None


    def convert_button_pressed(self):

        # Check if the PDF has already converted
        if self.has_converted:
            return

        #Convert
        print("Convert image to PDF initiated...")

        images = []

        for file in sorted(os.listdir(self.source_dir)):
            if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
                image = Image.open(os.path.join(self.source_dir, file))
                image_converted = image.convert('RGB')
                # image_converted.save(os.path.join(output_dir, '{0}.pdf'.format(file.split('.')[-2])))
                images.append(image_converted)
        if len(images) == 0:
            return
        self.has_converted = True
        images[0].save(self.output_dir + "/merged.pdf", save_all=True, append_images=images)

        # Open folder
        if os.path.exists(self.output_dir):
            #os.startfile(self.output_dir)  # For Windows
            os.system(f"open '{self.output_dir}'")  # For macOS


    def open_image_file_pressed(self):
        # Open images folder
        if os.path.exists(self.source_dir):
            # os.startfile(self.source_dir)  # For Windows
            os.system(f"open '{self.source_dir}'")  # For macOS


    def open_pdf_file_pressed(self):
        # Open PDF folder
        if os.path.exists(self.output_dir):
            # os.startfile(self.source_dir)  # For Windows
            os.system(f"open '{self.output_dir}'")


    def main(self):

        self.root = tk.Tk()

        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set desired proportions
        width_proportion = 0.2
        height_proportion = 0.3

        # Calculate new window dimensions
        win_width = int(screen_width * width_proportion)
        win_height = int(screen_height * height_proportion)

        # Resize the window
        self.root.geometry(f"{win_width}x{win_height}")
        self.root.resizable(True, True)

        # Title window frame
        self.root.title("PDF Convert")

        # Button Size
        button_height = int(win_height * 0.008)
        button_width = int(win_width * 0.05)
        print(button_width, button_height)
        print(win_width, win_height)

        tk.Label(height=button_height).pack(side=tk.TOP)

        # Open images file button
        self.open_images_file_button = tk.Button(
            self.root,
            text="Add Images",
            width=button_width,
            height=button_height,
            foreground="black",
            background="white",
            command=self.open_image_file_pressed,
        )
        self.open_images_file_button.pack()

        # Open PDF file button
        self.open_pdf_file_button = tk.Button(
            self.root,
            text="See PDF",
            width=button_width,
            height=button_height,
            foreground="black",
            background="white",
            command=self.open_pdf_file_pressed,
        )
        self.open_pdf_file_button.pack()

        tk.Label(height=button_height).pack(side=tk.BOTTOM)

        # Convert button
        self.convert_button = tk.Button(
            self.root,
            text="Convert",
            width=button_width,
            height=button_height,
            foreground="black",
            background="white",
            command=self.convert_button_pressed,
        )
        self.convert_button.pack(side=tk.BOTTOM)

        # Display everything
        self.root.mainloop()


if __name__ == "__main__":
    GUI().main()