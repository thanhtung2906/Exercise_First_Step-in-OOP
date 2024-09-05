class SteamUser:
    def __init__(self,username,games,played_hours):
        self.username = username
        self.games = games
        self.played_hours = played_hours
        played_hours == 0
    def play(self,game,hours):
        if game in self.games:
            self.played_hours = self.played_hours + hours
            print(self.username + ' is playing ' + game)
        else:
            print(game + ' is not in library')
    def buy_game(self,game):
        if game in self.games:
            print(game +' is already in your library')
        else:
            print(self.username +' bought',game)

    def status(self):
        print(self.username + " has " + str(len(self.games)) +" games. Total played time: " +str(self.played_hours) )

user = SteamUser("Tung",["CS:GO","Black Myth: Wukong","Elden Ring"],0)
user.play("CS:GO",10)
user.play("Nier",3)
user.buy_game("Elden Ring")
user.buy_game("Little Nightmare")
user.status()


        
        
        
        
        