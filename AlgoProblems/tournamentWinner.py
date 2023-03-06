def tournamentWinner(competitions, results):
    currWinner = ""
    teamPoints = {}

    for homeTeam, awayTeam in competitions:
        if homeTeam not in teamPoints:
            teamPoints[homeTeam] = 0
        else:
            teamPoints[homeTeam] += 3
        if awayTeam not in teamPoints:
            teamPoints[awayTeam] = 0
        else:
            teamPoints[awayTeam] += 3
    print(teamPoints)


competitions = [
    ["HTML", 'C#'],
    ["C#", 'Python'],
    ["Python", "HTML"]
]
results = [0, 0, 1]

print(tournamentWinner(competitions, results))