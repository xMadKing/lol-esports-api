# LOLESPORTS API (by xmadking)

## Introduction
This is just a an easier to install and use (for python) version of https://vickz84259.github.io/lolesports-api-docs/ This api will also do a little more stuff but its very similar. So, special thanks to vickz84259 as this would not be possible if not for the documentation. 

## How to install

You can install this using ```pip install lol-esp-api```

There are 4 main 'API's in the project
1. Leagues API (Information in regards to leagues, such as LPL, LCK, LEC, LCS and more)
2. Match API (Information in regards to matches, details, results, etc... )
3. Teams API (Information about the teams, players, logos, etc...)
4. Events API (Information about events, live, games, schedule, etc... )

You can either import each API individually or import them all using the lol-api.py file. 

## Usage

### Teams API

1. ```getTeams(slug)```
If not input is specified this returns a list of all teams. If a team slug is specified (URL friendly string of team's name) then it will return that team's information. 

2. ```getTeamPlayers(slug)```
Returns the players of a specific team. 

3. ```getTeamId(slug)```
Returns team ID based on the input slug.

4. ```getTeamSlug(id)```
Returns team Slug based on the input Id. 

5. ```getTeamImgUrl(slug)```
Returns team IMG url based on the input slug. 

6. ```getTeamCode(slug)```
Returns team code based on the input slug. 

### Leagues API

1. ```getLeagues()```
Returns all leagues and their information.

2. ```getLeagueBySlug(slug)```
Returns league based on the input slug

3. ```getLeagueById(id)```
Returns league based on input id.

4. ```getTournamentsForLeague(leagueId)```
Returns tournaments for the league based on th leagueId.

5. ```getTournaments()```
Returns all tournaments and their information.

6. ```getTournamnetById(id)```
Returns information about tournament based on input ID.

7. ```getTournamentBySlug(slug)```
Return information about tournament based on input slug. 

8. ```getStandings()```
Returns all standings.

9. ```getStandingBy_TID(tournamentID)```
Returns the standings of a tournament based on the input ID. 

10. ```getStandingsByStage(TournamentID, stage_slug)```
Returns the standings for a specific tournament stage based on the input ID and stage slug. 

### matchAPI

1. ```getWindow(gameID, startingTime)```
Returns game and match details of the specified gameID. startingTime is optional. 

2. ```getDetails(gameID, startingTime, participantIDs)```
Returns game details based on the specified parameters. startingTime and participantIDs are option. ParticipantIDs is a list of IDs separated by underscores NOT COMMAS. 

### eventsAPI

1. ```getSchedule(leagueID, pageToken)```
Returns the schedule based on the specified parameters. PageToken is optional.

2. ```getLive()```
Returns the live events.

3. ```getCompletedEvents(tournamentID)```
Returns the schedule of completed events.

4. ```getEventDetails(eventID)```
Returns the details of an event. 

5. ```getGames(gameIDs)```
Returns the games. GameIDs is optional.