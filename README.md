<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Kevdawg1/student-performance-prediction">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-NEICv1aGTvDRncdvM_fXoah5SNWx4pXAvg&s" alt="Logo" width="80" height="80">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJl4fp0SkQbTPU5ZxVl6AKWYuKCwM0gIhNtQ&s" alt="Logo" width="80" height="80">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Microsoft_Azure.svg/1200px-Microsoft_Azure.svg.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">EDI Cargo Application</h3>

  <p align="center">
    A standard format for exchanging business documents electronically.
    <br />
    <a href="https://github.com/Kevdawg1/student-performance-prediction"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Kevdawg1/student-performance-prediction">View Demo</a>
    &middot;
    <a href="https://github.com/Kevdawg1/student-performance-prediction/issues/new?template=bug_report.md">Report Bug</a>
    &middot;
    <a href="https://github.com/Kevdawg1/student-performance-prediction/issues/new?template=feature_request.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project aims to showcase a full stack application and ETL and CI/CD pipelines, aligning with industry standards of an MLOps infrastructure. The project will include a React web application that will host a simple form to encode and decode EDI messages. The form will query an API service powered by FastAPI for all logic functions. 

The API service is hosted in a Docker container that is published to Azure Container Registry for deployment. The web application is hosted in Azure Container Apps for better autoscaling and microservices.

The project also comes with custom logging and exception handling to efficiently improve troubleshooting in the app. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Python][Python]][Python]
* [![Conda][Conda]][Conda]
* [![React][React]][React]
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* python
  ```sh
  python -m pip install --upgrade pip
  ```

* npm


### Installation

#### Backend

1. Clone the repo
   ```sh
   git clone https://github.com/Kevdawg1/student-performance-prediction.git
   ```
2. Move into the backend directory
   ```sh
   cd edi-cargo-backend
   ```
3. Create virtual environment
   ```sh
   conda create -p venv python==3.11
   ```
4. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

#### Frontend
1. Move into the frontend directory
   ```sh
   cd edi-cargo-backend
   ```
2. Install dependencies
   ```sh
   npm install
   ```

### Set up Azure Container Registry

Azure Container Registry will be used to containerize the Docker Image of the project. 

1. Log in or sign up for a Microsoft Azure account.
2. Create an Azure Container Registry with the following details:
    * Registry Name: ensure that the registry name matches the domain of the Docker Image i.e. testdockerkevin
    * Location: select the closest region to your physical location
    * SKU: Standard
3. Once created, navigate to Settings > Access Keys > Admin User: Enabled.
    * Copy and paste the password in a secure location for later use

### Build and Push Docker Image to Azure Container Registry

Run the following commands from your terminal at the project root directory: 

** Replace `testdockerkevin` with your Azure Container Registry name.

```
docker build -t testdockerkevin.azurecr.io/mltest:latest .
```
```
docker login testdockerkevin.azurecr.io
```

Username: Your Azure Container Registry name

Password: Use the password you copied from the previous step. 

```
docker push testdockerkevin.azurecr.io/mltest:latest
```

### Create Azure Web App

1. In Azure App Services, create a web application. 
2. Ensure that the Resource Group is shared with the Container Registry created previously. 
3. Publish: select `Docker Container`
4. Region: select the closest region to your physical location
5. Pricing Plan: select a Free Tier plan if available
6. Under `Docker` settings, configure the following settings: 
    * Options: `Single Container`
    * Image Source: `Azure Container Registry`
    * Registry: select your container registry
    * Image: select the Docker image that was pushed previously
    * Tag: `latest`
7. Create the Web App.
8. Navigate to `Deployment Center`, enable Continuous Deployment.
9. Change the `Source` to `GitHub Actions: Build, deploy and manage your container app automatically with GitHub Actions`.
10. Under the GitHub Actions section, configure the following settings: 
    * Organization: select the relevant GitHub organization your project repository is under.
    * Repository: select your project repository.
    * Branch: main
11. Save your changes. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Python Application

To start the app locally, simply use the command below. If any changes are made, you will need to stop the program from running and restart it to see the changes applied. 

```sh
  python app.py
```

### React Application

```sh
  npm start
```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

README.md template from https://github.com/othneildrew/Best-README-Template/blob/main/README.md 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/kevin-kam-eng
[Python]: https://img.shields.io/pypi/pyversions/slack_bolt?style=for-the-badge&logo=python
[Python-url]: https://www.python.org/downloads/
[React]: https://img.shields.io/npm/v/react
[Conda]: https://img.shields.io/conda/d/conda-forge/python?style=for-the-badge&logo=anaconda
[Conda-url]: https://docs.anaconda.com/anaconda/install/