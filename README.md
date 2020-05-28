# Django Models

## Overview
Django has a powerful Object Relational Mapper that allows us to persist data using Python instead of SQL.

A project with one model, wire up that model using Django Views, and give it a little style as well.

## Feature Tasks and Requirements
- create blog project
- create blog app
- migrate data
- create Post model
    - Have 3 fields, one must be ForeignKey related to auth.User E.g.
        - add title CharField property
        - add author ForeignKey property related to auth.User with CASCADE delete option.
        - add body TextField property
- activate the model
- add model to admin
- modify Post model have user friendly display in admin
- create migrations and migrate data
- create a super user
- create HomePageView
    - extend ListView
    - give a template of home.html
    - associate Post model
- create home.html template
    - in templates folder in root of project
    - register templates folder in project settings
    - use Django Templating Language to display each post’s title and body
- create base.html ancestor template
    - add main html document
    - use Django Templating Language to allow child templates to insert content
- update HomePageView to provide explicit name for object list
- update url patterns for app and project
- add 4 posts in admin
- view home page and confirm 4 posts showing properly
- create PostModelTest
    - create Post object in set up
    - create test to verify the post’s text is correct
- create HomePageViewTest
    - test view’s status code
    - test view using correct template
    - use url name instead of hard coded path
- add styling
    - create static folder at root of project
    - update STATICFILES_DIRS
    - create base.css file which styles base.html elements
    - load static css in base.html file
- add detail view
    - link post_detail.html template
    - associate Post model
- create post_detail.html template
    - template should extend base
    - content should display post title and body
- update app urlpatterns to handle detail view
    - account for primary key in url
- add link in home page template to related post detail page
- add blog tests
    - create a user and post before each test
    - verify proper string representation of a Post instance
    - verify Post instance content
    - verify PostListView
    - verify PostDetailView
