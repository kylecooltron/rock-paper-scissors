import pyray


class KeyboardService:
    """Detects player input.

    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {
            # player 1
            "w": pyray.KEY_W,
            "a": pyray.KEY_A,
            "s": pyray.KEY_S,
            "d": pyray.KEY_D,
            # player 2
            "i": pyray.KEY_I,
            "j": pyray.KEY_J,
            "k": pyray.KEY_K,
            "l": pyray.KEY_L,
        }

    def is_key_up(self, key):
        """Checks if the given key is currently up.

        Args:
            key (string): The given key
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.

        Args:
            key (string): The given key
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)
