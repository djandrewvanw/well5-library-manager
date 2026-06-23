import librosa


def analyze_track(file):

    try:

        y, sr = librosa.load(
            file,
            duration=60
        )


        tempo, beats = librosa.beat.beat_track(
            y=y,
            sr=sr
        )


        bpm = round(
            float(tempo)
        )


        return {
            "bpm": bpm,
            "key": "Unknown"
        }


    except Exception:

        return {
            "bpm": 0,
            "key": "Unknown"
        }
