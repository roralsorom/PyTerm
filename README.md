# 📂 Installation:

```
🛑 Lasted:
  pip install git+https://github.com/Its-Vichy/PyTerm.git

✅ Stable from pypi:
  pip install PyTerms==0.0.2
```

# 📝 Basic example:

```py
from PyTerm import PyTerm
import time

def printFunction(text: str):
    
    # print-secure with Rlock in multiple thread
    PyTerm.prints(text)
    time.sleep(1)

if __name__ == '__main__':
    
    # clear the console
    PyTerm.clear()
    
    # set console title
    PyTerm.set_title("Basic example | PyTerm Work on windows and linux !")

    # start 5 threads with 2 max concurent worker:
    PyTerm.start_threads(5, printFunction, ["uwu"], False, 2)
```
