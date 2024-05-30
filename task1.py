import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.feature import corner_moravec
from skimage.io import imsave

def task1_edge_detection(image_path, output_filename):
    image = plt.imread(image_path)
    grayscale_image = rgb2gray(image)
    edges = corner_moravec(grayscale_image, window_size=1)
    
    # Convert the edges image to uint8 format
    edges_uint8 = (edges * 255).astype('uint8')
    
    imsave(output_filename, edges_uint8, cmap='gray')
    return f"Edge detection done successfully! Output saved as {output_filename}"