# SMLAlgoHub 🧠⚡

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/) [![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/) [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/) [![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/) [![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)](https://www.rabbitmq.com/) [![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com/)

## 📚 Overview

SMLAlgoHub is a comprehensive platform designed to share algorithmic knowledge and provide a competitive programming environment. The platform offers educational resources covering various algorithmic concepts, along with an integrated judging system that allows users to submit solutions to programming problems across multiple difficulty levels and categories.

The project aims to create a community-driven ecosystem where programmers can learn, practice, and compete to improve their algorithmic thinking and problem-solving skills.

## ✨ Features

### 📖 Educational Resources

- Comprehensive tutorials and explanations of common algorithms and data structures
- Visual representations and step-by-step guides for complex algorithmic concepts
- Multiple difficulty levels to accommodate learners from beginners to advanced
- Practical applications and real-world examples of algorithms

### 💻 Problem Repository

- Diverse collection of programming problems across various categories
- Tagged problems for easy filtering and search
- Multiple difficulty levels for progressive learning
- Detailed problem descriptions with input/output specifications

### ⚖️ Judging System

- Automated evaluation of submitted solutions
- Real-time feedback on code correctness and efficiency
- Support for multiple programming languages
- Comprehensive test cases for thorough verification

### 👤 User Experience

- User ranking system based on solved problems and competitions
- Personalized learning paths and recommended problems
- Progress tracking and performance analytics
- Social features for community interaction and knowledge sharing

### 🔧 Administrative Tools

- Comprehensive APIs for managing problems, tags, and user accounts
- Robust authentication and authorization system
- Analytics dashboard for monitoring platform usage and performance

## 🛠️ Technologies

### Backend

- **FastAPI** 🚀: High-performance Python web framework for building APIs
- **MongoDB** 🍃: NoSQL database for flexible data storage
- **Redis** 💾: In-memory data structure store for caching
- **RabbitMQ** 🐇: Message broker for handling submission queue
- **Firebase** 🔥: Authentication and messaging services

### Architecture

- Domain-Driven Design (DDD) architecture with simplified domain layer
- RESTful API design principles
- Containerized deployment using Docker
- Microservices approach for scalability

### DevOps

- Docker for containerization and deployment
- Koyeb for hosting and scaling
- GitHub Actions for CI/CD pipeline

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- MongoDB
- Redis
- RabbitMQ
- Firebase account

### Installation

1. Clone the repository

```bash
git clone https://github.com/Vanhoai/SMLAlgoHub.git
cd SMLAlgoHub
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Set up environment variables

```bash
cp .env.example .env
# Edit .env with your configurations
```

4. Run the application

```bash
uvicorn app.main:app --reload
```

### Docker Deployment

```bash
docker build -t smlalgohub .
docker run -p 8000:8000 smlalgohub
```

## 📚 API Documentation

Once the application is running, you can access the API documentation at:

```
http://localhost:8000/docs
```

## 📁 Project Structure

```
SMLAlgoHub/
├── app/
│   ├── domain/
│   │   ├── models/
│   │   └── repositories/
│   ├── application/
│   │   ├── services/
│   │   └── dtos/
│   ├── infrastructure/
│   │   ├── database/
│   │   ├── firebase/
│   │   ├── redis/
│   │   └── rabbitmq/
│   ├── presentation/
│   │   ├── controllers/
│   │   └── middlewares/
│   └── main.py
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📬 Contact

Project Link: [https://github.com/Vanhoai/SMLAlgoHub](https://github.com/Vanhoai/SMLAlgoHub)
