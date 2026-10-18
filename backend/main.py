import requests
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()
TBA_API_KEY = os.getenv("TBA_API_KEY")
TEAM_KEY = "frc7763"
YEAR = 2026
url = f"https://thebluealliance.com/api/v3/team/{TEAM_KEY}/matches/{YEAR}"
headers = {"X-TBA-Auth-Key": "BHLil6pkSFw3sVxcAsl36eSl1wMHk5EPySAiVnnNNTGCnrOTbzZZU8jszoNxYSFT"}

def getData():
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            matches = response.json()
            return matches
        else:
            print(f"Error: Status code {response}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False
def sortData(array):
    result = {}
    latest = max(
        (x for x in array if x.get("actual_time") is not None),
        key=lambda x: x["actual_time"],
        default=None,
    )
    if TEAM_KEY in latest["alliances"]["red"]["team_keys"]:
        result["alliance"] = "red"
        result["allianceScore"] = latest["alliances"]["red"]["score"]
    elif TEAM_KEY in latest["alliances"]["blue"]["team_keys"]:
        result["alliance"] = "blue"
        result["allianceScore"] = latest["alliances"]["blue"]["score"]
    else:
        return {"ok": False}

    if latest["winning_alliance"] == result["alliance"]:
        result["win"] = True
        result["ok"] = True
        return result
    else:
        result["win"] = False
        result["ok"] = True
        return result

a = (sortData(getData()))
print(sortData(getData()))
if a["win"]:
    print("CARBO WINS!!!")
elif a["win"] != True:
    print("CARBO LOSS!!!")