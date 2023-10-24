import requests

FORM_URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdgSLozEfmb5gKE8d_hyxBVRiXpvuFFUXdTVlPOVuRLfDxySg/formResponse"
MULTI_CHOICE_ENTRY_ID = "entry.953604185"

def submit_vote(choice_id):
    data = {
        MULTI_CHOICE_ENTRY_ID: choice_id
    }

    response = requests.post(FORM_URL, data=data)
    if response.status_code == 200:
        print(f"Successfully voted for choice {choice_id}!")
    elif response.status_code == 429:
        print(f"Failed to vote for choice {choice_id}.  Status Code: 429, you are most \nlikely being rate limited.")
    else:
        print(f"Failed to vote for choice {choice_id}. Status Code: {response.status_code}.")

# Automate votes
CHOICE_ID_FOR_YOUR_NAME = value="Ziegler, Ryne"
while True:
    submit_vote(CHOICE_ID_FOR_YOUR_NAME)
