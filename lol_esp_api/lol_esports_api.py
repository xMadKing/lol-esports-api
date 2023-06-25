import apis.eventsAPI as eventsAPI
import apis.leaguesAPI as leaguesAPI
import apis.matchAPI as matchAPI
import apis.teamsAPI as teamsAPI

def main():
    print("Api working")
    print(eventsAPI.getSchedule(leaguesAPI.getLeagueBySlug('lec')['id']))

main()
