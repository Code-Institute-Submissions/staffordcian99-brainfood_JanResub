# Brainfood
## A Website for a takeaway restaurant 


The primary goal of the website is to give potential customers of the restaurant the opportunity to view the menu, find their favourite food and place an order for delivery.

 ### The Business Goals of This Website Are: 
 1. To create a good impression of the restaurant online.
 2. Gain more profits by allowing customers to order online.
 3. Showcase the restaurants menu.

 ### The User Goals of This Website Are:
 1. To view a menu.
 2. Create an account and login easily.
 3. Search for menu items they like.
 4. Easily navigate the menu.
 5. View the details of each menu item.
 6. recover their password if they lose it.
 7. See the price of each item.
 8. Calculate how much money ir required as they add items to the bag.
 9. Have the ability to check out itens and pay online.
 

 # UX
 ### The ideal user:
 * Enjoys takeaway food.
 * Lives near the restaurant.

 ### Visitors to this website are searching for:
 * An easy way to purchase a meal.
 * An easy to view menu.
 * A way to pay for their meal online.
 * A way to login to see their order history.

 ### This project caters for these needs by:
 * Providing an easy to navigate menu divided into categories.
 * Displaying the price and a description of each item.
 * Allowing the user to search for their favourite items.
 * Providing a bag for the items they select and allowing the to checkout with stripe.
 * Allowing users to create an account.

 ## User Stories

1. As a customer, I would like to be able to view the menu.
2. As a customer, I would like to be able to see the price and description of each item.
3. As a customer, I would like the ability to navigate the menu quickly and easily.
4. As a customer, I would like to be able to order and pay online.
5. As a customer, I would like to create a personal account.
6. As a customer, I would like the ability to login, logout and change my password if I lose it.
7. As a customer, I would like to view my order history.
8. As a manager, I would like to be able to add and remove items from the menu.

# Features

## Header
Each page features a consistent and responsive header.
The header consists of a logo in the top left corner which links to the home page, a search bar, which finds keywords through-out the menu and an account and shopping bag icons. The account icon opens a dropdown menu when clicked which displays options to login or sign up if the user is not logged in and 'my profile' or logout if they are. There is also a menu management option if a manager is logged in.
The Shopping bag tracks and diplays items that the customer puts in the bag. It displays the total price of the items the user puts in the bag.

Beneath these features there is a horizontal row of the caegories each menu item is in. When clicked each category displays the menu items from within that category.

## Home
The home page contains a short message, a background image and a 'view menu' button which opens the menu page.

## The Sign up, Login, Logout and Password Change Pages
These pages are all part of the Django-Allauth templates which are styled to fit into the website.

## The Menu
The menu page contains a list of all items on the menu accompanied by an image and the price of each item. 

It can also be sorted into categories for a quicker and easier way for users to find what they are looking for.

When clicked each item brings the user to a seperate item description page which has a short description of the item, the feature image of the item, the price of the item and an option to add the item to the bag.  

## The Bag Page
When there are no items in the bag this page displays a short message letting the user know they have not added anything to the bag and features a return to menu button.

When items have been added to the bag it shows the details of each item, including the quantity of each item selected. It also allows the quantity of each item to be adjusted and provides a button to remove the item from the bag and a button to update the quantity. 

This page also shows the total price of all items in the bag, the cost of delivery and the grand total the customer must pay. There is also a message displaying how much more the user needs to pay to get free delivery.

Beneath these there are two buttons, one to return to menu and one to advance to the secure checkout.

## The Checkout Page
The checkout page contains an order summary on the right and a form for the user to give their details on the left. These details can be saved if the user has an account. Below the form is where they can give their payment details securely with a stripe payment element.

Beneath the payment section there are two buttons one for adjusting the bag before paying and one to complete the order. 

## Features to implement in the future:
* Add a 'How to find us' page using the google maps api.

# Technologies Used:
* This Website was built using the HTML, CSS, Javascript and Python programming languages.
*  [Gitpod](https://www.gitpod.io/) was the IDE used during the development of this project.
* [Bootstrap Cdn](https://materializecss.com/) was used to simplify the structure of the website and to easily make the website responsive.
* [Font Awesome](https://fontawesome.com/) was used to provide icons.
* [Google Fonts](https://fonts.google.com/) was used to style the website fonts.
* [JQuery](https://jquery.com/) was used when creating the stripe elements.
* [Stripe](https://stripe.com/) was used to provide payment functionality for customers.
* [Django Framework](https://www.djangoproject.com/) was the framework used for thus project. Django-allauth also provided the templates and functionality for the creation and login/out functionality of the users accounts.
* [Heroku](https://www.heroku.com) was used to host the deployed website.


# Testing
The testing information can be found in a seperate [TESTING.md](TESTING.md) file. 

# Deployment
This project was developed using [Gitpod IDE](https://www.gitpod.io/), committed to git and pushed to GitHub using the terminal.

To deploy this page to Heroku from its [GitHub repository](https://github.com/staffordcian99/brainfood), the following steps were taken:
1. Log in to heroku.
2. Create a new app.
3. Click on the deploy tab option.
4. Click on the option to connect to a github repository
5. connect to the correct github repository
6. Click to allow automatic deploys.
7. Click on deploy main branch.


At the moment of submitting this Milestone project the Development Branch and Master Branch are identical.

# Credits
## Content

* The content is all original.

## Images

* All images are from [Google](https://www.google.ie/) images.


## Code 
All code in this project is my own except bootstrap classes.

## Problems
This website was not created without it's problems, it took longer than expected to create functional stripe payments due to a problem with the form fields. The country field on the delivery address originally in the project was removed due to it being a local delivery service. Unfortunately I failed to remove the field in the JavaScript which caused the form to be invalid and the stripe payments to fail. 

Along with this there was also a problem with the select image button on the managers add item page. The select image button was positioned absolutely which caused a window to open every time the user clicked anywhere on the page. This led to the user being unable to complete the form or use the navigation links on the page. This was fixed by changing the the buttons position to relative.

On top of all of this I am aware that the project may still contain validation errors, due to time contraints all validation errors may not be resolved. If so I do certainly apologise.