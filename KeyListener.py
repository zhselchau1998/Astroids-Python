from pynput import keyboard

class KeyListener:
    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.buffer = []

        self.listener.start()
        
    def getKeys(self)->list:
        return self.buffer

    def on_press(self, key):
        try:
            k = key.char
        except:
            k = key.name
        if k in ['w','W','up'] and 'w' not in self.buffer:     # Up keys
            self.buffer.append('w')
        if k in ['a','A','left'] and 'a' not in self.buffer:   # Left keys
            self.buffer.append('a')
        if k in ['s','S','down'] and 's' not in self.buffer:   # Down keys
            self.buffer.append('s')
        if k in ['d','D','right'] and 'd' not in self.buffer:  # Right keys
            self.buffer.append('d')
        if k == 'space' and 'space' not in self.buffer:        # Shoot keys
            self.buffer.append('space')
    
    def on_release(self, key):
        try:
            k = key.char
        except:
            k = key.name
        if k in ['w','W','up'] and 'w' in self.buffer:     # Up keys
            self.buffer.remove('w')
        if k in ['a','A','left'] and 'a' in self.buffer:   # Left keys
            self.buffer.remove('a')
        if k in ['s','S','down'] and 's' in self.buffer:   # Down keys
            self.buffer.remove('s')
        if k in ['d','D','right'] and 'd' in self.buffer:  # Right keys
            self.buffer.remove('d')
        if k == 'space' and 'space' in self.buffer:        # Shoot keys
            self.buffer.remove('space')