from pynput.keyboard import Key, KeyCode, Listener as KeyListener
from pynput.mouse import Button, Controller, Listener as MouseListener


class KeysListener:
    combinations = []

    def __init__(self):
        self.hold_list = []
        self.Key = Key
        self.KeyCode = KeyCode

    def add_combination(self, combination: list, callback, **kwargs):
        self.combinations.append({
            'combination': combination,
            'callback': callback,
            'kwargs': kwargs,
        })

    def add_to_hold_list(self, key):
        self.hold_list.append(key)

    def on_release(self, key):
        print(key, end=', ')

        for comb in self.combinations:
            combination: list = comb['combination']
            callback = comb['callback']
            kwargs = comb['kwargs']

            if len(combination) > 1:
                if set(self.hold_list) == set(combination):
                    callback(**kwargs)
            elif len(combination) == 1:
                if key == combination[0]:
                    callback(**kwargs)

        cleared_hold_list = list(dict.fromkeys(self.hold_list))
        if key in cleared_hold_list:
            cleared_hold_list.remove(key)
        self.hold_list = cleared_hold_list

        if key == Key.esc:
            return False

    def listen(self):
        with KeyListener(on_press=self.add_to_hold_list, on_release=self.on_release) as listener:
            listener.join()

        print('KeyListener exited')
