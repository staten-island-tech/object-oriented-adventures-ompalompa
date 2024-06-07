# Monopoly 

https://www.hasbro.com/common/instruct/00009.pdf

https://www.geeksforgeeks.org/create-a-simple-two-player-game-using-turtle-in-python/

get Path Intellisense
not a ad

https://www.geeksforgeeks.org/how-to-play-sounds-in-python-with-tkinter/?ref=ml_lbp



## Tkinter

### Board
- 

### Player

```
343
Top Hat
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\__init__.py", line 1967, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "c:\Users\jonathan.ou23\Documents\GitHub\object-oriented-adventures-ompalompa\data\tkinterboard.py", line 68, in <lambda>
    self.canvas.tag_bind(text_id, "<Button-1>", lambda event: command())
                                                              ^^^^^^^^^
  File "c:\Users\jonathan.ou23\Documents\GitHub\object-oriented-adventures-ompalompa\data\tkinterboard.py", line 151, in submitted
    subprocess.Popen(["python3", "data/tkinterplayer.py"])
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified
alloc: invalid block: 000001C5328038C0: e0 31
```