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
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">project_title</h3>

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
Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `rosiemaguire`, `Django-crowd-funding-project`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![Django][Django.com]][Django-url]
- [![Python][Python.org]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

{{ The features your MVP will include. (Remebber this is a working document, you can change these as you go!) }}

- [] feature
- [] feature

### Stretch Goals

{{ Outline three features that will be your stretch goals if you finish your MVP }}

- [] Stretch goal one
- [] Stretch goal two
- [] Stretch goal three

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## API Specification

| HTTP Method | Url       | Purpose              | Request Body   | Successful Response Code | Authentication <br /> Authorization |
| ----------- | --------- | -------------------- | -------------- | ------------------------ | ----------------------------------- |
| GET         | projects/ | Return all projects  | N/A            | 200                      | N/A                                 |
| POST        | projects/ | Create a new project | project object | 201                      | User must be logged in.             |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Database Schema

{{ Insert your database schema }}

![image info goes here](./docs/image.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Wireframes

{{ Insert your wireframes }}

![image info goes here](./docs/image.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Colour Scheme

{{ Insert your colour scheme }}

![image info goes here](./docs/image.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Fonts

{{ outline your heading & body font(s) }}

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Submission Documentation

{{ Fill this section out for submission }}

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

Deployed Project: [Deployed website](http://linkhere.com/)

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

- npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/rosiemaguire/Django-crowd-funding-project.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = "ENTER YOUR API";
   ```

### How To Run

{{ What steps to take to run this code }}

### Updated Database Schema

{{ Updated schema }}

![image info goes here](./docs/image.png)

### Updated Wireframes

{{  Updated wireframes }}

![image info goes here](./docs/image.png)

### How To Register a New User

{{ Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data). }}

### Screenshots

- [] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
  ![image info goes here](./docs/image.png)

- [] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
  ![image info goes here](./docs/image.png)

- [] A screenshot of Insomnia, demonstrating a token being returned.
![image info goes here](./docs/image.png)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
  - [ ] Nested Feature

See the [open issues](https://github.com/rosiemaguire/Django-crowd-funding-project/issues) for a full list of proposed features (and known issues).

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

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

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
[Django.com]: https://img.shields.io/badge/django-0b4b33?style=for-the-badge&logo=Django&logoColor=WHITE&color=0B4B33
[Django-url]: https://www.djangoproject.com/
[DRF.org]: https:fix-this-up-later.org
[DRF-url]: https://www.django-rest-framework.org
[Python.org]: https://img.shields.io/badge/python-white?style=for-the-badge&logo=python
[Python-url]: https://www.python.org/
