# QuantumQrew
"QuantumQrew: Leveraging SuperAGI to automatically summarize web content scraped from URLs and deliver summaries to email inboxes. Revolutionizing information consumption with advanced AI and streamlined communication."

# QuantumQrew SuperAGI Summarizer

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



## 🛠 Tools Used
<a href="#"><img src=https://superagi.com/wp-content/uploads/2023/08/Web_scraper_logo.png height=50px width=50px alt="Web Scraper" valign="middle" title="Web Scraper"><a href="#"><img src=https://superagi.com/wp-content/uploads/2023/05/Group-113612.png height=50px width=50px alt="Email"  valign="middle" title="Email"></a>

## 💻 Screenshots

<p align="center">
  <a href="https://superagi.com//#gh-dark-mode-only">
    <img src="https://superagi.com/wp-content/uploads/2023/05/Dark-Dashboard.png" alt="SuperAGI logo" />
  </a>
</p>


## 🛣 Roadmap
[Click here to checkout the latest roadmap 🔗](https://github.com/users/TransformerOptimus/projects/5/views/1)


<a id="architecture">

## 🌐 Architecture
</a>
<details>
<summary>SuperAGI Architecture</summary>

![SuperAGI Architecture](https://superagi.com/wp-content/uploads/2023/06/SuperAGI-Architecture.png)
</details>

<details>
<summary>Agent Architecture</summary>

![Agent Architecture](https://superagi.com/wp-content/uploads/2023/06/Agent-Architecture.png)
</details>

<details>
<summary>Agent Workflow Architecture</summary>

![Agent Workflow Architecture](https://superagi.com/wp-content/uploads/2023/06/Agent-Workflow.png)
</details>

<details>
<summary>Tools Architecture</summary>

![Tools Architecture](https://superagi.com/wp-content/uploads/2023/06/Tool-Architecture.png)
</details>

<details>
<summary>ER Diagram</summary>

![ER Diagram](https://superagi.com/wp-content/uploads/2023/06/ER-Diagram.png)
</details>


## ⚙️ Setting up

1. Download the repo using `git clone https://github.com/TransformerOptimus/SuperAGI.git` in your terminal or directly from github page in zip format.

2. Navigate to the directory using `cd SuperAGI` and create a copy of `config_template.yaml`, naming it `config.yaml` (take note of the file extension `.yaml`, *not* `.yml`).
3. Enter your unique OpenAI API Key, Google key, Custom search engine ID without any quotes or spaces in `config.yaml` file. Follow the links below to get your keys:

|Keys|Accessing the keys|
|--|--|
|**OpenAI API Key**| Sign up and create an API key at [OpenAI Developer](https://beta.openai.com/signup/)|
|**Google API key**| Create a project in the [Google Cloud Console](https://console.cloud.google.com/) and enable the API you need (for example: [Google Custom Search JSON API](https://developers.google.com/custom-search/v1/introduction)).|
|**Custom search engine ID**| Visit [Google Programmable Search Engine](https://programmablesearchengine.google.com/about/) to create a custom search engine for your application and obtain the search engine ID.|

4. Ensure that Docker is installed in your system, if not, Install it from [here](https://docs.docker.com/get-docker/). 
5. Once you have Docker Desktop running, run the command: `docker-compose up --build` in the SuperAGI directory. Open your browser and navigate to `http://localhost:3000` to access SuperAGI.

   - If you wish to change the port it's running on, open the `docker-compose.yml` file and update the `proxy` container port forwarding, for example: `"3000:80"`



## ⚠️ Under Development!
This project is under active development and may still have issues. We appreciate your understanding and patience. If you encounter any problems, please first check the open issues. If your issue is not listed, kindly create a new issue detailing the error or problem you experienced. Thank you for your support!


## 👩‍💻 Contributors
[![TransformerOptimus](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/133493246?v=4&w=50&h=50&mask=circle)](https://github.com/TransformerOptimus) [![Cptsnowcrasher](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/133322218?v=4&w=50&h=50&mask=circle)](https://github.com/Cptsnowcrasher) [![vectorcrow](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/133646556?v=4&w=50&h=50&mask=circle)](https://github.com/vectorcrow) [![Akki-jain](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/92881074?v=4&w=50&h=50&mask=circle)](https://github.com/Akki-jain) [![Autocop-Agent](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/129729746?v=4&w=50&h=50&mask=circle)](https://github.com/Autocop-Agent)[![COLONAYUSH](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/60507126?v=4&w=50&h=50&mask=circle)](https://github.com/COLONAYUSH)[![luciferlinx101](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/129729795?v=4&w=50&h=50&mask=circle)](https://github.com/luciferlinx101)[![mukundans89](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/101278493?v=4&w=50&h=50&mask=circle)](https://github.com/mukundans89)[![Fluder-Paradyne](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/121793617?v=4&w=50&h=50&mask=circle)](https://github.com/Fluder-Paradyne)[![nborthy](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/101320057?v=4&w=50&h=50&mask=circle)](https://github.com/nborthy)[![nihirr](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/122777244?v=4&w=50&h=50&mask=circle)](https://github.com/nihirr)[![Tarraann](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/97586318?v=4&w=50&h=50&mask=circle)](https://github.com/Tarraann)[![neelayan7](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/43145646?v=4&w=50&h=50&mask=circle)](https://github.com/neelayan7)[![Arkajit-Datta](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/61142632?v=4&w=50&h=50&mask=circle)](https://github.com/Arkajit-Datta)[![guangchen811](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/103159823?v=4&w=50&h=50&mask=circle)](https://github.com/guangchen811)[![juanfpo96](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/14787156?v=4&w=50&h=50&mask=circle)](https://github.com/juanfpo96)[![iskandarreza](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/32027019?v=4&w=50&h=50&mask=circle)](https://github.com/iskandarreza)[![jpenalbae](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/8380459?v=4&w=50&h=50&mask=circle)](https://github.com/jpenalbae)[![pallasite99](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/26508636?v=4&w=50&h=50&mask=circle)](https://github.com/pallasite99)[![xutpuu](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/11964505?v=4&w=50&h=50&mask=circle)](https://github.com/xutpuu)[![alexkreidler](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/11166947?v=4&w=50&h=50&mask=circle)](https://github.com/alexkreidler)[![hanhyalex123](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/100895608?v=4&w=50&h=50&mask=circle)](https://github.com/hanhyalex123)[![ps4vs](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/91535358?v=4&w=50&h=50&mask=circle)](https://github.com/ps4vs)[![eltociear](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/22633385?v=4&w=50&h=50&mask=circle)](https://github.com/eltociear)
[![shaiss](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/113060?v=4&w=50&h=50&mask=circle)](https://github.com/shaiss)
[![AdityaRajSingh1992](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/105219157?v=4&w=50&h=50&mask=circle)](https://github.com/AdityaRajSingh1992)
[![namansleeps2](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/134390870?v=4&w=50&h=50&mask=circle)](https://github.com/namansleeps22)
[![sirajperson](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/396941?v=4&w=50&h=50&mask=circle)](https://github.com/sirajperson)
[![hsm207](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/2398765?v=4&w=50&h=50&mask=circle)](https://github.com/hsm207)
[![unkn-wn](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/43097991?v=4&w=50&h=50&mask=circle)](https://github.com/unkn-wn)
[![DMTarmey](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/590474?v=4&w=50&h=50&mask=circle)](https://github.com/DMTarmey)
[![Parth2506](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/122429822?v=4&w=50&h=50&mask=circle)](https://github.com/Parth2506)
[![platinaCoder](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/47349795?v=4&w=50&h=50&mask=circle)](https://github.com/platinaCoder)
[![anisha1607](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/60440541?v=4&w=50&h=50&mask=circle)](https://github.com/anisha1607)
[![jorgectf](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/46056498?v=4&w=50&h=50&mask=circle)](https://github.com/jorgectf)
[![PaulRBerg](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/8782666?v=4&w=50&h=50&mask=circle)](https://github.com/PaulRBerg)
[![boundless-asura](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/122777244?v=4&w=50&h=50&mask=circle)](https://github.com/boundless-asura)
[![JPDucky](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/34105363?v=4&w=50&h=50&mask=circle)](https://github.com/JPDucky)
[![Vibhusha22](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/128478691?v=4&w=50&h=50&mask=circle)](https://github.com/Vibhusha22)
[![ai-akuma](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/7444521?v=4&w=50&h=50&mask=circle)](https://github.com/ai-akuma)
[![rounak610](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/81288115?v=4&w=50&h=50&mask=circle)](https://github.com/rounak610)
[![AdarshJha619](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/53672264?v=4&w=50&h=50&mask=circle)](https://github.com/AdarshJha619)
[![ResoluteStoic](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/105219157?v=4&w=50&h=50&mask=circle)](https://github.com/ResoluteStoic)
[![JohnHunt999](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/137149331?v=4&w=50&h=50&mask=circle)](https://github.com/JohnHunt999)
[![Maverick-F35](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/138012351?v=4&w=50&h=50&mask=circle)](https://github.com/Maverick-F359)
[![PaulRBerg](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/8782666?v=4&w=50&h=50&mask=circle)](https://github.com/PaulRBerg)
[![jorgectf](https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/46056498?v=4&w=50&h=50&mask=circle)](https://github.com/jorgectf)

  
<p align="center"><a href="https://github.com/TransformerOptimus/SuperAGI#"><img src="https://superagi.com/wp-content/uploads/2023/05/backToTopButton.png" alt="Back to top" height="29"/></a></p>


## Contact Us
Have questions or feedback? Feel free to reach out to us at qrewquantum@gmail.com

