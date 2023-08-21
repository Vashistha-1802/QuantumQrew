# import streamlit as st
# import superagi

# # Create a title and a sidebar
# st.title("Web Scraper and Emailer")
# st.sidebar.header("Enter your details")

# # Get the user input from the sidebar
# url = st.sidebar.text_input("Enter the URL you want to scrape")
# email = st.sidebar.text_input("Enter your email address")

# # Create a button to trigger the agent
# if st.sidebar.button("Run Agent"):
#     # Initialize the SuperAGI api with your credentials
#     api = superagi.API("your_api_key", "your_api_secret")
#     # Create an agent with the webscraper and email tools
#     agent = api.create_agent(["webscraper", "email"])
#     # Set the input parameters for the agent
#     agent.set_input({"url": url, "email": email})
#     # Run the agent and get the output
#     output = agent.run()
#     # Display the output on the main page
#     st.write(output)
