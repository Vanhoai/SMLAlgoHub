# Changelog

## Unreleased

### Added

- Add redis cache support for caching data
- Add rabbitmq for message queue when submit solution to judge
- Write api for manage submission

## March 19, 2025 - Pull Request [https://github.com/Vanhoai/SMLAlgoHub/pull/2]

### Added

- Set up Dockerfile for deployment to koyeb
- Write api for manage problem, tag and account not not finished
- Add middleware for authentication and authorization (RoleMiddleware, AuthMiddleware)
- Use pipeline for query aggregate problem
- Integrate firebase for authentication and messaging
- Add TimeHelper for get time zone (UTC, Asia/Ho_Chi_Minh)
- Add README.md file for project

### Refactored

- Refactor code response json use JSONResponse and jsonable_encoder instead of return
- Refactor BaseRepository in method create, update, get for return id with type string instead of ObjectId
- Remove singleton class in main file and create app without class

## March 11, 2025 - Pull Request [https://github.com/Vanhoai/SMLAlgoHub/pull/1]

### Added

- Init project with fast api python
- Set up domain driven design architecture but remove unnecessary in domain (remove domain service)
- Set up connection mongodb database and binding to document model
- Write base repository and use depend in fast api for set up dependencies
