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

- [![DRF][DRF.org]][DRF-url]
- [![Django][Django.com]][Django-url]
- [![Python][Python.org]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

{{ The features your MVP will include. (Remebber this is a working document, you can change these as you go!) }}

- [] feature
- [] feature

### Stretch Goals/ Roadmap

{{ Outline three features that will be your stretch goals if you finish your MVP }}

- [] Update Account Details
- [] Stretch goal two
- [] Stretch goal three

See the [open issues](https://github.com/rosiemaguire/Django-crowd-funding-project/issues) for a full list of proposed features (and known issues).
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

This is an example of how to list things you need to use the software and how to install them.

- npm
  ```sh
  npm install npm@latest -g
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
[DRF.org]: https://img.shields.io/badge/Django%20Rest%20Framework-7F2D2D?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNzAwIiBoZWlnaHQ9IjQ2NiIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgNzAwIDQ2NiI+CiAgICA8aW1hZ2Ugd2lkdGg9IjcwMCIgaGVpZ2h0PSI0NjYiIHhsaW5rOmhyZWY9ImRhdGE6aW1hZ2UvcG5nO2Jhc2U2NCxpVkJPUncwS0dnb0FBQUFOU1VoRVVnQUFBSUFBQUFCVkNBWUFBQUNCemV4WEFBQUFBWE5TUjBJQXJzNGM2UUFBR01sSlJFRlVlRjd0WFFsWWxGWGJ2dGszQlhIRFJCT1gzOVJNemRUVStNUjl0eXlsTkVzejA4ejk5ek1zYzh1c0xQYzBsejZ6Y3NVdE5aZk0zRXJOY0FsY2NGOVlORkZSQVpGMWdQKzZIK2JNL3pMTXdKRHdPY3FjNitJQ1pzNzdudk9lNXo3UGZwN1hMaXNyS3d1MlZteFh3TTRHZ0dKTGUzbHdHd0NLTi8xdEFDam05TGNCd0FZQW14SllyREZnMHdHS05mbHRTbUF4Sjc4TkFEWUEyUHdBeFJzRE5oMmdlTlBmWmdZV2MvcmJBR0FEZ00wUFVLd3hVS1E2UUVaR0J2amo3T3hjckJmWm1oKytTQUh3ODg4LzQ0Y2Zma0J3Y0RDKy9mWmJIRDkrSEY5OTlaVTFyMGV4bTF1UkFFQkpsVldyVm1IYXRHazRlZktrZ09EZ3dZT1lOMitlWVpIWno4N09MdmVpWjJXQlNRckczMlZtWnNwbnhwK3I4VXplcTlpUnRHQVBYT2dBT0hyMEtBNGNPQUFTS3lrcENXdldyQkVBN055NUU5SFIwUmd3WUFEdTNic25ISUhpd2NIQkFhMWF0VUw5K3ZXeFlNRUNlSHQ3NCthTkc5QmxaS0JKa3lidzkvZVgrMnpidGcxWHIxNFY0dHZiMjZOU3BVcm8zcjI3QUNzbUprWStiOW15SlJvMmJGaXdGU2ptdlFzVkFBa0pDZmpnZ3c5UXBVb1Z2UEhHRzVnK2ZUcDI3OTR0QUpnd1lRSU9IVHFFWGJ0MkNUaCsrKzAzMUsxYkY1TW1UWUtycXl0bXpacUZ4bzBibzBhTkdwZzRjU0xpNCtQeDBVY2ZZZlhxMWJoKy9Ucm16cDJMenovL1hLN2J1bldyY0pKZmYvMVZQdHV5Wll0OHZuRGhRbXpldkZsQVpHdVdyVUNoQWlBeU1oS3Z2dnFxRUtSOCtmSll0bXlaZ01BWUFDa3BLZmpycjc5QTFuM3AwaVVjUG53WTgrYlBSNVBHamZIU1N5OWgvUGp4K1B2dnY5R2pSdzlzMkxBQnZPK21UWnZ3MldlZkNkR1hMRm1DdFd2WFl0R2lSVUxzM3IxN3k5T1NrM1RxMUFsQlFVR1dQYjJ0VitINkFTSWlJdkRhYTYvSkRpMVhycHdBWWR5NGNia0E4T21ubndvQUtBNHVYTGdnUHdvQVBYdjJ4Tml4WXdVQWdZR0JXTGR1SGR6YzNJU3plSHA2SWowOUhkMjZkUk4yUDJmT0hOU3JWdy90MnJVekFJQWk0NU5QUHJHUjFzSVZLRlFPUUtMMTdkc1hTNWN1UmNXS0ZURmx5aFJzM0xneEZ3QW91MS9yMVF1QmVtS25wcWJtQ1lCYnQyNEp5NTgvZno0Y0hSMUYzbE4zV0xGaWhYQUc2Z0hVRTdwMjdTcmlvMjNidGhZK3ZxMWJvUUtBTFAyWFgzNFJaWTRFb2tKRzlrOTJyZFVCdnY3NmErellzVU80QlB2Y3YzOGZRV1BIb3UrYmI2Sk5telo0NjYyM1FLS1RsWC81NVplaUE1Q1R1THU3ZzJEaE9BUUUvUXNVTS92MjdaUHZxRk44L1BISE5xb1dZQVVLRlFBY2w4U2h0czlXb1VJRjNMNTlHMDg4OFVRT0FQQzd5NWN2dzhYRlJUakYzYnQzVWJwMGFkSG1TVWl5ZWxvSUJBRkJNbmp3WUxSbzBVSjJOa1VBd1VTMlQwV1QvYWdqRUF5OEZ5MEVXN044QlFvZEFLYUdwblpPZmFCeTVjcFl2SGl4NWJQVDl4dytmTGlBaVBvQkxZbjE2OWNMVjZGdVlHc1B0Z0wvRlFEUWxLT01KbXVuYUNob28zbEprVUZPUVE3QjNVL3U4cUNOM0lQdG44enBRY2UybHV2L0t3Q3dsb2MxbmtkYVdwcDhWSnhqRlRZQVdBaUFwTGc0cENVbENXQ2NYRnpnNXVVRmUwZEhhOFcyeGZNcVZBRGNpWXJDYjRzV21mVHZpMitmMDZJcjE5RVJUdTd1cUZpbkRxbzFiUXJYVXFXZ1MwK0hnNFVMZW1URkN0eTZlRkhpQlZsNk5zNzcybWtVUUk2bFBmU28vYitVcnkrYTllK1BqTXpNYklJYVJTdlpsNlptNU5HakNOK3hBdzVPVGloZm93WTh2TDFoNytTRTVMZzQzTDE2RmZkdTNoU3Zwb2xvaG9FQWFnNXFmUG10am1OeXp2cDVHditXcFRJaW80cUZ2UHpaWnhZVE9MK09oUXFBNjJmTzRFNTBOSjV1M3o3UGNma2czRTJYLy9nRGUrZlBGMUIwL2ZoalZHblFJTC81eXZlcmhnM0Q2N3dPRUt1QVppSjFBa3RZZWFaT2g4UEJ3V2dVR0loTWZTREsrTHI3ZCs5aVNlL2VlTHBEQjdRYU5rd0FvRzJaZWdJbTNiK1BFaVZLV0RSbmJhZkV4RVFCbUllSFI0R3VaWHprNjI3ZE1ITDc5Z0pkbDFmbndnWEEyYk80SFJXRjJtM2FGRWl4U3JsM0QzK3VXb1gweEVUVTdkd1pUOVN1bmVjRHJoNDJETDNuejVlQWtZTzl2WmlkTkFHNXM1eU1pR1Y4b3d5ZERrZFdyMGFqVjE4MUNZQUwrL2ZqM042OVFuaVAwcVZ6ellOajhJZm1KZ2xKcGRSVWhES3ZCMkF3ak5jVUJEdzZuVTV1dWJoblR3emR0TWxLQVhEbURPS3VYY05UclZ1REU3WmtSNm9ub1VJV0Z4V0YwSTBiMGFSWEwzaFhybXoySVZjTkhZclg1czJEdlQ0MEhCVVJnU2Y5L01RblFPNlNGd2p5NGdCazZ6dW1UY09MVTZia0lENEovdGY2OVlnNWZ4NlpHUmtvVjYwYW5tN2ZBVm5PVGlqcDVTVmpFaENXaHFNTHlnRzRscncvZjc3dTN0MjZBWEQzMmpYVWFkdFdGbVhybENsSXZIVUwzSFZabVpteWVPbkp5VWhPU0lCWGhRcG8zcThmZko5NUJ1N2UzaUFBQ0poTGh3N2g3L1BuOGE5Ky9jd0NZT1dRSWVpellJSGgrMFBidHlQMFAvOFJHVzFuWjQvTXpBelkwV1ZNT1VxOVFKTnpRSk9QT2tDSDk5K0hqblBLekJSL0F1ZTJiT0JBOUYyeXhPQk1TazlKd2Q1NTh4QVpGb1lPLy82MzZBSHNuM0RqQmtJM3JNZkZRMy9peVFZTjBLeGZQMFNmT0lHandjRW9XYTVjdnJ1VCtvN29RdmIycUZ5dkhnTGVlMCt1T2JKbWpYQWZlNzJwVE9DVktGTUdTZkh4QmwwbkxUa1pieTFkbXU4WWxuWW9YQkdnNXdDMTliNTRBcURqdUhIaXY5YzJ5dTNFdURoRWhZVGdhbGdZMkw5U3c0WUdqckZ1ekJpOE9Ia3lYRXpJVis2R05TTkc1QURBMFQxNzRKNlJnVHI2b0JCRkF3bWFId2VpWDRGRWNIZHp3NDBMRjNEOTlHazBEZ3cwVFBYM2I3NUJwWHIxVVBYNTU3TVZON0oralIvamZsSVNNaE1UY1hMN2RnRjRyVFp0VU9iSkozTUF6aFFobEFpZ1puRm8rWEswMUFDZ1ZxdFdLRm0rdkZ6R1RVSEFhdjBVNUI0RkVSMzVBYUZJQWJCbHloUjBIVDllWkxXV0xYTXhoUnZvZE1oTVNjSE8yYk1STUd3WXZQVzc1OXFwVTdoNDZCQUNCZzQwekovWE1BNUE5L0hxNGNNTlNpQTdHQU9BbjNHbkVtanNiNjVkdTNaTlhORHNFN1pwRTN4cTFvUnYzYnJTbmRkdkNBckN5OU9tQ1VnWXIrRENrM2gwVmJQeE02WElLYzJlM0k3V1RGN2l3QklBa1BoY00rUDdXRDBBbEFqZ0FoRUEzU1pNQUxWbUxwQ3h4NDBtVWxwcUtxNGNQQ2hvcjlleG95d3NGL0g3L3YweFlQbHlBKzFVOWhEdll3a0E1RDRaR1RLdWxnT0pCWktXSmpvSzUwUGlFZ0JIZ29OUjhlbW5SU1N4WGZyakR5VGV2bzFudW5UQm5UdDNVTFpzV1FNd2twS1RVY0xESXdjQXRDRGp1SG5wQkFvQTVJdC9tdUFBN21YS0dES2ZqTUZyOVFDZ0VxaEVnQUlBNVowb2FOVFNIUjFsWnlxT3dNV0lDUTFGVW1JaTZuZnViSGplcjdwMFFmL2dZQ1FuSjJmYjJucUZqOWY5UEdGQ3ZoeEEzWWpqa2dPNU9Edkw3cVc4NS9nVUQ4b1Z6TCtOQVJBVkZvYllTNWZRc0VjUDNJNk5SUmtOQURnbjdud3RCOUFTU2poY0hvcWhXUUFFQjZOR3k1YndLbC9lYkZEcmtRVUFGNGdMdzUzSHhWR3NtZjlIaElUZ2ZrSUM2bmZxWkZqSHVaMDZZZmkyYmNJTnRJNGE5bDgzYXBTWWdhcVpFZ0hHTzVJTHA2S01CQUNCb0hVRkg5dXdBVS9VcWlWY2dNQ2dBcmxtNUVqRE9IRnhjU2psNVlYWTI3Y04zTUFjQU5UWW5Lc2pkUWFqeEZkeklpQmsxU294b1QxOWZNeUtyVWNLQUZRQ3UwNllrR01CNkgyakZxd0F3RUNQY0lENzk5RkF6d0V5MHRQeHc0QUI2UGZkZHliOUNWcEhrRGtkZ0orVEFCeFBURU05NXlGeGxSS2xCY0RWRXljUWMvWXNuZ3NNTk5qNVZBSXIxS3FGbWkxYUNFR01zNWp6QTREb0VnU1RrWWxvaWdOd3JqUTFhN2R1YlZBQ1RhSGdrUUtBVmdSb0g0WUVVZXlYaTNwcTJ6WjQrdnFpUnBNbTB1M3NuajFJam85SGcrN2RUU3BUbGdBZ0xqNGVKVDA4Ukd1bitDQ3hsU2hSNE5NQ2dKeG14ZURCZUdQeFlnUG82S0Q2NC92dmNmL09IUUd5MXRWc3JBU2EyN0tteEVFT0FDeGJobVlEQm9oSVBMWnVIYlJXd0dNUEFHcjFHUWtKMkx0Z0FUcFBuSmd0bDNVNkxCODBDUDJXTE1tMTRHcEJqQUZ3Wk04ZTROWXRpU3R3d2JucmhmWHFHd0ZBL1NQYnQ1N3RkZWRuSEorbW5iT0xpd0RsNXNXTE9MNWxDd0puek1nQnZPdG56MkxiSjUrZzFkQ2h3aEhjUzVXU3VWbkNBYlM2aUZJTXRTTGdqeFVyRURCb2tNaDgrZ0VlZXdDUVFQY1RFM0h6OUdtUTdUTEsxbXJJRU5nNU9ja3VPTE43dHdSYm51dlowNndjTkFiQW1iQXdKSnc3QjBjbnAremRxL2ZWMnprNFpOdnZkTHJBRHRuSFRiSURQVlFNSlpERTcrM3REWmFDczVzNy91ZGYvbkEwTWgvcGdEbjE4OCs0ZCt1V2pGUGpYLzRvVWRIWFluOCtSeGJGME01T1hNaWkxR1praVBNbzROMTNaVjZQUGdCT240YVlnWHFIekUrVEowdkFSMFhxR0ZSeGNuVVY3eGJOcTRwMTY4SzdVaVdEbVJoMzlTb09yMXlKRG1QR3dDbVBiQjlqQUZ5SmlFRGxTcFZ5T1p5NHFFeEVvY0puNnBRUmR6Qk5SSW9FUzFQSnFKL0VYNytPa05XcmNUc3lFaTlQbldveVptQU92WlQxbkJORm9LdWpJMEpvQmc0WmtnMkE0R0RVZWxSMEFHclNzYkd4WWxLcGRqY3lFbkhSMGFqcTc1K3ROQUdDZUlNV3JLbEtxejJVekxCcTFKSER1UFZYS0ZxTUc1ZkQyMlpxSVhkT21vUU9uMzZLakxRMElTd3RpTlM0T01QTzEyL3o3T05sMmRxYjlGT0JISHJ0Vkovc2lXWnpDVU9vVm1udDZuTTdPNVN1VWlVSFNIaS8rSmdZbkZ5NUVyNysvcWhVdjM0dXJtRnE3c29TSXVDeTB0TnhZdDA2Tkh6elRlbDZac3NXK0xWb0lia0c1cHJ5aDZqdkNXN21UZjdUVnFTZVFFc210WFBtVExpV0xJblNmbjU0cWxXcmZLTjV2Q2RqQWIzbXpUTTRlV2dHSm9TSGk2OWVOWW9aOTVJbGVmQWh4elNFRGRPOTZ1eU10SlNVYk03QU5IUE5tVU1EY1BRZ1RyMTNEemN1WGhUT1ZrVno5SXdjeE1YUkVlRy8vQ0poOEJmNjk0ZXp1M3VlajUyV25pNFdEd0ZBVjNESXlwWC83d3ArbERpQXFhZGtQb0RXRVJTMmNTT3Vuam9sQkhZdFVRSnVucDV3OGZSQ0RmOFg1SDg1R1JRU2dvc0hEcUQxaUJGQ2ZMTEl2S0o1bEorYnhvekJHNHNXR2FhUTdRZlFvVTdiN0FNaTlOUUoyOWRNOGw1aUlxNWN1WUlLUGo3dzh2SVN4VTlyQmZCdmMyNWp6cE5CckYxejV1REM3Ny9qN1dYTHhGVFRLb0huZnZzTmFZbUpJdHJNTlhKTGloeWxBemhrWnVZRXdPT29CRExRd2FpYUxpVUZxVWxKWWxMUjNuMTE5bXpScE9rM0p4ZW8vL0xMOEtsV1RSUWxZN2V4TWh0SkpIcmc4aklEeGYwTDVMQUNGRUV1WDdrQ1AzMndoanN3aHhsb1FTaVo5MG1oMWJKd0ljcjYrYUY2UUFCSzY1TlRLWTYyVHAyS3JoTW5tc3hzMG9aMERXWmdWcGFZbWN3OUlDZDY5SlZBSXc1Z3pnOFFjZXdZenV6YWhZNUJRZG1wVjhlT2dhWlcwejU5aEZZa09MVjBaeWNuZy90V25RYmk5K1lBUUJlMGNqT2JDc2J3L0FCVDA1WENaNXdVS201am5TN1BBSkxNVDZkRDlQSGpPTHAyTGJwUG5XcklHRHEzYjU4QXZPRXJyK1JnQWh5SE8xK05xL1VESEZxMkRBR0RCOHM2OEg2UHZCbG9LaGlrZFlXS25aNlJnVjB6WnFEZWl5OUtYaUEvMnpodUhEcDk4SUZCQVZMYWNrbktjU05YcXNvSVVxdE1FZUNtMDZGeTA2YUdTSjB4RythWWpQNDlTUTZnYjZheWdnVjhSc2tzbkIvRlNuSlNrbmdSS1NvNHA1TTdkeUkxUGw3U3kxU2IwN0VqUnUzWVlmaWZFVS82SkxUUFFBQ3dPZG5aR1lKQm5OK3h0V3ZGRmF6Q3dhWkVpZFY3QXZNQ2dQS0swVmFucm5CaTZ6YTg4SFovMlVFM3IxekJUK1BIUzdKRG10NFg3K0xxS3R6QU9KL0FsQ1BJTVNrSkRicDBNZWs1Rk4rK25SMGlJaU5ScldyVlBBSEFMNDFMMjlCZHJZQ293dEk4MG43MTNEbmNEQS9Icy9SWTZoTlNwelZ2ampHLy95NmN5Tnk1QStvT2RFS1Y5ZkxLa1E5d2JQMTZQTld5SlVyb0EwK1BGUURVemxmRXBDbTJiK0ZDMU8zUUFlVnExQkI1SEh2K1BNNGZPQUQvZDk0eDVQZUpBcWFQM3FrRk1lWUE5QVJTQ1h5NlhlNWtWQlgySlFDb0ExZ0NBQ1dHT0NjU091YkdEVkVlMWVjcUduZ2pJZ0xYang5SHZhNWREYVlyQVREMjRFR2tKQ2RMRU11VUtDSUhJQUJLZVhqa0FJQ0lnSGJ0NEVGUG82bktLWUFva0ZhZEVLTGxBQ29ZcEx4Z3h2a0FESlFzRGd4RXY2Vkw0ZWp1THF4eTM0SUZzcUJ1UGo1d2MzVVZ1VW13aUh0WG4xbWtPSUN3NXFRa25Ba0p5WkVScElCaUhKY3ZDQUFVc2RVdWxubm9UVXJPaDhTTk9IRUN0ODZkUTJONkxSbnlUay9Ib2g0OThPNlBQeHB5K0V6dFlsTWlnUDJVRWlnY3dFUXBIUGF4ZWdBWTV3TXdpSkpYYlB6djhIQnhzUVlNSHk2eTljYjU4d2pidkJudHg0d3haQUNKTDErZlUwZzNyQUtBMnQzSDl1N05CUUN0MXEySVFET3dxZ2tSUU9DRi83SURaYXRXeTVXUlRBQ1FBeEc4RXQ2bE4xTVB4TzNUcDZOMlFBQ3E2b05ZVkFLWnYxZS9XN2M4UFl2NUpZUlFCekJYRDhucUFXQ3NBM1QrNktOOFU4VC8yckFCcnQ3ZXFOTzZ0ZENLTzRIeEFQK0JBM09aaEF3bHI5WG5BNUE0NUFyRytRREczaklGQU9Od3JsSUNIZTN0RWJwcEU2SkRRM0hoNEVINER4Z2dhZU04QWNURzY3UitBbG9CYTBhTmdrK3RXaElnVXV4NmZWQVFla3liWmphSXBlWmhDUUNVTG1LY1dXVDFBRkFjZ0l2MjA2UkplSW5uOWMzSU03VWdzVmNpRVBiVFpyUWRPZExBTVdsQ2x2RHhnWU9qQTNTcGFiTHp4R1dibFlXYkVSSG9Nbmt5M1BRRUNqdHdBQmMzYjg1MjlkS1BRRytmbVZOR0lrNTBPdlNjUGgxWitua1JBQ2UyYmtYTmdBQzRlbnJpU2tnSVR1L2NDVjFhbXJpQVMxV29BSHRuWitoU1U1RjQ4eVppSXlQUitQWFg0ZTNuWndnR2hlL2NpYVE3ZDlDNFZ5OVRYRC9IWjVZQ1FJa2g3Ym1EUndJQXpJNGxDOXMrZFNxNlRaeVlMd0Q0b0VmWHIwZGliQ3hhRGg1c1dDd2xjNmt3Y1JFWUxsYjVmUFFScUV3aEhneWhmYTlWK014UndkVEJFQzBBbUtLdWJYUmkwYlluOGVrK2R2YjBoRWZKa3RKRmVRSkR0MjVGMUpFakFtQlRoMG1NNTFJUUFDaE9RSzhtWGRoV0R3QWVydURCRU1wTWM0NGdVOFNodmJ5MGQyLzArUEpMbE5YSWFkVlhuY0toUzlmTDB6TTc3cThYQVZGUlVmRDE5YzFYMU1oaW1qZ1pSQUFjVzc4QlZSbzlCMDhlTVhOek14dVFVdUtBMTl5T2lVSG82dFVTSWlaSHNiVGxCd0NQc21VTkNxZFNuRlVnaTBxdjFWb0IxMDZlbEoxY3ZucDFXUXV5MGY3TGxsbTBMcElEYjIrUDNYUG5vbG5mdmprT1dKQVZYOXkvSDdIUjBRWUZUTWxteHZUdk1sK3ZWQ21MRHBmUzhtRGdoZ2REdEdjRHMvMFNXK0hnNGlKeEFza1ZzTE9UQ0o4Nkc4aHJ5UW40bTRkRWIvTWNaSnMycVB6c3N4WTlvMVlIb0d4M3lNckNqMEZCcU42OHVYd1Z6UU1vUVVISWNuVTErQkMwSmU4a2x5SXBDWjU2RGxTZ1FjMTBMdFJvSUFNbWQxak1VVE1ZYlh4TG1qb1p4THc4bW9LOTlDVmx1U2k3NXN4RzB6NXZvRXpWcXJsT3pHckR5aXFrYXp5ZWNYU1BPUW5ldnI1Z1pJNU5lNENFeEUySWlaSDRCWnNvWVhvbmp6aXk5S2VSR2JKMUwxM2E0andDN1p3VUIvQndkMGZzNWNzNXBzdG4xQjQreWZVcytuT0pscXlwSlgwS0ZRQ1dER2l1andJQXY3OGJIWTJmSms2RVY4V0s4Q2hUQnUxR2ozNlFXNXU5OW1FVmlQZ25oME9MWkFHczZjMmhXZ0R3WVVYampvMlZjM3hGMVI1V2lSZ2JBRXhRMUJnQVJVVjBhN2l2RWx1V25pWXV5amxicFFnb3JBZG1uZUlaTTJhZ2V2WHE2TnFsQ3pwcURwNFUxaGhGZVI4Q3BWZXZYcGc5ZTdiVVB5aUs5dGdDZ0l2SFVyTE0vbmxUbjNPWFgvR0lvbGpnQjdrbm40RjFrQWtBbHNrcmltWTFBS0NIenZqZ3hZTThNRXZVc2xRdDdXaFZ0cGFWUnovODhFT01HVE1HKy9mdmx4ZFlzQzR4ZmYxTXJHVDFVZHJZbzBhTmtqTDEzMzMzblRpWFdQMjBYNzkrVXNqU3o4OVBTdUR6dml5TlAweWZ6ZE9oUXdjcFlObW9VU084L2ZiYllHMURWa3pkczJjUHZ2bm1HemxnK3Q1Nzcwa2Q1ZkR3Y0tsOHlvcm9kZXJVa1hjcThQRHB6Smt6cFJiaTY2Ky9Ma1V3MlY4QmdQb0tnY3dDMlU4OTlkU0RMRTJPYTYwR0FJWDJSUG9iY2NGbnpwcUZoczgraTRDQUFDaytUYUs4OE1JTFVuR1V4YWJwUUtLRGlRdktzdlY4WndGckVMSmZ6Wm8xTVdMRUNFeWVQRm1JeVBLMkRBMlQ0Q1FVZ1VBaVVjVHdldjQ5ZXZSb0tZTE51Z01zV2R1eFkwZXBaczQrektCbTVYUytRWVVGdFFrWWdvcmpwcWFsWWZhc1dWSXluKzlWNk4rL3Y1VE1KU2g0WC9iaitBUUVyeXRNM2VHeEJRRFpKNnVTODZVVDdkdTN4NGtUSjRTdzNJRk03bUJqdVZvU2s4UmhTZHRYWG5sRlpDNzdrVmprSEx3SDMwSEFrdlpzenozM25PeDBsckZsMWROcTFhb0pRUWdtZnQ2OFdUUDg3K2pSVXVlWW5JUUZyTG5MZVg5cS95UnU1ODZkNWYwSEJBN25RN0R3L2dRQVdUMDVBQnVmZ2Rlek5XdldUTGhYWVJlMUxIWUEyTDFuanlGaGxGemduWGZlRVRhN2N1Vks0UVlLQU55MUpBYmZVY0F5dHl4UnF3REFpdVFrS0luSE41K29YRDlXR3FFemlnUW1lQmlwN05LbGl4UzBKdUc0azBsUTdtSUNnTUJndGZPcFU2Zml5SkVqQWdBV3ZPYjNDZ0FFTUxrU1g3ZEQ3a0hPVTVpdFdBT2dhZE9tR0RwMHFCQ0NCT0gvbGdLQU81THZNMkFoNitlZmZ4Nm5UNTlHN2RxMUpkL2dpeSsra0JkZExGKytYRjZjMGFkUEgvRTJVcG1qUlRKbzBDRFJPVmcybjZYMWZYeDhSQlNZQW9EU0FRZ1V4U1VLODQwb2p6VUErRG9aS21WS0JJd2NPUksvN3RwbDRBQjhEeEVWUmNZUlNDUkdIZm1XRXNwK2lnQnlBTjZEL2ZnZUpEYSsxb1p2Tk9HYlRjNmRPeWZLSE45bHhGZmRLSzVCNHZPbEZhR2hvU0lldU92TGxDbUQ3Ny8vWHY0bjkzai8vZmR4NnRRcG1SdnZ3WE1NQkFnNUFEOVRISUR6b3BnaTBUbFg2Z1hVTlFxclBiWUFLS3dGZXR6dll3UEE0MDdoZko3UEJnQWJBSXhPVHhiekJTbHVqMi9qQU1XTjRrYlBhd09BRFFBMkVWQ2NNV0RqQU1XWit0YVVFVlRNNmZEUUh0L0dBUjdhMGx2SHdEWUFXQWNkSHRvc2JBQjRhRXR2SFFQYkFHQWRkSGhvczdBQjRLRXR2WFVNYkFPQWRkRGhvYzNpL3dCSUVTTGpTUWtnSmdBQUFBQkpSVTVFcmtKZ2dnPT0iLz4KICA8L3N2Zz4=
[DRF-url]: https://www.django-rest-framework.org
[Python.org]: https://img.shields.io/badge/python-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjggMTI4Ij48bGluZWFyR3JhZGllbnQgaWQ9InB5dGhvbi1vcmlnaW5hbC1hIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeDE9IjcwLjI1MiIgeTE9IjEyMzcuNDc2IiB4Mj0iMTcwLjY1OSIgeTI9IjExNTEuMDg5IiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KC41NjMgMCAwIC0uNTY4IC0yOS4yMTUgNzA3LjgxNykiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iIzVBOUZENCIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzMwNjk5OCIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJweXRob24tb3JpZ2luYWwtYiIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSIyMDkuNDc0IiB5MT0iMTA5OC44MTEiIHgyPSIxNzMuNjIiIHkyPSIxMTQ5LjUzNyIgZ3JhZGllbnRUcmFuc2Zvcm09Im1hdHJpeCguNTYzIDAgMCAtLjU2OCAtMjkuMjE1IDcwNy44MTcpIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiNGRkQ0M0IiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNGRkU4NzMiLz48L2xpbmVhckdyYWRpZW50PjxwYXRoIGZpbGw9InVybCgjcHl0aG9uLW9yaWdpbmFsLWEpIiBkPSJNNjMuMzkxIDEuOTg4Yy00LjIyMi4wMi04LjI1Mi4zNzktMTEuOCAxLjAwNy0xMC40NSAxLjg0Ni0xMi4zNDYgNS43MS0xMi4zNDYgMTIuODM3djkuNDExaDI0LjY5M3YzLjEzN0gyOS45NzdjLTcuMTc2IDAtMTMuNDYgNC4zMTMtMTUuNDI2IDEyLjUyMS0yLjI2OCA5LjQwNS0yLjM2OCAxNS4yNzUgMCAyNS4wOTYgMS43NTUgNy4zMTEgNS45NDcgMTIuNTE5IDEzLjEyNCAxMi41MTloOC40OTFWNjcuMjM0YzAtOC4xNTEgNy4wNTEtMTUuMzQgMTUuNDI2LTE1LjM0aDI0LjY2NWM2Ljg2NiAwIDEyLjM0Ni01LjY1NCAxMi4zNDYtMTIuNTQ4VjE1LjgzM2MwLTYuNjkzLTUuNjQ2LTExLjcyLTEyLjM0Ni0xMi44MzctNC4yNDQtLjcwNi04LjY0NS0xLjAyNy0xMi44NjYtMS4wMDh6TTUwLjAzNyA5LjU1N2MyLjU1IDAgNC42MzQgMi4xMTcgNC42MzQgNC43MjEgMCAyLjU5My0yLjA4MyA0LjY5LTQuNjM0IDQuNjktMi41NiAwLTQuNjMzLTIuMDk3LTQuNjMzLTQuNjktLjAwMS0yLjYwNCAyLjA3My00LjcyMSA0LjYzMy00LjcyMXoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAgMTAuMjYpIi8+PHBhdGggZmlsbD0idXJsKCNweXRob24tb3JpZ2luYWwtYikiIGQ9Ik05MS42ODIgMjguMzh2MTAuOTY2YzAgOC41LTcuMjA4IDE1LjY1NS0xNS40MjYgMTUuNjU1SDUxLjU5MWMtNi43NTYgMC0xMi4zNDYgNS43ODMtMTIuMzQ2IDEyLjU0OXYyMy41MTVjMCA2LjY5MSA1LjgxOCAxMC42MjggMTIuMzQ2IDEyLjU0NyA3LjgxNiAyLjI5NyAxNS4zMTIgMi43MTMgMjQuNjY1IDAgNi4yMTYtMS44MDEgMTIuMzQ2LTUuNDIzIDEyLjM0Ni0xMi41NDd2LTkuNDEySDYzLjkzOHYtMy4xMzhoMzcuMDEyYzcuMTc2IDAgOS44NTItNS4wMDUgMTIuMzQ4LTEyLjUxOSAyLjU3OC03LjczNSAyLjQ2Ny0xNS4xNzQgMC0yNS4wOTYtMS43NzQtNy4xNDUtNS4xNjEtMTIuNTIxLTEyLjM0OC0xMi41MjFoLTkuMjY4ek03Ny44MDkgODcuOTI3YzIuNTYxIDAgNC42MzQgMi4wOTcgNC42MzQgNC42OTIgMCAyLjYwMi0yLjA3NCA0LjcxOS00LjYzNCA0LjcxOS0yLjU1IDAtNC42MzMtMi4xMTctNC42MzMtNC43MTkgMC0yLjU5NSAyLjA4My00LjY5MiA0LjYzMy00LjY5MnoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAgMTAuMjYpIi8+PHJhZGlhbEdyYWRpZW50IGlkPSJweXRob24tb3JpZ2luYWwtYyIgY3g9IjE4MjUuNjc4IiBjeT0iNDQ0LjQ1IiByPSIyNi43NDMiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMCAtLjI0IC0xLjA1NSAwIDUzMi45NzkgNTU3LjU3NikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiNCOEI4QjgiIHN0b3Atb3BhY2l0eT0iLjQ5OCIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzdGN0Y3RiIgc3RvcC1vcGFjaXR5PSIwIi8+PC9yYWRpYWxHcmFkaWVudD48cGF0aCBvcGFjaXR5PSIuNDQ0IiBmaWxsPSJ1cmwoI3B5dGhvbi1vcmlnaW5hbC1jKSIgZD0iTTk3LjMwOSAxMTkuNTk3YzAgMy41NDMtMTQuODE2IDYuNDE2LTMzLjA5MSA2LjQxNi0xOC4yNzYgMC0zMy4wOTItMi44NzMtMzMuMDkyLTYuNDE2IDAtMy41NDQgMTQuODE1LTYuNDE3IDMzLjA5Mi02LjQxNyAxOC4yNzUgMCAzMy4wOTEgMi44NzIgMzMuMDkxIDYuNDE3eiIvPjwvc3ZnPgo=
[Python-url]: https://www.python.org/
[colour-palette]: images/ColorHuntPaletteb5f1cce5fdd1c9f4aafcc2fc.png
[colour-palette.url]: https://colorhunt.co/palette/b5f1cce5fdd1c9f4aafcc2fc
[font-family]:
[font-family.url]: