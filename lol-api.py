import eventsAPI
import leaguesAPI
import matchAPI
import teamsAPI
import time

def main(): 
    print("Api working")



start_time = time.time()

print(teamsAPI.getTeams('g2-esports'))
print(teamsAPI.getTeamCode('g2-esports'))
print(leaguesAPI.getLeagues())



print("--- %s seconds ---" % (time.time() - start_time))