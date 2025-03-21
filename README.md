# SMLAlgoHub 🧠⚡

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/) [![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/) [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/) [![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/) [![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)](https://www.rabbitmq.com/) [![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com/)

## 📚 Overview

SMLAlgoHub là một nền tảng toàn diện được thiết kế để chia sẻ kiến ​​thức thuật toán và cung cấp một môi trường lập trình cạnh tranh. Nền tảng này cung cấp các nguồn tài nguyên giáo dục bao gồm nhiều khái niệm thuật toán khác nhau, cùng với một hệ thống đánh giá tích hợp cho phép người dùng gửi các giải pháp cho các vấn đề lập trình ở nhiều cấp độ và danh mục khó khăn.

Dự án này nhằm mục đích tạo ra một hệ sinh thái do cộng đồng thúc đẩy, nơi các lập trình viên có thể học hỏi, thực hành và cạnh tranh để cải thiện tư duy thuật toán và kỹ năng giải quyết vấn đề của họ.

## ✨ Features

### 📖 Educational Resources

- Hướng dẫn và giải thích toàn diện về các thuật toán và cấu trúc dữ liệu phổ biến
- Biểu diễn trực quan và hướng dẫn từng bước cho các khái niệm thuật toán phức tạp
- Nhiều cấp độ khó để phù hợp với người học từ người mới bắt đầu đến nâng cao
- Các ứng dụng thực tế và ví dụ thực tế về thuật toán

### 💻 Problem Repository

- Bộ sưu tập đa dạng các bài toán lập trình thuộc nhiều danh mục khác nhau
- Các bài toán được gắn thẻ để dễ dàng lọc và tìm kiếm
- Nhiều mức độ khó để học tập tiến bộ
- Mô tả bài toán chi tiết với thông số kỹ thuật đầu vào/đầu ra

### ⚖️ Judging System

- Đánh giá tự động các giải pháp đã gửi
- Phản hồi thời gian thực về tính chính xác và hiệu quả của mã
- Hỗ trợ nhiều ngôn ngữ lập trình
- Các trường hợp thử nghiệm toàn diện để xác minh kỹ lưỡng

### 👤 User Experience

- Hệ thống xếp hạng người dùng dựa trên các vấn đề đã giải quyết và các cuộc thi
- Lộ trình học tập được cá nhân hóa và các vấn đề được đề xuất
- Theo dõi tiến trình và phân tích hiệu suất
- Các tính năng xã hội để tương tác cộng đồng và chia sẻ kiến ​​thức

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
- Monolithic architecture

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
