# 📊 Sales & Inventory Analytics Dashboard  
### Enterprise-Grade Sales, Inventory & KPI Analytics Platform


This project is a production-style full-stack application built using React (Frontend) and Django + Django REST Framework (Backend).
It is designed to track product inventory, record sales transactions, and present real-time business insights through an interactive dashboard.

The system reflects how retail, distribution, and e-commerce organizations build internal analytics platforms for operational and management decision-making.

### 🚀 Project Overview

The Sales & Inventory Analytics Dashboard provides a complete solution for:

Managing products and categories

Tracking sales across multiple channels

Monitoring inventory levels and low-stock conditions

Generating daily business KPIs asynchronously

Visualizing analytics through a React dashboard

Ensuring secure communication via JWT-protected APIs

The project emphasizes scalability, performance, and clean architecture, rather than simple CRUD functionality.



### 🏗️ High-Level Architecture
React Frontend (Analytics Dashboard)
        │
        ▼
Django REST APIs (JWT Secured)
        │
        ▼
PostgreSQL Database
(Products, Sales, KPIs)
        │
        ▼
Celery Workers + Redis
(Async Analytics & Alerts)

### ⚙️ Tech Stack
Frontend

React

REST API integration

Chart-based data visualization

JWT-based authentication handling

Backend

Django

Django REST Framework

PostgreSQL

Celery (asynchronous processing)

Redis (caching & message broker)

JWT authentication

Deployment Ready

Gunicorn & Nginx compatible

AWS EC2 friendly

CI/CD-ready structure

### 🧩 Key Features
🎨 React Analytics Dashboard

Displays business KPIs in real time

Visualizes sales trends and top-selling products

Highlights low-stock inventory items

Communicates securely with backend APIs

Designed for management and analyst use cases

### 🔐 Authentication & Security

JWT-based authentication

Secure API communication between frontend and backend

Easily extendable to role-based access control

### 📦 Product & Inventory Management

Centralized product and category management

Tracks stock quantities and reorder levels

Supports warehouse/location metadata

Automatically updates inventory on sales

### 💰 Sales Tracking

Records all sales transactions

Supports multiple sales channels (online/offline)

Maintains historical sales data for analytics

### 📈 Analytics & KPI Engine

Generates daily business KPIs asynchronously

Metrics include:

Total revenue

Total orders

Average order value

Top-selling products

Low-stock item count

Designed to support future trend analysis (weekly/monthly)

### ⚙️ Background Processing

Heavy analytics tasks handled outside API requests

Prevents performance bottlenecks

Scheduled background jobs for reporting and monitoring

### 🚀 Performance Optimization

Redis caching for frequently accessed analytics

Reduced database load for dashboard requests

Faster response times for high-traffic endpoints

### 🚨 Inventory Alerts

Automatically detects low-stock products

Exposes alert data via APIs

Easily extendable to email or notification systems

### 🔗 API Usage

The frontend consumes REST APIs to:

Authenticate users

Fetch dashboard KPIs

Display top-selling products

Monitor inventory alerts

Record sales transactions

All API communication is secure and token-based.

### 🧰 Project Structure (Overview)
sales_inventory_dashboard/
│
├── frontend/   # React analytics dashboard
├── backend/    # Django + DRF backend
├── requirements.txt
└── manage.py

### 🧪 Testing Strategy

Backend unit testing for business logic

API integration testing

Validation of background task execution

Designed to support realistic data volumes

### ☁️ Deployment Readiness

Structured for cloud deployment

Supports PostgreSQL and Redis in production

Backend compatible with Gunicorn & Nginx

Frontend ready for static build deployment

### 👨‍💻 Author

Dillip Kumar Singh
Backend / Full-Stack Python Developer
Django • DRF • React • PostgreSQL • Celery • Redis
