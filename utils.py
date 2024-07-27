import csv
from data_sets.images.image import image

"""
Input:
    str : filename
Output:
    Image[] : all_images
"""
def read_mnist_csv(file_name):
    all_images = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            label = row[0]
            data = row[1:]
            im = image(label, data)
            all_images.append(im)
    return all_images
