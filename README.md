# Demo Brand Page with E-Commerce

A demo e-commerce platform built with Django and Tailwind CSS.

## Features

- Product catalog with PostgreSQL database
- Shopping cart with session cookies
- Responsive design 
- Clean, component-based templates

## Requirements

- Python 3.8+
- PostgreSQL
- Node.js (for Tailwind CSS)

## Setup

1. Clone the repository
2. Create and activate virtual environment
3. Install requirements:
```
  pip install -r requirements.txt
  
  // Install Node.js (https://nodejs.org/) then:
  
  // Install Tailwind and dependencies
  npm install -D tailwindcss postcss autoprefixer
  npx tailwindcss init
  
  // Create CSS file (in shop1django/static/css/tailwind.css)
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
  
```
4. Set up environment variables in `.env`
5. Run migrations: `python manage.py migrate`
6. Start development server: `python manage.py runserver`

## Development

- Tailwind CSS: `npm run build` (watches for changes)
- Admin interface: `/admin` (create superuser first)
