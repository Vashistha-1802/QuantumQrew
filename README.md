# QuantumQrew
"QuantumQrew: Leveraging SuperAGI to automatically summarize web content scraped from URLs and deliver summaries to email inboxes. Revolutionizing information consumption with advanced AI and streamlined communication."

# QuantumQrew SuperAGI Summarizer
<p align = "center"><a href="#"><img src=https://github.com/Vashistha-1802/QuantumQrew/assets/81288311/02926a2f-e38b-4d65-8afc-1cc870b37ea2 height=215px width=200px alt="LOGO" valign="middle" title="LOGO"></a>
</p>

Welcome to QuantumQrew's SuperAGI Summarizer Agent! 🚀

## Introduction

QuantumQrew's SuperAGI Summarizer Agent is an innovative tool that automates the process of summarizing web content using cutting-edge artificial general intelligence (SuperAGI). It combines advanced web scraping, powerful AI summarization, and seamless email delivery to provide concise and informative summaries of webpages, directly to your inbox.

## Features

- **Web Scraping:** Our tool efficiently extracts relevant data from webpages using a robust web scraping tool.
- **SuperAGI Summarization:** Leverage the power of SuperAGI to create accurate and insightful summaries that capture the essence of the original content.
- **Email Delivery:** Automatically receive summaries in your email inbox, saving you time and effort.
- **Customization:** Configure your preferences, such as summarization length and delivery frequency, to suit your needs.

## How It Works

1. The web scraping tool gathers data from a provided URL.
2. SuperAGI processes the extracted data, generating high-quality summaries.
3. Summaries are sent directly to your email inbox using our integrated email tool.

## Getting Started

To get started with the QuantumQrew SuperAGI Summarizer, follow these steps:

<p align="center">
<a href="https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=640182997&machine=basicLinux32gb&location=EastUs"> <img src="https://github.com/codespaces/badge.svg"></a><br>Not sure how to setup? <a href="https://youtu.be/yvmNthyWYCE">Learn here</a>
</p>

## Getting Started

To utilize the QuantumQrew SuperAGI Agent, follow these steps:

### Initial Setup

1. **Access Codespace (Optional):** If the provided commands do not work on your machine, consider using Codespace to customize your agent.

### Running Your Agent

1. **Create Agent:**

   Run the following command to create your SuperAGI agent. Replace `{{URL}}` with the actual API endpoint URL.
    # Run the curl command for creating the agent
   
```bash
curl --location -g '{{URL}}/api/v1/agent' \
--header 'X-API-Key: YOUR_API_KEY' \
--data '{
    "name": "My AI Assistant",
    "description": "Automates summarization of web content",
    "goal": ["Generate summaries"],
    "agent_workflow": "Goal Based Workflow", 
    "constraints": [
        "~4000 word limit for short term memory.",
        "Exclusively use the commands listed in double quotes e.g. \"command name\""
    ],
    "tools":[
        {   
            "name":"Email Toolkit"
        },
        {   
            "name":"Web Scrapper Toolkit"
        }
    ],
    "iteration_interval": 500,
    "model": "gpt-4",
    "max_iterations": 25,
    "schedule": null
}'
```

2. **Run Agent:**
Execute the following command to run your SuperAGI agent. Replace {{URL}} and {{agent_id}} with the actual API endpoint URL and agent ID.

```bash
curl --location -g '{{URL}}/api/v1/agent/{agent_id}/run' \
--header 'X-API-Key: bf2b13a0-c5d3-403f-a887-ac8849b8304b' \
--data '{}'
```

### Accessing Results
After running the agent, you can view the generated summary in your email inbox.

#### Please note that due to API credits constraints, the QuantumQrew SuperAGI Agent's full functionality is not available at the moment. However, future updates will include an extension that enables users to access summaries effortlessly.

We apologize for any inconvenience and appreciate your understanding. If you encounter any issues or have questions, contact us at contact@quantumqrew.com.



## 🛠 Tools Used
<a href="#"><img src=https://superagi.com/wp-content/uploads/2023/08/Web_scraper_logo.png height=50px width=50px alt="Web Scraper" valign="middle" title="Web Scraper"></a><a href="#"><img src=https://superagi.com/wp-content/uploads/2023/05/Group-113612.png height=50px width=50px alt="Email"  valign="middle" title="Email"></a><a href="#"><img src=https://superagi.com/wp-content/uploads/2023/05/Group-113613.png height=50px width=50px alt="Google Search" valign="middle" title="Google Search"></a><a href="#"><img src=https://superagi.com/wp-content/uploads/2023/05/Group-113614.png height=50px width=50px alt="Github" valign="middle" title="Github"></a>

## 💻 Screenshots
![image](https://github.com/Vashistha-1802/QuantumQrew/assets/81288311/bf396a8f-a799-4ee8-a47f-012f06355b13)
![mail_from_superagi](https://github.com/Vashistha-1802/QuantumQrew/assets/81288311/fb6fe09d-b4b1-4a64-87ae-11be77489812)





<p align="center"><a href="https://github.com/TransformerOptimus/SuperAGI#"><img src="https://superagi.com/wp-content/uploads/2023/05/backToTopButton.png" alt="Back to top" height="29"/></a></p>


## Contact Us
Have questions or feedback? Feel free to reach out to us at qrewquantum@gmail.com

