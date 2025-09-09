import requests
from requests.exceptions import ConnectionError, JSONDecodeError

URL = "https://parcari.adp-sector1.ro/"
#add try except to test timeout on requests same with curl --connect-timeout
try:
    response = requests.get(URL, timeout = 5)
    sc = response.status_code
    if sc < 200 or sc > 300:
        print("Site is still DOWN")
    else: 
        print("Site is UP")

except ConnectionError as e: 
    print(f"Site is DOWN", str(e))

except JSONDecodeError:
    print(f"Bad json encoding", response.json())

# Finally runs after each try and/or except
# Finally should be used to handle any context that needs to be cleared
#finally:
   # del response