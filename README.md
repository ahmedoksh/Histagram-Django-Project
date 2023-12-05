# Photo Sharing Social Networking Service

This application is a photo sharing social networking service developed using Django and its ORM. It allows users to interact with each other by sharing photos and commenting on posts.

## Features

- **User Management**: Each user has a profile that can be searched by their username or name. Users can register, login, and manage their profiles.

- **Photo Management**: Users can add, edit, and delete their photos. All photos are associated with a user profile.

- **Post Management**: Users can comment on posts. They can also add, edit, and delete their comments. All relations between users, posts, and comments are maintained using Django’s ORM.

- **Containerization**: The application is containerized using Docker and Docker Compose, which simplifies deployment and scaling.

## API Endpoints

- `admin/`: Django admin site.
- `user/`: User related operations like registration, login, profile management.
- `comments/`: Operations related to comments on posts.
- `posts/`: Operations related to photo posts.

## Setup and Running

The application is containerized using Docker. To setup and run the application, use Docker Compose:

```
docker-compose up
```