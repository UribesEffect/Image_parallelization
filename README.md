# Image Processing with Master-Slave Architecture

This project demonstrates parallel processing of image tasks using a master-slave architecture. The master process distributes tasks to slave processes, which execute edge detection, corner detection, and facial recognition on images. The system dynamically adjusts the number of slave processes based on CPU utilization to optimize performance.

## Features

- Parallel processing of image tasks using Python's multiprocessing and socket communication
- Master process coordinates task distribution and result collection
- Slave processes execute image processing tasks (edge detection, corner detection, facial recognition)
- Dynamic adjustment of slave processes based on CPU utilization
- Efficient processing of a large number of images

## Requirements

- Python 3.x
- OpenCV (cv2)
- psutil

## Usage

1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/image-processing-master-slave.git


2. Install the required dependencies:
   ```shell
   pip install opencv-python psutil

3. Place the image files you want to process in the project directory.

4. Run the master script:
   ```shell
    python master.py

5. The processed images will be saved in the project directory with the corresponding task names.

## Project Structure

- `master.py`: The master process script that coordinates task distribution and result collection.
- `slave.py`: The slave process script that executes the assigned tasks on images.
- `task1.py`: Contains the implementation of edge detection task.
- `task2.py`: Contains the implementation of corner detection task.
- `task3.py`: Contains the implementation of facial recognition task.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
