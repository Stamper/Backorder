# Backorder
Backend for orders/invoices

### Requirements
- python 3.10
- `$ pip install -r ./requirements/base.txt`

### DB population
- `$ python ./src/manage.py migrate`
- `$ python ./src/manage.py createsuperuser`
- `$ python ./src/manage.py syncdata products.yaml`

### Run server
`$ python ./src/manage.py runserver`

### Admin dashboard
Login to [admin dashboard](http://127.0.0.1:8000/admin) with superuser credentials

### API endpoints
Visit [Swagger](http://127.0.0.1:8000/api/docs)

### Tests
- `$ pip install -r ./requirements/dev.txt`
- `$ PYTHONPATH=./src pytest`