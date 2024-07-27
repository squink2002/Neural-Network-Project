def get_2d_data(data):
    # TODO
    return [[]]

MNIST_IMAGE_WIDTH = 28
MNIST_IMAGE_HEIGHT = 28

class image:
    """
    Input:
        int : label
        int[] : data
    """
    
    image_width = MNIST_IMAGE_WIDTH
    image_height = MNIST_IMAGE_HEIGHT

    def __init__(self, label, data):
        self.label = label
        self.data = data
        self.data2d = get_2d_data(data)

    def print_image(self):
        print("label: ", self.label, "\ndata: ", self.data)

if __name__ == '__main__':
    im = image(0, [1, 2, 3, 4])

    print(im.data)
