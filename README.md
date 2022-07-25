# 📂 Installation:

```
🛑 Lasted:
  pip install git+https://github.com/Its-Vichy/PyTerm.git

✅ Stable from pypi:
  pip install PyTerms==0.0.2
```

# 📝 Basic example:

```py
from PyTerm import Console, Concurrencies
import time

def printFunction(text: str):
    
    # print-secure with Rlock in multiple thread
    Concurrencies.print_s(text)
    time.sleep(1)

if __name__ == '__main__':
    # clear the console
    Console.clear()
    
    # set console title
    Console.set_title("Basic example | PyTerm Work on windows and linux !")
    
    # start 5 threads with 2 max concurent worker:
    Concurrencies.start_threads(5, printFunction, ["uwu"], False, 2)
```

```py
from PyTerm import Console, Concurrencies
import time

def printLine(line: str):
    Concurrencies.print_s(line)

if __name__ == '__main__':
    # This function will be executed on each line send into the STDIN.
    # Ex: cat file.txt | python3 script.py

    Console.forward_stdin(printLine)
```