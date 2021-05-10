import requests
from steam import steamid

class BanChecker:
    
    def checkBan(self, player_profile):
        
        player_steam_url = player_profile

        # pull steamid from profile link

        player_steamid = steamid.steam64_from_url(player_steam_url)

        # request etf2l data

        response = requests.get(f'https://api.etf2l.org/player/{player_steamid}.json')
        player_bans = response.json()['player']['bans']
        player_bans_out = []
        player_name = response.json()['player']['name']

        #ban check
        if player_bans:
            for ban in player_bans:
                player_bans_out.append(ban['reason'])
            bans=";".join(player_bans_out)
            return f"{player_name}'s bans: " + bans
        else:
            return f"{player_name} is clean on ETF2L"