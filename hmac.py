import hmac
import argparse
from hashlip import md5

parser = argparse.ArgumentPaser()

parser.add argument ("key")
parser.add argument ("data")

args = parser.parse args()

key = args.key

h = hmac.new(key,'',md5 )

##insert data 
h.update (args.data)

## output the HMAC digest
print h.hexdigest()
