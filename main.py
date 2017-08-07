from tabulate import tabulate
from statistics import mean
from ff import League


def print_table(data, headers):
    """prints out data using tabulate"""

    return print(tabulate(data, headers=headers, tablefmt='simple'))


def print_league_stats(leagueid, year):
    """prints out league stats"""
    data = get_league_stats(leagueid, year)
    headers = ['name', 'standing', 'record', 'scores', 'against']

    return print_table(data, headers)


def print_top_points(leagueid, start, end, top=10):
    """prints out top points scored"""

    data = get_top_points(leagueid, start, end, top)
    headers = ['score', 'year', 'week', 'name']

    return print_table(data, headers)


def get_league_stats(leagueid, year):
    """returns list of stats for each team"""
    league = League(leagueid, year)
    stats = []

    for team in league.teams:
        stats.append([team.name, team.standing, team.record, mean(team.scores),
                      mean(team.scores_against)])

    return stats


def get_top_points(leagueid, start, end, top=10):
    """returns list of top scores, default is 10"""

    top_scores = []
    myleague = {}

    for year in range(start, end+1):
        myleague[year] = League(leagueid, year)
        for team in myleague[year].teams:
            week = 1
            for score in team.scores:
                top_scores.append((score, year, week, team.name))
                week += 1

    return sorted(top_scores, reverse=True)[:top]


def main():
    # leagueid = 476859
    leagueid = 1670403
    start = 2013
    end = 2016

    #print_league_stats(leagueid, 2016)
    print_top_points(leagueid, 2014, end)


if __name__ == '__main__':
    main()
