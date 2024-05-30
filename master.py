import multiprocessing
import socket
import pickle
import subprocess
import time
import logging
import cv2
import os
import psutil

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_task_to_slave(task, slave_port):
    start_time = time.time()
    try:
        # Connect to the slave
        slave_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        slave_socket.connect(('localhost', slave_port))

        # Send the task to the slave
        task_data = pickle.dumps(task)
        slave_socket.send(task_data)

        # Receive the result from the slave
        result_data = slave_socket.recv(4096)
        result = pickle.loads(result_data)

        # Close the connection
        slave_socket.close()

        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Task sent to slave on port {slave_port} - Execution time: {execution_time:.4f} seconds")

        return result
    except Exception as e:
        logging.error(f"Error sending task to slave on port {slave_port}: {str(e)}")
        return None

def start_slave(port):
    subprocess.Popen(['python', 'slave.py', str(port)])

def get_cpu_utilization():
    return psutil.cpu_percent()

def main():
    start_time = time.time()

    # Get the current directory (where the master script is located)
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Get the list of image files in the current directory
    image_files = [file for file in os.listdir(current_directory) if file.endswith('.jpg')]

    # Define the tasks to be processed
    tasks = []
    for image_file in image_files:
        image_path = os.path.join(current_directory, image_file)
        tasks.extend([
            {'task_type': 'task1', 'image_path': image_path},
            {'task_type': 'task2', 'image_path': image_path},
            {'task_type': 'task3', 'image_path': image_path, 'modelo_cara_path': cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'},
        ])

    # Create a pool of worker processes
    pool = multiprocessing.Pool()

    # Start the initial slaves
    num_initial_slaves = 2
    slave_ports = [9000 + i for i in range(num_initial_slaves)]
    for port in slave_ports:
        pool.apply_async(start_slave, args=(port,))

    # Wait for the initial slaves to start
    time.sleep(1)

    # Send tasks to the slaves and collect the results
    results = []
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(current_directory, image_file)
        for j in range(3):
            task_type = f"task{j+1}"
            output_filename = f"{image_file}_output_{task_type}.jpg"
            task = {
                'task_type': task_type,
                'image_path': image_path,
                'output_filename': output_filename
            }
            if task_type == 'task3':
                task['modelo_cara_path'] = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            
            slave_port = slave_ports[i % len(slave_ports)]
            result = pool.apply_async(send_task_to_slave, args=(task, slave_port))
            results.append(result)

        # Check CPU utilization and start additional slaves if needed
        cpu_utilization = get_cpu_utilization()
        if cpu_utilization > 80:
            new_slave_port = max(slave_ports) + 1
            slave_ports.append(new_slave_port)
            pool.apply_async(start_slave, args=(new_slave_port,))
            logging.info(f"Started new slave on port {new_slave_port} due to high CPU utilization")
    # Wait for all tasks to complete and retrieve the results
    pool.close()
    pool.join()

    # Print the results and execution time for each image
    for i, image_file in enumerate(image_files):
        logging.info(f"Results for {image_file}:")
        for j in range(3):
            result_index = i * 3 + j
            logging.info(f"  Result from task {j + 1}: {results[result_index].get()}")

    end_time = time.time()
    total_execution_time = end_time - start_time
    logging.info(f"Total execution time: {total_execution_time:.4f} seconds")

if __name__ == '__main__':
    main()
