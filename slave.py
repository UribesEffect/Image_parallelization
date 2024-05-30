import socket
import subprocess
import pickle
import sys
import logging
import time
import cv2
from task1 import task1_edge_detection
from task2 import task2_corner_detection
from task3 import task3_facial_recognition


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_task(task):
    try:
        task_type = task['task_type']
        image_path = task['image_path']
        output_filename = task['output_filename']

        if task_type == 'task1':
            result = task1_edge_detection(image_path, output_filename)
        elif task_type == 'task2':
            result = task2_corner_detection(image_path, output_filename)
        elif task_type == 'task3':
            modelo_cara_path = task['modelo_cara_path']
            result = task3_facial_recognition(modelo_cara_path, image_path, output_filename)
        else:
            raise ValueError(f"Unknown task type: {task_type}")

        return result
    except Exception as e:
        logging.error(f"Error processing task: {str(e)}")
        return None


def main(port):
    # Create a socket and listen for incoming connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)

    logging.info(f"Slave started on port {port}")

    while True:
        try:
            # Accept a connection from the master
            master_socket, address = server_socket.accept()

            # Receive the task from the master
            task_data = master_socket.recv(4096)
            task = pickle.loads(task_data)

            logging.info(f"Received task: {task}")

            # Process the task
            result = process_task(task)

            # Send the result back to the master
            result_data = pickle.dumps(result)
            master_socket.send(result_data)

            # Close the connection
            master_socket.close()
        except Exception as e:
            logging.error(f"Error in slave communication: {str(e)}")

if __name__ == '__main__':
    port = int(sys.argv[1])
    main(port)
