"""
If you want to test this file directly, add import

from images.image import image                                

Comment out:
from data_sets.images.image import image

Uncomment if __name__ section 
"""
from data_sets.images.image import image
class mnist_dataset:
    """
    Input:
        Image[] : images
    """
    def __init__(self, images):
        self.image_list = images
        self.image_dict = {}

    def print_dataset_image_list(self):
        for im in self.image_list:
            im.print_image()

# if __name__ == '__main__':
#     im = image(0, [1, 2, 3])
#     print(im.data)
