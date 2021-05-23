# Learning Django

## Description

Introduction to Django developing a project called wisdompets

## Usage

You can clone all the repo with the following command:

```Shell
    git clone --depth 1 https://github.com/oimoralest/django.git
```

Next go to the wisdompets project using the following command:

```Shell
    cd django/learning_django/wisdompets/
```

Install the requeriments with the following command:

```Shell
    pip3 install -r requeriments.txt
```

Apply migrations running the following commands:

```Shell
    python3 manage.py migrate
```

You can add some data to the database running the following command:

```Shell
    python3 manage.py load_pet_data
```

Finally, run the the server with the following command:

```Shell
    python3 manage.py runserver
```

Now you can use your favorite web browser and visit to the following URL to enjoy the app:

<http://localhost:8000/>

### Using admin tool

To use the admin endpoint, Firts you need to create a superuser.

To create a superuser run the following command and fill the requested information:

```Shell
    python3 manage.py createsuperuser
```

Run the server and go to the following URL and make use of admin tools:

<http://localhost:8000/admin>

## Learned concepts

### Models and Admin

In this section I learned to:

- Create models
- Makemigrations, migrate and showmigrations
- Use admin site
- Make queries

#### Implemented Models

```Python
    class Pet(models.Model):
        '''Defines a Pet Schema'''
        SEX_CHOICE = [
            ('M', 'Male'),
            ('F', 'Female')
        ]
        name = models.CharField(max_length=100)
        submitter = models.CharField(max_length=100)
        species = models.CharField(max_length=30)
        breed = models.CharField(max_length=30, blank=True)
        description = models.TextField(blank=True)
        sex = models.CharField(max_length=1, choices=SEX_CHOICE, blank=True)
        submission_date = models.DateField()
        age = models.IntegerField(null=True)
        vaccinations = models.ManyToManyField('Vaccine', blank=True)

        class Meta:
            '''Defines Metadata for Pet'''
            db_table = 'pets'


    class Vaccine(models.Model):
        '''Defines a Vaccine Schema'''
        name = models.CharField(max_length=50)

        def __str__(self) -> str:
            return self.name
```

#### Registering the models for the admin site

```Python
    @admin.register(Pet)
    class PetAdmin(admin.ModelAdmin):
        pass
```

#### Using Django shell

To use the Django shell we run the following command:

```Shell
    python3 manage.py shell
```

This will run the python shell with DJANGO_SETTINGS_MODULE enviroment variable

#### References for Models and Admin

- [MVC Architecture](https://www.guru99.com/mvc-tutorial.html)
- [Models](https://docs.djangoproject.com/en/3.2/topics/db/models/)
- [Migrations](https://docs.djangoproject.com/en/3.2/topics/migrations/)
- [Custom django-admin command](https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/)
- [Admin site](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/)
- [Making queries](https://docs.djangoproject.com/en/3.2/topics/db/queries/)

### URL Handlers and Views

In this section I learned to:

- Implement a view for a specific endpoint

#### Implemented URLs

- Home: <http://localhost:8000/>
- Pet detail: <http:/localhost:8000/adoptions/<int:pet_id>>

#### References for URL Handlers and Views

- [URL configs](https://docs.djangoproject.com/en/3.2/topics/http/urls/)
