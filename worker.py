import queue
import threading
import time

class ModbusWorker:
    def __init__(self):
        self.tasks_queue = queue.Queue()
        self.read_tasks = []
        self.write_tasks = []
        self.stopwatch = time.perf_counter()

    def add_read_task(self, task):
        self.read_tasks.append(task)

    def add_write_task(self, task):
        self.write_tasks.append(task)

    def on_before_process_image(self):
        self.stopwatch = time.perf_counter()
        next_read_tasks = self.get_next_read_tasks()
        next_write_tasks = self.get_next_write_tasks()
        for task in next_read_tasks + next_write_tasks:
            self.tasks_queue.put(task)

    def get_next_read_tasks(self):
        # Logic to collect next set of read tasks
        return []

    def get_next_write_tasks(self):
        # Logic to collect next set of write tasks
        return []

    def on_execute_write(self):
        while not self.tasks_queue.empty():
            task = self.tasks_queue.get()
            task.execute()

worker = ModbusWorker()
worker.on_before_process_image()
worker.on_execute_write()
