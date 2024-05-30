import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.feature import corner_harris,corner_moravec
from skimage import feature
from skimage.io import imsave

def task2_corner_detection(image_path, output_filename):
    image = plt.imread(image_path)
    grayscale_image = rgb2gray(image)
    edges = corner_moravec(grayscale_image, window_size=1)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(image, cmap='gray')
    
    threshold = 0.7
    corner_peaks = edges > threshold
    corner_peaks_y, corner_peaks_x = corner_peaks.nonzero()

    fig, ax = plt.subplots()
    ax.imshow(image, cmap='gray')
    ax.scatter(corner_peaks_x, corner_peaks_y, c='r', marker='x')
    ax.set_title('Detección de Esquinas')
    ax.axis('off')
    fig.savefig(output_filename)
    plt.close(fig)

    return f"Corner detection done successfully! Output saved as {output_filename}"
