# Django App Setup and Run Instructions

This guide will walk you through the steps to set up and run a Django app locally.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- Python 3.x
- `virtualenv` (for creating a virtual environment)

## Setup

```bash
# 1. Clone the repository:
git clone <repository_url>
cd <repository_directory>

# 2. Create a virtual environment (recommended):
python -m venv venv

# 3. Activate the virtual environment:
# On Windows:
venv\Scripts\activate
# On macOS and Linux:
source venv/bin/activate

# 4. Install project dependencies:
pip install -r requirements.txt

# 5. Apply database migrations:
python manage.py migrate

# 6. Run django app on local server (default PORT 8000):
python manage.py runserver
