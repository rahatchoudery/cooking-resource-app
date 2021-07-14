# Cooking Resource App

## Overview
Between teaching myself how to cook and teaching myself Django, I understand the importance of not only finding resources, but finding the best ones. This cooking resource app is meant to serve as a comprehensive guide that provides reliable resources to chefs who are looking to learn or refine cooking techniques at any level.

## Data
I manually collected data for this project based on some of the best resources I've used to learn how to cook and consolidated them in a [Google Sheet](https://docs.google.com/spreadsheets/d/1yPbT8RefXyRLEG-FyC4ALW6bmnINIQANGklT5trffes/edit?usp=sharing), which I then accessed using the [Google Sheet API](https://developers.google.com/sheets/api/reference/rest).

## Functionality
[/home](ResourceApp/templates/ResourceApp/HomePage.html) -  user is welcomed to the website and directed to the next page

[/subject](ResourceApp/templates/ResourceApp/SubjectPage.html) - user is asked to choose a subject, level, and medium for their resources

[/results](ResourceApp/templates/ResourceApp/ResultsPage.html) - based on their selections on the previous page, user is given a list of custom cooking resources
