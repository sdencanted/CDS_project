from ossapi import *
client_id=None #redacted
client_secret='' #redacted
redirect_uri='http://localhost:3914/'
api = OssapiV2(client_id, client_secret)
def getStarDifficulty(beatmap_id):
    try:
        return api.beatmap(beatmap_id=beatmap_id).difficulty_rating
    except:
        pass
    return -1