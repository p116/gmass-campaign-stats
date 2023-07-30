# GMass Campaign Visualizer

This program is a simple Streamlit app that allows users to track and visualize the email open rates for campaigns using the GMass API.

## Description

The GMass Email Tracker is a Python program built with Streamlit, requests, numpy, and matplotlib. It lets users input their GMass API key and then view the open rates of their email campaigns. The program fetches data from the GMass API and displays it in an interactive manner using Streamlit.

## Requirements

Make sure you have the following packages installed:

- requests
- numpy
- matplotlib
- streamlit

You can install them using pip:

pip install requests numpy matplotlib streamlit

## Usage

1. Run the program by executing the following command:
streamlit run gmass_email_tracker.py

2. A Streamlit app will be launched in your browser, prompting you to enter your GMass API key.

3. Enter your GMass API key in the text input field and click on "Enter" to proceed.

4. The app will fetch all the campaigns associated with the provided API key and display buttons for each campaign.

5. Click on a campaign button to view the email open rates for that specific campaign.

6. The app will show the total recipients, the number of opened emails, and a pie chart representing the open rates.

7. If there are unopened emails in the campaign, the app will also display a list of those email addresses.

8. You can switch between different campaigns by clicking on their respective buttons.

## Function Descriptions

- `get_all_campaigns(api_key)`: Retrieves a list of all campaigns associated with the provided GMass API key.

- `get_campaign_name(api_key, campaign_id)`: Retrieves the subject (name) of a specific campaign using its campaign ID.

- `get_opened_emails(api_key, campaign_id)`: Fetches information about recipients who opened the email and those who haven't opened it yet for a given campaign.

- `plotData(ec)`: Generates a pie chart to visualize the open rates of the emails for a selected campaign.

- `main()`: The main function that runs the Streamlit app. It prompts the user for their GMass API key, fetches campaign data, and displays campaign statistics and open rates.

## Note

Make sure to generate an API key for your GMass account through their dashboard at https://app.gmass.co/dashboard

For any issues or questions, feel free to contact me!

Enjoy tracking your GMass email campaigns with this simple yet effective Email Tracker!
