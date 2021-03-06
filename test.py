import threading
import progress_bar_animation


def some_task():
    """
        function to mock a task that takes time , till that time our loader will show
    """
    for _ in range(1 * 100000000):
        pass


task_thread = threading.Thread(target=some_task)


progress_thread = threading.Thread(target=progress_bar_animation.show_progress)

task_thread.start()
progress_thread.start()
task_thread.join()

progress_bar_animation.done = True
