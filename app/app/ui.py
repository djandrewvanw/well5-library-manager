import os

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QListWidget,
    QFileDialog,
    QLabel,
    QComboBox,
QTableWidget,
QTableWidgetItem
)
)

from app.player import Player
from app.analyzer import analyze_track
from app.tags import save_cover
from app.dj_tags import (
    DJ_COLORS,
    EVENT_TYPES,
    ENERGY_LEVELS,
    MOODS
)
from app.database import connect, create_database

class MainWindow(QWidget):

    def __init__(self):

        super().__init__()
        create_database()
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
self.table = QTableWidget()

self.table.setColumnCount(4)

self.table.setHorizontalHeaderLabels(
    [
        "Track",
        "Rating",
        "Color",
        "Event"
    ]
)

left.addWidget(
    self.table
)
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
self.bpm_label = QLabel(
    "BPM: ---"
)

right.addWidget(
    self.bpm_label
)


analyze_button = QPushButton(
    "ANALYZE TRACK 🎧"
)

analyze_button.clicked.connect(
    self.analyze
)

right.addWidget(
    analyze_button
)
save_button = QPushButton(
    "SAVE TAGS 💾"
)
cover_button = QPushButton(
    "ADD COVER 💿"
)

cover_button.clicked.connect(
    self.add_cover
)

right.addWidget(
    cover_button
)
save_button.clicked.connect(
    self.save_tags
)

right.addWidget(
    save_button
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
row = self.table.rowCount()

self.table.insertRow(row)


self.table.setItem(
    row,
    0,
    QTableWidgetItem(file)
)


self.table.setItem(
    row,
    1,
    QTableWidgetItem("⭐")
)


self.table.setItem(
    row,
    2,
    QTableWidgetItem("")
)


self.table.setItem(
    row,
    3,
    QTableWidgetItem("")
)


    def play(self):

        row = self.list.currentRow()

        if row >= 0:

            self.player.play(
                self.files[row]
            )
    def save_tags(self):

        row = self.list.currentRow()

        if row < 0:
            return


        file = self.files[row]


        db = connect()

        cursor = db.cursor()


        cursor.execute(
            """
            INSERT INTO tracks
            (
                file,
                rating,
                color,
                event,
                energy,
                mood
            )

            VALUES
            (?, ?, ?, ?, ?, ?)
            """,

            (
                file,
                int(self.rating.currentText()),
                self.color.currentText(),
                self.event.currentText(),
                self.energy.currentText(),
                self.mood.currentText()
            )
        )


        db.commit()

        db.close()
    def add_cover(self):

        row = self.list.currentRow()

        if row < 0:
            return


        image, _ = QFileDialog.getOpenFileName(
            self,
            "Choose Cover",
            "",
            "Images (*.jpg *.png)"
        )


        if image:

            save_cover(
                self.files[row],
                image
            )
    def analyze(self):

        row = self.list.currentRow()


        if row < 0:
            return


        result = analyze_track(
            self.files[row]
        )


        self.bpm_label.setText(
            f"BPM: {result['bpm']}"
        )
