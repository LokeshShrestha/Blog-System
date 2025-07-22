# Django Blog System

A full-featured blog application built with Django that supports user authentication, role-based permissions, and rich content management.

## Features

### ✅ User Management
- **User Registration & Authentication**: Complete signup, login, and logout functionality
- **User Roles**: Two-tier system with Author and Reader roles
- **Profile Management**: Users can create and update their profiles with bio and profile pictures

### ✅ Blog Management
- **Full CRUD Operations**: Create, read, update, and delete blog posts
- **Rich Text Editor**: Integrated TinyMCE for enhanced content creation
- **Image Uploads**: Support for blog post images using Pillow
- **Categories & Tags**: Organize posts with categorization and tagging system

### ✅ Interactive Features
- **Comments System**: Users can comment on blog posts
- **Like System**: Users can like/unlike blog posts
- **View Tracking**: Track and display view counts for posts
- **Search Functionality**: Search through blog posts

### ✅ UI/UX
- **Rich Animated CSS**: Modern, responsive design with smooth animations
- **Responsive Layout**: Mobile-friendly design that works across devices

## Technology Stack

- **Backend**: Django 4.x
- **Database**: SQLite (default, easily configurable to PostgreSQL/MySQL)
- **Frontend**: HTML5, CSS3, JavaScript
- **Rich Text Editor**: TinyMCE
- **Image Processing**: Pillow
- **Authentication**: Django's built-in authentication system

## Project Structure

```
Basic_Blog_Site/
├── manage.py
├── db.sqlite3
├── Basic_Blog_Site/          # Main project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog/                     # Blog app
│   ├── models.py            # Blog post, comment, category models
│   ├── views.py             # Blog views and logic
│   ├── forms.py             # Blog forms
│   ├── urls.py              # Blog URL patterns
│   ├── admin.py             # Admin interface setup
│   ├── templates/           # Blog templates
│   │   ├── blog_home.html
│   │   ├── blog_details.html
│   │   ├── post_blog.html
│   │   ├── edit_blog.html
│   │   └── search.html
│   └── migrations/          # Database migrations
├── members/                  # User management app
│   ├── models.py            # User profile models
│   ├── views.py             # Authentication views
│   ├── forms.py             # Registration and login forms
│   ├── urls.py              # Member URL patterns
│   └── templates/           # Member templates
├── media/                   # User uploaded files
│   ├── blog_images/
│   └── profile_pics/
├── static/                  # Static files
│   ├── css/
│   └── images/
└── templates/               # Global templates
    ├── base.html
    └── 404.html
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- 
### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/LokeshShrestha/Blog-System.git
   cd Basic_Blog_Site
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # Add other dependencies as needed
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### For Readers
- Register an account or log in
- Browse blog posts on the home page
- Read full posts, like them, and leave comments
- Use the search functionality to find specific content

### For Authors
- Register and set your role to "Author"
- Create new blog posts with rich text content
- Upload images for your posts
- Edit or delete your existing posts
- Manage categories and tags

### For Administrators
- Access the Django admin panel
- Manage users, posts, comments, and categories
- Monitor site activity and user engagement

## Key Models

### BlogPost
- Title, content, author, category, tags
- Image upload capability
- Like and view tracking
- Publication timestamps

### Comment
- Linked to blog posts and users
- Threaded commenting support
- Moderation capabilities

### UserProfile
- Extended user information
- Profile pictures
- User role management (Author/Reader)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Future Enhancements

- Email notifications for comments
- Social media integration
- Advanced search with filters
- Blog post scheduling
- SEO optimization
- RSS feed support
- Multi-language support

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

**Developer**: Lokesh Shrestha  
**Repository**: [Blog-System](https://github.com/LokeshShrestha/Blog-System)

---

*Built with ❤️ using Django*
