import os

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QListWidget,
    QFileDialog
)

from app.player import Player


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Well5 Library Manager"
        )

        self.resize(
            900,
            600
        )

        self.player = Player()

        self.files = []

        layout = QVBoxLayout()


        self.list = QListWidget()

        layout.addWidget(
            self.list
        )


        button = QPushButton(
            "Import MP3 Folder"
        )

        button.clicked.connect(
            self.load_folder
        )

        layout.addWidget(
            button
        )


        play = QPushButton(
            "PLAY"
        )

        play.clicked.connect(
            self.play
        )

        layout.addWidget(
            play
        )


        self.setLayout(
            layout
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
