from mutagen.id3 import ID3, POPM, APIC, TXXX


def get_id3(file):

    try:
        return ID3(file)

    except:

        return ID3()



def save_rating(file, rating):

    audio = get_id3(file)

    audio.add(
        POPM(
            email="Well5Library",
            rating=rating * 51,
            count=0
        )
    )

    audio.save()



def save_dj_tags(
    file,
    color,
    event,
    energy,
    mood
):

    audio = get_id3(file)


    audio.add(
        TXXX(
            description="DJ Color",
            text=color
        )
    )


    audio.add(
        TXXX(
            description="Event Type",
            text=event
        )
    )


    audio.add(
        TXXX(
            description="Energy",
            text=energy
        )
    )


    audio.add(
        TXXX(
            description="Mood",
            text=mood
        )
    )


    audio.save()



def save_cover(file, image):

    audio = get_id3(file)


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
