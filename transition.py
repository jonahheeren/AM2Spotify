import sys
import spotipy
import spotipy.util as util

scope = "user-library-modify"

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    ##CONTINUE
else:
    print "Can't get token for", username
