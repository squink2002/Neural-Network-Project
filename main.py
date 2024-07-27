import utils
from data_sets.images.image import image
from data_sets.data_sets import mnist_dataset

MNIST_TRAINING_DATA = "data/mnist/mnist_train.csv"

def main():

    # Read in the MNIST training data
    dataset = mnist_dataset(utils.read_mnist_csv(MNIST_TRAINING_DATA))

    # Print out for sanity (feel free to comment out)
    dataset.print_dataset_image_list()
    
    return;

if __name__ == '__main__':
    main()
    print("hello world")
