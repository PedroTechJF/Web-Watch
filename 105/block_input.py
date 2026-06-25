from pynput import keyboard, mouse

keyboard_listener = None
mouse_listener = None

def dummy_callback(*args, **kwargs):
    pass

def block_inputs(stop=False):
    global keyboard_listener, mouse_listener
    
    if stop:
        if keyboard_listener:
            keyboard_listener.stop()
        if mouse_listener:
            mouse_listener.stop()
        return False
    
    keyboard_listener = keyboard.Listener(on_press=dummy_callback, suppress=True)
    mouse_listener = mouse.Listener(
        on_move=dummy_callback, 
        on_click=dummy_callback, 
        on_scroll=dummy_callback, 
        suppress=True
    )
    
    keyboard_listener.start()
    mouse_listener.start()
        