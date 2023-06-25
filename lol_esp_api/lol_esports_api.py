import eventsAPI as eventsAPI
import leaguesAPI as leaguesAPI
import matchAPI as matchAPI
import teamsAPI as teamsAPI

def main():
    print("Api working")
    print(eventsAPI.getSchedule(leaguesAPI.getLeagueBySlug('lec')['id']))

main()
