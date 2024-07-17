# CollabDoc: Collaborative Document Editing Platform
Welcome to the CollabDoc! This application allows users to collaboratively edit documents in real-time, providing features like user authentication, document sharing, and real-time notifications.

## Features
- User Authentication: Sign up, log in, and manage your profile securely.
- Google Authentication: Log in using your Google account for added convenience.
- Real-Time Collaboration: Multiple users can edit the same document simultaneously with changes reflected in real-time.
- Document Sharing: Share documents privately or publicly with secure access codes.
- Notifications: Receive notifications when someone gets access to your document or when there are changes.
- User Profiles: Customize your profile with avatars and manage your account settings.
- Document Management: View, create, edit, and manage documents easily with sorting and filtering options.

## Technologies Used

### Backend
- Django: The web framework used for building the backend of the application.
- Django Rest Framework (DRF): For creating RESTful APIs.
- PostgreSQL: The database for storing user and document data.
- Redis: Used as the message broker for Celery tasks.
- Celery: For handling asynchronous tasks like sending email notifications.
- Channels: For real-time features using WebSockets.
- Django Allauth: For handling authentication, including Google OAuth.
- Django Rest Auth: Provides endpoints for user registration and authentication.

### Frontend
- React: The web framework used for building the frontend of the application.

