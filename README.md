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
  <a href="https://github.com/Kevdawg1/edi-cargo-project">
    <img src="https://upload.wikimedia.org/wikiversity/en/8/8c/FastAPI_logo.png" alt="Logo" width="80" height="80">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlGmKtrnxElpqw3AExKXPWWBulcwjlvDJa1Q&s" alt="Logo" width="80" height="80">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJl4fp0SkQbTPU5ZxVl6AKWYuKCwM0gIhNtQ&s" alt="Logo" width="80" height="80">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Microsoft_Azure.svg/1200px-Microsoft_Azure.svg.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">EDI Cargo Application</h3>

  <p align="center">
    A standard format for exchanging business documents electronically.
    <br />
    <a href="https://github.com/Kevdawg1/edi-cargo-project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Kevdawg1/edi-cargo-project">View Demo</a>
    &middot;
    <a href="https://github.com/Kevdawg1/edi-cargo-project/issues/new?template=bug_report.md">Report Bug</a>
    &middot;
    <a href="https://github.com/Kevdawg1/edi-cargo-project/issues/new?template=feature_request.md">Request Feature</a>
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
   git clone https://github.com/Kevdawg1/edi-cargo-project.git
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
    * Registry Name: ensure that the registry name matches the domain of the Docker Image i.e. clearaitakehomeproject
    * Location: select the closest region to your physical location
    * SKU: Standard
3. Once created, navigate to Settings > Access Keys > Admin User: Enabled.
    * Copy and paste the password in a secure location for later use

### Build and Push Docker Image to Azure Container Registry

Run the following commands from your terminal at the project root directory: 

** Replace `clearaitakehomeproject` with your Azure Container Registry name.

```
docker build -t clearaitakehomeproject.azurecr.io/mltest:latest .
```
```
docker login clearaitakehomeproject.azurecr.io
```

Username: Your Azure Container Registry name

Password: Use the password you copied from the previous step. 

```
docker push clearaitakehomeproject.azurecr.io/mltest:latest
```

### Create Azure Container App

1. In Azure Container Apps, create a container application. 
2. Ensure that the Resource Group is shared with the Container Registry created previously. 
3. Enter the name of your container app and save it as a Github Action Secret under the secret name `AZURE_CONTAINER_APP_NAME`
4. Region: select the closest region to your physical location
5. Deployment Source: Container image
6. Under `Container` settings, configure the following settings: 
    * Image Source: `Azure Container Registry`
    * Registry: select your container registry
    * Image: select the Docker image that was pushed previously
    * Image Tag: `latest`
7. Create the Container App.

### Create Azure Static Website

1. In Azure Storage Accounts, create a storage account.
2. Enter the name of your storage account and save it as a Github Action Secret under the secret name `STORAGE_ACCOUNT_NAME`.
    * Region: select the closest region to your physical location
    * Primary Serivce: `Azure Blob Storage or Azure Data Lake Storage Gen 2`
    * Performance: `Standard`
3. Create the storage account instance. 
4. When created, navigate to `Data Management` > `Static Website`.
5. Enable the static website
    * Index document name `index.html`
    * Error document path: `index.html`

### Github Action Secrets Setup

| Secret Name  | Value |
| ------------- | ------------- |
| `AZURE_CREDENTIALS`  | JSON from CLI Command: `az ad sp create-for-rbac --sdk-auth`  |
| `STORAGE_ACCOUNT_NAME` | Name of your storage account created |
| `ACR_LOGIN_SERVER` | Find this in ACR > Settings > Access Keys e.g. `clearaitakehomeproject.azurecr.io` |
| `ACR_USERNAME` | Find this in ACR > Settings > Access Keys e.g. `clearaitakehomeproject` |
| `ACR_PASSWORD` | Find this in ACR > Settings > Access Keys |
| `AZURE_CONTAINER_APPS_NAME`  | Name of your container app created  |


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Python Backend pplication

To start the app locally, simply use the command below. If any changes are made, you will need to stop the program from running and restart it to see the changes applied. 

```sh
  cd edi-cargo-backend | python main.py
```

### React Frontend Application

```sh
  cd edi-cargo-frontend | npm start
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