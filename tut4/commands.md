# Ogólnie

## Gunicorn

```
gunicorn <wsgi_callable> [--reload] [params]

```

## HTTPie

```
http <method> <url> [params]
```

# W naszym przypadku

## Gunicorn
```
gunicorn images_api --reload
```

## HTTPie


#### Postowanie obrazka
```
http POST localhost:8000/v1/images Content-Type:image/jpeg < path_do_pliku
```
