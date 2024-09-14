# Project Documentation for Microblog

## Overview

Microblog is a Flask-based blogging platform developed as part of the Flask Mega-Tutorial. This application allows users to register, log in, create, edit, and delete blog posts, and follow other users. It includes authentication, post management, and a user-following system.

## Functionality

### Models

#### User

- **`User`**: Represents a user in the system.
  - **Fields**: `id`, `username`, `email`, `password_hash`, etc.
  - **Methods**:
    - **`set_password(password)`**: Hashes and sets the user's password.
    - **`check_password(password)`**: Checks if the provided password matches the stored hash.

#### Post

- **`Post`**: Represents a blog post.
  - **Fields**: `id`, `title`, `content`, `timestamp`, `author_id`, etc.
  - **Methods**:
    - **`save()`**: Saves the post to the database.
    - **`delete()`**: Deletes the post from the database.

### Views and Routes

#### Main Views

- **`index`**:
  - **Description**: Displays a list of blog posts.
  - **URL**: `/`
  - **Methods**: `GET`

- **`post`**:
  - **Description**: Displays a single blog post.
  - **URL**: `/post/<id>`
  - **Methods**: `GET`

- **`profile`**:
  - **Description**: Displays a user’s profile and their posts.
  - **URL**: `/user/<username>`
  - **Methods**: `GET`

#### API Endpoints

- **`/api/posts`**:
  - **Description**: Manages blog posts through the API.
  - **Methods**: `GET`, `POST`, `PUT`, `DELETE`

- **`/api/users`**:
  - **Description**: Manages user accounts through the API.
  - **Methods**: `GET`, `POST`, `PUT`, `DELETE`

### Forms

#### RegistrationForm

- **Fields**:
  - `username`: User's desired username.
  - `email`: User's email address.
  - `password`: User's chosen password.

- **Methods**:
  - **`validate()`**: Ensures all required fields are filled out and valid.

#### PostForm

- **Fields**:
  - `title`: Title of the blog post.
  - `content`: Content of the blog post.

- **Methods**:
  - **`validate()`**: Ensures that the title and content are not empty.

## Implementation Details

### Task Creation

Tasks such as creating blog posts or user accounts are managed through forms and views. For instance, creating a post involves filling out the `PostForm` and submitting it to the `post` view, which then handles saving the post to the database.

### Task Listing

Blog posts are listed on the homepage (`index` view), which queries the `Post` model and passes the data to the template for rendering.

### Task Update

Blog posts and user profiles can be updated through forms provided in the application. The respective views handle form submissions and update the database.

### Task Deletion

Tasks or blog posts are deleted through specific actions in the application, such as clicking a delete button, which triggers a request to the corresponding view to remove the item from the database.

## Code Example

Here’s a snippet from `views.py` showing how post creation is handled:

```python
from flask import render_template, redirect, url_for
from app import app
from app.models import Post
from app.forms import PostForm

@app.route('/post/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        post.save()
        return redirect(url_for('index'))
    return render_template('post_form.html', form=form)
