import time

class ModbusWorker:
    def __init__(self):
        #initialize the worker
        self.read_tasks = []
    def add_read_task(self, task):
        self.read_tasks.append(task)

    def get_next_read_tasks(self):
        # Logic to collect next set of read tasks
        self.read_tasks.sort(key=lambda x: x.priority)
        next_tasks = []
        for task in self.read_tasks:
            if (time.perf_counter() - self.stopwatch) + task.get_execute_duration() < cycle_time:
                next_tasks.append(task)
            else:
                break
        self.read_tasks = [task for task in self.read_tasks if task not in next_tasks]
        return next_tasks

# Add the task to the worker
worker = ModbusWorker()
worker.add_read_task(task1)
worker.add_read_task(task2)

# Collect the next set of tasks and execute them
worker.on_before_process_image()
worker.on_execute_write()
