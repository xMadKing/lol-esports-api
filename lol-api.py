import apis.eventsAPI as eventsAPI
import apis.leaguesAPI as leaguesAPI
import apis.matchAPI as matchAPI
import apis.teamsAPI as teamsAPI
import time


def main():
    print("Api working")

    start_time = time.time()

    print(leaguesAPI.getStandingsByStage(leaguesAPI.getTourmanentBySlug('lec_summer_2023')['id'], "playoffs"))

    print("--- %s seconds ---" % (time.time() - start_time))


main()
