import pyray
from source import constants


class VideoService:
    """Outputs the game state to the screen"""

    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering."""
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)

    def flush_buffer(self):
        """Copies the buffer contents to the screen."""
        pyray.end_drawing()

    def draw_text(self, x, y, text, color):
        """Draws the given actor's text on the screen.

        Args:
            actor (Actor): The actor to draw.
        """

        pyray.draw_text(text, x, y, 16, color)

    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
        pyray.set_target_fps(constants.FRAME_RATE)
