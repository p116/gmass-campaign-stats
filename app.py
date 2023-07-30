import requests
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def get_all_campaigns(api_key):
    url = f"https://www.gmass.co/api/campaigns?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # Handle error if API call was not successful
        return None

def get_campaign_name(api_key, campaign_id):
    url = f"https://www.gmass.co/api/campaigns/{campaign_id}?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["subject"]
    else:
        # Handle error if API call was not successful
        return None

def get_opened_emails(apikey, campaign_id):

    # Replace CAMPAIGN_ID with the actual ID of the campaign you want to track

    url = f"https://www.gmass.co/api/reports/{campaign_id}/opens?apikey={apikey}"
    otherURL = f"https://api.gmass.co/api/reports/{campaign_id}/recipients?apikey={apikey}"
    response = requests.get(url)
    response2 = requests.get(otherURL)
    # Check if the API call was successful

    if response.status_code == 200 and response2.status_code == 200:
        data = response.json()
        data2 = response2.json()
        emailcounts = {}
        not_opened = []
        # Retrieve the information about the recipients who opened the email
        for add in data["data"]:
            emailcounts[add["emailAddress"]] = add["openCount"]

        # Retrieve the information about the recipients who haven't opened the email
        for ad in data2["data"]:
            if emailcounts.get(ad["emailAddress"]):
                pass
            else:
                not_opened.append(ad["emailAddress"])

        return emailcounts, not_opened

    else:
        # Handle error if API call was not successful
        return None


def plotData(ec):
    labels = list(ec.keys())
    values = list(ec.values())

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct=lambda p: '{:.0f}'.format(p * sum(values) / 100))

    ax.set_title('Opened Emails')

    st.pyplot(fig)


def main():
    st.title("GMass Email Tracker")

    # Prompt the user to input their API key
    api_key = st.text_input("Enter your GMass API key:")

    # If the user has provided an API key, proceed with the rest of the code
    if api_key:
        # Initialize session state variables
        if "selected_campaign" not in st.session_state:
            st.session_state.selected_campaign = None
        campaigns = get_all_campaigns(api_key)

        # If a campaign has been selected, display its stats
        if st.session_state.selected_campaign:
            email_counts, unopened_emails = get_opened_emails(api_key, st.session_state.selected_campaign)
            campaign_name = get_campaign_name(api_key, st.session_state.selected_campaign)
            total_recipients = len(email_counts) + len(unopened_emails)
            st.header(f"Campaign: {campaign_name}")
            st.subheader(f"Total Recipients: {total_recipients}")
            st.subheader("Opened Emails")
            plotData(email_counts)
            st.subheader("Unopened Emails")
            if unopened_emails:
                st.write("The following emails have not been opened:")
                st.write("\n".join([f"{i+1}. {email}" for i, email in enumerate(unopened_emails)]))
            else:
                st.write("All emails have been opened.")
        else:
            st.write("No data found for this campaign.")

        # Display a button for each campaign
        for campaign in campaigns:
            if st.button(campaign["subject"], key=campaign["campaignId"]):
                st.session_state.selected_campaign = campaign["campaignId"]

        # Debugging statement
        st.write("Selected campaign ID:", st.session_state.selected_campaign)

  



if __name__ == "__main__":
    main()
