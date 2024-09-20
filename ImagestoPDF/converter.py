import os
from PIL import Image
from fontTools.subset import save_font


def main():
    output_dir = "./PDFs"
    source_dir = "./Images"

    images = []

    for file in sorted(os.listdir(source_dir)):
        if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
            image = Image.open(os.path.join(source_dir, file))
            image_converted = image.convert('RGB')
            #image_converted.save(os.path.join(output_dir, '{0}.pdf'.format(file.split('.')[-2])))
            images.append(image_converted)
    images[0].save("./PDFs/merged.pdf", save_all=True, append_images=images)


if __name__ == "__main__":
    main()