from mutagen.id3 import ID3, POPM, APIC


def save_rating(file, rating):

    audio = ID3(file)

    audio.add(
        POPM(
            email="Well5Library",
            rating=rating * 51,
            count=0
        )
    )

    audio.save()



def save_cover(file, image):

    audio = ID3(file)

    with open(image, "rb") as img:

        audio.add(
            APIC(
                encoding=3,
                mime="image/jpeg",
                type=3,
                desc="Cover",
                data=img.read()
            )
        )

    audio.save()
