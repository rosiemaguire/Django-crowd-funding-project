<a name="readme-top"></a>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/rosiemaguire/Django-crowd-funding-project">
    <!-- <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
  </a>

<h1 align="center">Advocat</h3>

  <p align="center">
    by Rosie Maguire 
    <br>
    She Codes crowdfunding project - DRF Backend.
    <br />
    <a href="https://github.com/rosiemaguire/Django-crowd-funding-project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/rosiemaguire/Django-crowd-funding-project">View Demo</a>
    ·
    <a href="https://github.com/rosiemaguire/Django-crowd-funding-project/issues">Report Bug</a>
    ·
    <a href="https://github.com/rosiemaguire/Django-crowd-funding-project/issues">Request Feature</a>
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
      <a href="#features">Features</a>
      <ul>
        <li><a href="#stretch-goals">Stretch Goals</a></li>
      </ul>
    </li>
    <li><a href="#api-specification">API Specification</a></li>
    <li><a href="#database-schema">Database Schema</a></li>
    <li><a href="#wireframes">Wireframes</a></li>
    <li><a href="#colour-scheme">Colour Scheme</a></li>
    <li><a href="#Fonts">Fonts</a></li>
    <li><a href="#submission-documentation">Submission Documentation</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#how-to-run">How To Run</a></li>
        <li><a href="#updated-database-schema">Updated Database Schema</a></li>
        <li><a href="#updated-wireframes">Updated Wireframes</a></li>
        <li><a href="#how-to-register-a-new-user">How To Register a New User</a></li>
        <li><a href="#screenshots">Screenshots</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">RoadMap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)
{{ A paragraph detailing the purpose and target audience for your website. }}

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![Django][Django.com]][Django-url]
- [![Python][Python.org]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

- [X] User Log in/Out
- [X] Project creation (must be logged in user)
- [X] Project owner can update project
- [X] Pledge creation (must be logged in as user)
- [X] Pledge supporter can update pledge
- [X] Pledges able to be created without comment (optional field)

### Stretch Goals/ Roadmap

- [] User able to update account details
- [X] Have created/updated dates as current datetime, but created date not to be updated after initial post
- [X] Prevent pledge PUT from allowing project field to be changed
- [X] Pledges not to be created or updated if project is closed
- [] Project owner only able to update open/closed field if project has been set to closed
- [] Validation to ensure at least one field is modified in PUT Request (rather than just updating the last_modified date because PUT request fields are identical to data in table)
- [] Users able to "soft delete" (e.g. set deleted field to 1 which hides in front end) own pledges/projects

See the [open issues](https://github.com/rosiemaguire/Django-crowd-funding-project/issues) for a full list of proposed features (and known issues).
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## API Specification

| HTTP Method | Url                  | Purpose              | Request Body                   | Successful Response Code | Authentication <br /> Authorization       |
| ----------- | -------------------- | -------------------- | ------------------------------ | ------------------------ | ----------------------------------------- |
| GET         | projects/            | Return all projects  | N/A                            | 200                      | N/A                                       |
| GET         | pledges/             | Return all pledges   | N/A                            | 200                      | N/A                                       |
| GET         | users/               | Return all users     | N/A                            | 200                      | N/A                                       |
| POST        | projects/            | Create a new project | project object                 | 201                      | User must be logged in.                   |
| POST        | pledges/             | Create a new pledge  | pledge object                  | 201                      | User must be logged in.                   |
| POST        | users/               | Create a new pledge  | user object                    | 201                      | N/A                                       |
| PUT         | projects/< int:pk >/ | Update project       | project object or project field| 201                      | User (project owner) must be logged       |
| PUT         | pledges/< int:pk >/  | Update pledge        | pledge object or pledge field  | 201                      | User (pledge supporter) must be logged in.|
| PUT         | users/< int:pk >/    | Update user          | user object or user field      | 201                      | User must be logged in.                   |
| DEL         | projects/< int:pk >/ | Delete Project       |  N/A                           | 204                      | User must be logged in as administrator.  |
| DEL         | projects/< int:pk >/ | Delete Project       |  N/A                           | 204                      | User must be logged in as administrator.  |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Database Schema

![First Draft Database Schema](images/DatabaseSchema.svg)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Wireframes

![First Draft wireframes](images/Crowdfunding_wireframes.svg)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Colour Scheme

[![Colour Pallete][colour-palette]][colour-palette.url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Fonts

[![Font Family][font-family]][font-family.url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Submission Documentation

{{ Fill this section out for submission }}

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

Deployed Project: [Deployed website](http://linkhere.com/)

### Prerequisites
- `python`
- `pip`
- unrestricted execution policy (Windows requirement)

### How To Run

- Clone a copy of this repo to your local machine. This can be done in the command line by navigating to the desired directory, then running:

        git clone https://github.com/rosiemaguire/Django-crowd-funding-project.git
- Once you have a local version of this repository, you'll need to set up your virtual environment:
    -  navigate to the folder that contains the `requirements.txt` file
    - If you're on a windows machine, run the command 
            
            . venv/Scripts/activate
    - If you're on a mac, run the command 
            
            source venv/bin/activate
    - Install the Django library: 
            
            python -m pip install -r requirements.txt
    - Check installation was successful: 
    
            python -m pip freeze
    - Change directory to where manage.py is located:
            
            cd crowdfunding
    - Make the inital migrations:
        
            python manage.py migrate

    - Now with everything set up, you'll just need to run the server!

            python manage.py runserver
    
    <!-- Add information about accessing via API Tool (e.g. Insomnia, Postman) and front end urls -->
    - When you're finished press CTRL+C to quit the server
    - Deactivate the virtual environment by either using the command `deactivate` or terminate your terminal session.

### Updated Database Schema

{{ Updated schema }}

![image info goes here](./docs/image.png)

### Updated Wireframes

{{  Updated wireframes }}

![image info goes here](./docs/image.png)

### How To Register a New User

{{ Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data). }}

### Screenshots

- [X] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
  ![GET REQUEST RETURNING PROJECTS](images/Insomnia_Successful_GET_Request.png)

- [X] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
  ![PLEDGE POST REQUEST](images/Insomnia_Successful_POST_Request.png)

- [X] A screenshot of Insomnia, demonstrating a token being returned.
![AUTHENTICATION TOKEN POST REQUEST](images/Insomnia_Returning_Token.png)
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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Rosie Maguire - [@rosie_maguire](https://www.threads.net/@rosie_maguire)

Project Link: [https://github.com/rosiemaguire/Django-crowd-funding-project](https://github.com/rosiemaguire/Django-crowd-funding-project)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- []()
- []()
- []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/rosiemaguire/Django-crowd-funding-project.svg?style=for-the-badge
[contributors-url]: https://github.com/rosiemaguire/Django-crowd-funding-project/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/rosiemaguire/Django-crowd-funding-project.svg?style=for-the-badge
[forks-url]: https://github.com/rosiemaguire/Django-crowd-funding-project/network/members
[stars-shield]: https://img.shields.io/github/stars/rosiemaguire/Django-crowd-funding-project.svg?style=for-the-badge
[stars-url]: https://github.com/rosiemaguire/Django-crowd-funding-project/stargazers
[issues-shield]: https://img.shields.io/github/issues/rosiemaguire/Django-crowd-funding-project.svg?style=for-the-badge
[issues-url]: https://github.com/rosiemaguire/Django-crowd-funding-project/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/rosie-maguire-515777230
[product-screenshot]: images/screenshot.png
[Django.com]: https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=Django&logoColor=WHITE&color=0B4B33
[Django-url]: https://www.djangoproject.com/
[Python.org]: https://img.shields.io/badge/python-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjggMTI4Ij48bGluZWFyR3JhZGllbnQgaWQ9InB5dGhvbi1vcmlnaW5hbC1hIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeDE9IjcwLjI1MiIgeTE9IjEyMzcuNDc2IiB4Mj0iMTcwLjY1OSIgeTI9IjExNTEuMDg5IiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KC41NjMgMCAwIC0uNTY4IC0yOS4yMTUgNzA3LjgxNykiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iIzVBOUZENCIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzMwNjk5OCIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJweXRob24tb3JpZ2luYWwtYiIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSIyMDkuNDc0IiB5MT0iMTA5OC44MTEiIHgyPSIxNzMuNjIiIHkyPSIxMTQ5LjUzNyIgZ3JhZGllbnRUcmFuc2Zvcm09Im1hdHJpeCguNTYzIDAgMCAtLjU2OCAtMjkuMjE1IDcwNy44MTcpIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiNGRkQ0M0IiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNGRkU4NzMiLz48L2xpbmVhckdyYWRpZW50PjxwYXRoIGZpbGw9InVybCgjcHl0aG9uLW9yaWdpbmFsLWEpIiBkPSJNNjMuMzkxIDEuOTg4Yy00LjIyMi4wMi04LjI1Mi4zNzktMTEuOCAxLjAwNy0xMC40NSAxLjg0Ni0xMi4zNDYgNS43MS0xMi4zNDYgMTIuODM3djkuNDExaDI0LjY5M3YzLjEzN0gyOS45NzdjLTcuMTc2IDAtMTMuNDYgNC4zMTMtMTUuNDI2IDEyLjUyMS0yLjI2OCA5LjQwNS0yLjM2OCAxNS4yNzUgMCAyNS4wOTYgMS43NTUgNy4zMTEgNS45NDcgMTIuNTE5IDEzLjEyNCAxMi41MTloOC40OTFWNjcuMjM0YzAtOC4xNTEgNy4wNTEtMTUuMzQgMTUuNDI2LTE1LjM0aDI0LjY2NWM2Ljg2NiAwIDEyLjM0Ni01LjY1NCAxMi4zNDYtMTIuNTQ4VjE1LjgzM2MwLTYuNjkzLTUuNjQ2LTExLjcyLTEyLjM0Ni0xMi44MzctNC4yNDQtLjcwNi04LjY0NS0xLjAyNy0xMi44NjYtMS4wMDh6TTUwLjAzNyA5LjU1N2MyLjU1IDAgNC42MzQgMi4xMTcgNC42MzQgNC43MjEgMCAyLjU5My0yLjA4MyA0LjY5LTQuNjM0IDQuNjktMi41NiAwLTQuNjMzLTIuMDk3LTQuNjMzLTQuNjktLjAwMS0yLjYwNCAyLjA3My00LjcyMSA0LjYzMy00LjcyMXoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAgMTAuMjYpIi8+PHBhdGggZmlsbD0idXJsKCNweXRob24tb3JpZ2luYWwtYikiIGQ9Ik05MS42ODIgMjguMzh2MTAuOTY2YzAgOC41LTcuMjA4IDE1LjY1NS0xNS40MjYgMTUuNjU1SDUxLjU5MWMtNi43NTYgMC0xMi4zNDYgNS43ODMtMTIuMzQ2IDEyLjU0OXYyMy41MTVjMCA2LjY5MSA1LjgxOCAxMC42MjggMTIuMzQ2IDEyLjU0NyA3LjgxNiAyLjI5NyAxNS4zMTIgMi43MTMgMjQuNjY1IDAgNi4yMTYtMS44MDEgMTIuMzQ2LTUuNDIzIDEyLjM0Ni0xMi41NDd2LTkuNDEySDYzLjkzOHYtMy4xMzhoMzcuMDEyYzcuMTc2IDAgOS44NTItNS4wMDUgMTIuMzQ4LTEyLjUxOSAyLjU3OC03LjczNSAyLjQ2Ny0xNS4xNzQgMC0yNS4wOTYtMS43NzQtNy4xNDUtNS4xNjEtMTIuNTIxLTEyLjM0OC0xMi41MjFoLTkuMjY4ek03Ny44MDkgODcuOTI3YzIuNTYxIDAgNC42MzQgMi4wOTcgNC42MzQgNC42OTIgMCAyLjYwMi0yLjA3NCA0LjcxOS00LjYzNCA0LjcxOS0yLjU1IDAtNC42MzMtMi4xMTctNC42MzMtNC43MTkgMC0yLjU5NSAyLjA4My00LjY5MiA0LjYzMy00LjY5MnoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAgMTAuMjYpIi8+PHJhZGlhbEdyYWRpZW50IGlkPSJweXRob24tb3JpZ2luYWwtYyIgY3g9IjE4MjUuNjc4IiBjeT0iNDQ0LjQ1IiByPSIyNi43NDMiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMCAtLjI0IC0xLjA1NSAwIDUzMi45NzkgNTU3LjU3NikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiNCOEI4QjgiIHN0b3Atb3BhY2l0eT0iLjQ5OCIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzdGN0Y3RiIgc3RvcC1vcGFjaXR5PSIwIi8+PC9yYWRpYWxHcmFkaWVudD48cGF0aCBvcGFjaXR5PSIuNDQ0IiBmaWxsPSJ1cmwoI3B5dGhvbi1vcmlnaW5hbC1jKSIgZD0iTTk3LjMwOSAxMTkuNTk3YzAgMy41NDMtMTQuODE2IDYuNDE2LTMzLjA5MSA2LjQxNi0xOC4yNzYgMC0zMy4wOTItMi44NzMtMzMuMDkyLTYuNDE2IDAtMy41NDQgMTQuODE1LTYuNDE3IDMzLjA5Mi02LjQxNyAxOC4yNzUgMCAzMy4wOTEgMi44NzIgMzMuMDkxIDYuNDE3eiIvPjwvc3ZnPgo=
[Python-url]: https://www.python.org/
[colour-palette]: images/ColorHuntPaletteb5f1cce5fdd1c9f4aafcc2fc.png
[colour-palette.url]: https://colorhunt.co/palette/b5f1cce5fdd1c9f4aafcc2fc
[font-family]:
[font-family.url]: