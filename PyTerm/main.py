import os, ctypes, threading, time

__lock__ = threading.RLock()


class PyTerm:
    """Access to all PyTerm methods."""

    @staticmethod
    def start_threads(threads: int, func: callable, args: list, wait: bool= False, max_concurent: int=100):
        """Start a certain amount of threads on a specific function
        
        Args:
            threads (int): Amount of threads to run
            func (callable): Function to thread
            args (list): Arguments to pass to the function
            wait (bool): If true, waits for threads to complete.
            max_concurent (int): Maximum number of threads to execute simultaneously. WARNING: Work only if wait is disabled.
        
        Example:
            start_threads(
                threads = 3,
                func = myfunction,
                args = [arg1, arg2, arg3]
            )
        """
        
        activate = threading.active_count()
        thread_list = []

        for _ in range(threads):
            while (threading.active_count() - activate) >= max_concurent and wait == False:
                time.sleep(1)

            thread = threading.Thread(target=func, args=args)
            thread_list.append(thread)

            if wait == False:
                thread.start()
        
        if wait:
            for thread in thread_list:
                thread.start()

            for thread in thread_list:
                thread.join()

    @staticmethod
    def set_title(title: str):
        """Changing the console title on Linux and Windows.

        Args:
            title (str): New title of the console
        """

        if not isinstance(title, str):
            raise ValueError('title must be a string')

        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW(title)
        else:
            print(f'\33]0;{title}\a', end='', flush=True)
    setTitle = set_title

    @staticmethod
    def prints(*content: str):
        """Display text in the console while preventing jerks.

        Args:
            *content (str): Text to display
        """

        with __lock__:
            print(" ".join(map(str, content)))

    @staticmethod
    def clear():
        """Clears the console on Linux and Windows.

        Args:
            None
        """

        os.system('cls||clear')
