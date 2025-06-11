CrawlerX is an orchestration platform for managing and executing web crawlers and API requests. It provides a RESTful API (built with FastAPI) for registering, updating, deleting, and running scripts and API calls, as well as managing logs and data recovery. The project uses SQLAlchemy for ORM and supports script uploads and execution in a controlled environment.

---

## Features

- **API Management**: Register, update, delete, and list APIs with customizable HTTP methods, headers, and parameters.
- **Script Management**: Upload, update, delete, and list Python scripts. Scripts are executed in a sandboxed environment and must return results via a `result` variable.
- **Execution Orchestration**: Run all registered APIs and scripts, with real-time progress updates via WebSocket.
- **Logging**: All requests (except GET) are logged with method, path, status code, IP, and user agent.
- **Data Storage**: Results from APIs and scripts are saved in a structured directory by date.
- **Data Recovery**: Download zipped archives of result folders for backup or analysis.
- **RESTful API**: Built with FastAPI, providing endpoints for all operations.
- **WebSocket Support**: Real-time execution feedback for orchestrated runs.

---

## Project Structure

```
crawlerx/
├── crawler_x/
│   ├── api/                # FastAPI application and route definitions
│   ├── aplication/         # Use cases for business logic
│   ├── infrastructure/     # Database and DAO infrastructure
│   ├── modules/            # Domain modules (API, script runner, logger, etc.)
│   └── service/            # Service layer (data saver, crawler manager, etc.)
├── requirements.txt
└── .gitignore
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- MySQL database (configured in sqlalchemy_session.py)
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/crawlerx.git
   cd crawlerx
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Configure the database:**
   - Edit sqlalchemy_session.py with your MySQL credentials.

4. **Run the API server:**
   ```
   python -m crawler_x.api
   ```
   The API will be available at [http://127.0.0.1:8000/v1](http://127.0.0.1:8000/v1).

---

## Usage

- **API Documentation:**  
  Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive Swagger documentation.

- **Script Upload:**  
  Upload Python scripts via the `/v1/script/file/{id}` endpoint. Scripts must define a `result` variable.

- **Run Crawler:**  
  Use the WebSocket endpoint `/v1/crawler/ws/execute` to start execution and receive progress updates.

- **Data Recovery:**  
  Download zipped result folders via `/v1/dataRecover/zip/{folder_name}`.

---

## Development

- **Add new modules** in the `modules/` directory.
- **Add new use cases** in the `aplication/` directory.
- **Unit tests** can be added in a `tests/` directory (not included by default).

---

## License

This project is licensed under the MIT License.

---

## Authors

- [Natã Nogueira Ferreira](https://github.com/nataferreiradev)
- Kauê sobreira
- Rafael de camargo neves
- Julia Zuim
- Diogo

---

## Notes

- Only `.py` files are accepted for script uploads.
- All script executions are sandboxed but use Python's `exec`—review uploaded scripts for security.
- Data and scripts are stored in the `data/` and scripts folders, which are git-ignored by default.

---

**Enjoy using CrawlerX!**
