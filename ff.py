import requests


class League:
    def __init__(self, league_id, year):
        self.league_id = league_id
        self.year = year
        self.endpoint = "http://games.espn.com/ffl/api/v2/teams"
        self.teams = []  # list of Team instances
        self._fetch_league()

    def _fetch_league(self):
        """retrieve JSON data"""
        params = {
            'leagueId': self.league_id,
            'seasonId': self.year
        }

        r = requests.get(self.endpoint, params=params)
        status = r.status_code
        data = r.json()

        if status != 200:
            raise Exception("Error: status code: %s" % status)
        else:
            self._fetch_teams(data)

    def _fetch_teams(self, data):
        """add Team instances to teams array"""
        teams = data['teams']  # array of objects

        for team in teams:
            self.teams.append(Team(team))


class Team:
    def __init__(self, team_data):
        self.wins = str(team_data['record']['overallWins'])
        self.losses = str(team_data['record']['overallLosses'])
        self.ties = team_data['record']['overallTies']
        self.record = (self.wins + "-" + self.losses if self.ties == 0
                       else self.wins + "-" + self.losses + "-" + str(self.ties))
        self.team_id = team_data['teamId']
        self.name = team_data['teamLocation'] + " " + team_data['teamNickname']
        self.standing = team_data['overallStanding']
        self.transactions = team_data['teamTransactions']['overallAcquisitionTotal']
        self.scores = []
        self.scores_against = []
        self._fetch_scores(team_data)

    def __repr__(self):
        return self.name

    def _fetch_scores(self, data):
        """collect scores from schedule"""
        matchups = data['scheduleItems']

        for matchup in matchups:
            home_score = matchup['matchups'][0]['homeTeamScores'][0]
            if not matchup['matchups'][0]['isBye']:
                away_score = matchup['matchups'][0]['awayTeamScores'][0]

                if matchup['matchups'][0]['awayTeam']['teamId'] == self.team_id:
                    self.scores.append(away_score)
                    self.scores_against.append(home_score)
                else:
                    self.scores_against.append(away_score)
                    self.scores.append(home_score)
            else:
                self.scores.append(home_score)  # if bye, always at home
