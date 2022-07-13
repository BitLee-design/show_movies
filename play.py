import webbrowser

class Movie():
    def __init__(self, play_title, play_storyline, trailor_youtube):
        self.title = play_title
        self.storyline = play_storyline
        self.trailor_youtube_url = trailor_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailor_youtube_url)
        

	
	
