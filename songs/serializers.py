from rest_framework import serializers
from .models import Artist,Lyric,Song,Album


class AlbumSerialezer(serialazers.Modelserializer):
    class Meta:
        model = Album
        fields = ['artist','name','release','cover']


class ArtistSerialezer(serialazers.Modelserializer):
    class Meta:
        model = Artist
        fields = ['first_name','last_name','artist_pic','num_stars']

class SongSerialezer(serialazers.Modelserializer):
    class Meta:
        model = Song
        fields = ['album','artist','lyric','name','released']