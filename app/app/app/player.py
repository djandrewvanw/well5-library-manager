import vlc


class Player:

    def __init__(self):

        self.player = vlc.MediaPlayer()


    def play(self, file):

        media = vlc.Media(file)

        self.player.set_media(
            media
        )

        self.player.play()


    def pause(self):

        self.player.pause()


    def stop(self):

        self.player.stop()
