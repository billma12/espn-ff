import sys
from methods import *


def main():

    if len(sys.argv) == 2:
        print_top_points(int(sys.argv[1]))
    elif len(sys.argv) == 3:
        if int(sys.argv[2]) <= 25:
            print_top_points(int(sys.argv[1]), top=int(sys.argv[2]))
        else:
            print("only displays up to top 25")
    elif len(sys.argv) == 4:
        if sys.argv[2] == 'stats':
            print_league_stats(int(sys.argv[1]), int(sys.argv[3]))
        else:
            print_top_points(int(sys.argv[1]), top=int(sys.argv[2]), start=int(sys.argv[3]))
    else:
        print("Usage: python main.py [leagueID] [top] [startYear]")


if __name__ == '__main__':
    main()
