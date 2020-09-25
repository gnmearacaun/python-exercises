def tracklist(**tracks):
    for band, info in tracks.items():
        print(band)
        for album, track in info.items():
            print("ALBUM: {} TRACK: {}".format(album, track))
