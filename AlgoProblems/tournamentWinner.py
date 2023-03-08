homeTeamWon = 1
def tournamentWinner(competitions, results):
    currWinner = ""
    teamPoints = {currWinner: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == homeTeamWon else awayTeam

        updateScores(winningTeam, 3, teamPoints)

        if teamPoints[winningTeam] > teamPoints[currWinner]:
            currWinner = winningTeam
    
    return currWinner

def updateScores(team, points, teamPoints):
    if team not in teamPoints:
        teamPoints[team] = 0
    
    teamPoints[team] += points


competitions = [
    ["HTML", 'C#'],
    ["C#", 'Python'],
    ["Python", "HTML"]
]
results = [0, 0, 1]

print(tournamentWinner(competitions, results))