# djangoproject

### Project Setup
### Step 1: Create a virtual environment named venv
```bash
python3 -m venv venv
```

![alt text](resources/image-2.png)

### Step 2: Activate the virtual environment
```bash
source venv/bin/activate
```

![alt text](resources/image-3.png)

### Step 3: Install Django using uv
```bash
uv pip install Django
```
![alt text](resources/image-4.png)

### Step 4: Create Django Project named djangoproject
```bash
django-admin startproject simple-django-project 
```
![alt text](resources/image-5.png)

### Step 5: Go to djangoproject directory
```bash
cd djangoproject/
```

### Step 6: Run the project
```bash
python manage.py runserver
```
![alt text](resources/image-1.png) </br>
![alt text](resources/image.png)

### Step 7:  Create an app named products
```bash
python manage.py startapp products
```

### Step 8: Add products app in djangoproject settings
![alt text](resources/image-6.png)

## Add Tailwind 
```bash
uv pip install django-tailwind
uv pip install 'django-tailwind[reload]'
```


### Resources:
1.  https://docs.astral.sh/uv/getting-started/installation/#next-steps
2. https://www.djangoproject.com/start/
3. https://jinja.palletsprojects.com/en/stable/
4. https://pypi.org/project/django-tailwind/