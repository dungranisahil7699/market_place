# Django Marketplace Project

## Overview

This project is a Django-based online marketplace API where users can buy and sell products. It includes features such as user management, product management, purchase handling, and product listings.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [User Management](#user-management)
  - [Product Management](#product-management)
  - [Purchase Handling](#purchase-handling)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Bonus Features](#bonus-features)

## Getting Started

### Prerequisites

- Python 3.8+
- Django
- Django Rest Framework
- SQLite3 or PostgreSQL
- AWS S3 (for image storage)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/marketplace-project.git

2. Create and activate a virtual environment:

    ```bash
    cd marketplace-project
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate

3. Install dependencies:

    ```bash
    pip install -r requirements.txt

4. Apply database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate


## Configuration

Update the project settings in settings.py with your specific configurations:

- AWS S3 credentials for image storage
- Django Rest Framework settings
- Database settings (SQLite3 or PostgreSQL)

## User Management

- User Registration: 
    ```bash 
    Endpoint: '/api/register/'
    Method: 'POST'
    Parameters: 'username', 'email', 'password', 'phone_number'

- User Login: 
    ```bash 
    Endpoint: '/api/auth/login/'
    Method: 'POST'
    Parameters: 'username', 'password'

## Product Management

- Add Product: 
    ```bash 
    Endpoint: '/api/products/'
    Method: 'POST'
    Parameters: 'name', 'description', 'price', 'image'(upload image file), 'seller'

- List Products: 
    ```bash 
    Endpoint: '/api/products-list/'
    Method: 'GET'

## Purchase Handling

- Create Purchase:
    ```bash 
    Endpoint: '/api/purchase/'
    Method: 'POST'
    Parameters: 'product', 'seller', 'buyer', 'purchase_price'

## All Endpoints
- User registration : /api/register/
- User login : /api/auth/login/
- Add product : /api/products/
- List products : /api/products-list/
- Create purchase : /api/purchase/

## Testing
Run the tests to ensure that the API functions correctly:

    python manage.py test

## Bonus Features
- Pagination:
    - Products are paginated on the /api/products-list/ endpoint.
- Image Storage:
    - Product images are stored on AWS S3. Store Image locally If bucket is not available.