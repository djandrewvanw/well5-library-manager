import os

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QListWidget,
    QFileDialog,
    QLabel,
    QComboBox
)

from app.player import Player
from app.dj_tags import (
    DJ_COLORS,
    EVENT_TYPES,
    ENERGY_LEVELS,
    MOODS
)


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Well5 Library Manager"
        )

        self.resize(
            1000,
            600
        )


        self.player = Player()

        self.files = []


        main = QHBoxLayout()


        # LEWA STRONA - MUZYKA

        left = QVBoxLayout()


        self.list = QListWidget()

        left.addWidget(
            self.list
        )


        import_button = QPushButton(
            "Import MP3 Folder"
        )

        import_button.clicked.connect(
            self.load_folder
        )

        left.addWidget(
            import_button
        )


        play_button = QPushButton(
            "PLAY"
        )

        play_button.clicked.connect(
            self.play
        )

        left.addWidget(
            play_button
        )


        # PRAWA STRONA - TAGI

        right = QVBoxLayout()


        right.addWidget(
            QLabel("Rating ⭐")
        )


        self.rating = QComboBox()

        self.rating.addItems(
            [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5"
            ]
        )

        right.addWidget(
            self.rating
        )


        right.addWidget(
            QLabel("Color 🎨")
        )


        self.color = QComboBox()

        self.color.addItems(
            DJ_COLORS
        )

        right.addWidget(
            self.color
        )


        right.addWidget(
            QLabel("Event Type 🏷")
        )


        self.event = QComboBox()

        self.event.addItems(
            EVENT_TYPES
        )

        right.addWidget(
            self.event
        )


        right.addWidget(
            QLabel("Energy ⚡")
        )


        self.energy = QComboBox()

        self.energy.addItems(
            ENERGY_LEVELS
        )

        right.addWidget(
            self.energy
        )


        right.addWidget(
            QLabel("Mood 😎")
        )


        self.mood = QComboBox()

        self.mood.addItems(
            MOODS
        )

        right.addWidget(
            self.mood
        )


        main.addLayout(
            left
        )

        main.addLayout(
            right
        )


        self.setLayout(
            main
        )



    def load_folder(self):

        folder = QFileDialog.getExistingDirectory()


        for file in os.listdir(folder):

            if file.lower().endswith(".mp3"):

                path = os.path.join(
                    folder,
                    file
                )

                self.files.append(
                    path
                )

                self.list.addItem(
                    file
                )



    def play(self):

        row = self.list.currentRow()

        if row >= 0:

            self.player.play(
                self.files[row]
            )
