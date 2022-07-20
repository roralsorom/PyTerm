import os, threading

__lock__ = threading.RLock()

class PyTerm:
    """Access to all PyTerm methods."""

    @staticmethod
    def set_title(title: str):
        """Changing the console title on Linux and Windows.

        Args:
            title (str): New title of the console
        """

        if title.isdigit():
            raise ValueError('title must be a string')
        
        if os.name == 'nt':
            os.system(f'title {title}'.replace('|', '^|'))
        else:
            print(f'\33]0;{title}\a', end='', flush=True)

    @staticmethod
    def prints(content: str):
        """Display text in the console while preventing jerks.

        Args:
            content (str): Text to display
        """

        with  __lock__:
            print(content)
    
    @staticmethod
    def clear():
        """Clears the console on Linux and Windows.

        Args:
            None
        """

        os.system('cls' if os.name == 'nt' else 'clear')