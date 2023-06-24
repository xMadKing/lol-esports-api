import eventsAPI
import leaguesAPI
import matchAPI
import teamsAPI
import time


def main():
    print("Api working")

    start_time = time.time()

    print(leaguesAPI.getStandingsByStage(leaguesAPI.getTourmanentBySlug('lec_summer_2023')['id'], "playoffs"))

    print("--- %s seconds ---" % (time.time() - start_time))


main()
