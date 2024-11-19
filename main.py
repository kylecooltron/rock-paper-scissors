import pyray
from source.keyboard import KeyboardService
from source.video import VideoService
from source import constants


class Player:

    def __init__(self, x, y, color, name) -> None:
        self.x = x
        self.y = y
        self.name = name
        self.color = color
        self.speed = 4

    def move(self, up, down, left, right):
        if up:
            self.y -= self.speed
        if down:
            self.y += self.speed
        if left:
            self.x -= self.speed
        if right:
            self.x += self.speed

    def draw(self, video_service: VideoService):
        height = 60
        half_height = round(height * 0.5)
        # head
        pyray.draw_circle(self.x, self.y, 15, self.color)
        # body
        pyray.draw_line(self.x, self.y + 15, self.x, self.y + height, self.color)
        # arms
        pyray.draw_line(
            self.x,
            self.y + half_height,
            self.x - 20,
            self.y + half_height - 10,
            self.color,
        )
        pyray.draw_line(
            self.x,
            self.y + half_height,
            self.x + 20,
            self.y + half_height - 10,
            self.color,
        )
        # legs
        pyray.draw_line(
            self.x, self.y + height, self.x - 20, self.y + height + 20, self.color
        )
        pyray.draw_line(
            self.x, self.y + height, self.x + 20, self.y + height + 20, self.color
        )
        # name
        video_service.draw_text(self.x, self.y - 50, self.name, self.color)


def main():

    # services
    keyboard_service = KeyboardService()
    video_service = VideoService()

    # players
    player_1 = Player(100, 100, pyray.RED, "Player 1")
    player_2 = Player(300, 100, pyray.BLUE, "Player 2")

    all_players = [player_1, player_2]

    # run game
    video_service.open_window()
    while video_service.is_window_open():
        video_service.clear_buffer()
        # player movement
        player_1.move(
            keyboard_service.is_key_down("w"),
            keyboard_service.is_key_down("s"),
            keyboard_service.is_key_down("a"),
            keyboard_service.is_key_down("d"),
        )
        player_2.move(
            keyboard_service.is_key_down("i"),
            keyboard_service.is_key_down("k"),
            keyboard_service.is_key_down("j"),
            keyboard_service.is_key_down("l"),
        )
        # draw all players
        for player in all_players:
            player.draw(video_service)

        video_service.flush_buffer()
    video_service.close_window()


if __name__ == "__main__":
    main()
