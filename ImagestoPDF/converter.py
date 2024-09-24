import os
from PIL import Image

def main():

    output_dir = "./PDFs"
    source_dir = "./Images"

    images = []

    for file in sorted(os.listdir(source_dir)):
        if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
            image = Image.open(os.path.join(source_dir, file))
            image_converted = image.convert('RGB')
            images.append(image_converted)
    if len(images) == 0:
        return
    images[0].save("./PDFs/merged.pdf", save_all=True, append_images=images)


if __name__ == "__main__":
    main()