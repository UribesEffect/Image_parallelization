# Image Processing with Master-Slave Architecture

This project demonstrates parallel processing of image tasks using a master-slave architecture. The master process distributes tasks to slave processes, which execute edge detection, corner detection, and facial recognition on images. The system dynamically adjusts the number of slave processes based on CPU utilization to optimize performance.

(NOTE: in the ProjectOperating.pdf you can have a complete document of all this project)

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
The master script will start the slave processes and distribute the image processing tasks among them. The number of initial slave processes is set to 2, but the system will dynamically adjust the number of slaves based on CPU utilization. If the CPU utilization exceeds 80%, additional slave processes will be started to handle the workload.
The master script will process all the image files found in the project directory. It will apply three types of tasks to each image:
- `task1.py`: Contains the implementation of edge detection task.
- `task2.py`: Contains the implementation of corner detection task.
- `task3.py`: Contains the implementation of facial recognition task.

The main codes:
- `master.py`: The master process script that coordinates task distribution and result collection.
- `slave.py`: The slave process script that executes the assigned tasks on images.

The processed images will be saved in the project directory with filenames indicating the original image and the applied task, e.g., image1_output_task1.jpg, image1_output_task2.jpg, image1_output_task3.jpg.
The master script will also log the execution time for each task and the total execution time for processing all the images.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
