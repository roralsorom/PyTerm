import os, ctypes, threading, time, sys

__lock__ = threading.RLock()

class Concurrencies:
    """ Methods related to threads and concurrencies """
    
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
                args = [arg1, arg2, arg3],
                wait = True,
                max_concurent = 100
            )
        """
        
        active_count = threading.active_count()
        thread_list = []

        for _ in range(threads):
            while (threading.active_count() - active_count) >= max_concurent and wait == False:
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
    def print_s(*content: str):
        """Display text in the console while preventing jerks.

        Args:
            *content (str): Text to display
        """

        with __lock__:
            print(" ".join(map(str, content)))

class Console:
    """ Methods related to terminal and command prompt """
    
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

    @staticmethod
    def clear():
        """Clears the console on Linux and Windows.

        Args:
            None
        """

        os.system('cls||clear')

    @staticmethod
    def get_char():
        """Get first pressed keyboard char form user without pressing return
        
        Args:
            None
        """
        try:
            # for Windows
            import msvcrt
            return msvcrt.getch().decode('utf-8')

        except ImportError:
            # for linux (with termios & tty support)
            import tty, sys, termios

            fd = sys.stdin.fileno()
            oldSettings = termios.tcgetattr(fd)

            try:
                tty.setcbreak(fd)
                answer = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)

            return answer

    @staticmethod
    def read_stdin():
        """Read first line of STD-IN
        
        Args:
            None
        """
        for line in sys.stdin:
            return line.rstrip()
            break
    
    @staticmethod
    def read_all_stdin(remove_duplicate: bool = False):
        """Read all lines of STD-IN and return a list
        
        Args:
            remove_duplicate (bool): Remove all duplicated lines
        """

        lines = []
        
        for line in sys.stdin:
            lines.append(line)
        
        return lines if not remove_duplicate else list(set(lines))

    @staticmethod
    def forward_stdin(func: callable, args: list = None):
        """Execute function on each line from stdin
        
        Args:
            func(line: str, ..other_args) (callable): Function to execute, this function must take line at the first parameter
            args (int): Other args to add into the function.
        """
        
        for line in sys.stdin:
            line = line.strip()
            Concurrencies.start_threads(1, func, args.insert(0, line) if args != None else [line], False)