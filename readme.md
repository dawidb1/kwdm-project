# Temat 

Internetowa stacja wspomagania segmentacji obrazów medycznych

# Cel projektu

Celem projektu jest stworzenie aplikacji webowej, która umożliwi wsparcie dla personelu medycznego w segmentacji obrazów medycznych pacjentów

# Repo

- webapp (Vue.js)
- orthanc (API do obrazów z pacsa)
- webapi (.NET - logowanie/rejestracja)
- segmentationapi (python - segmentacja)

# Docker
First use:
`docker-compose up --build`
Next use:
`docker-compose up`

## only orthanc 
`docker build -t orthanc:latest .`
`docker run -p 8042:8042 orthanc`

## only webapp
`docker build -t webapp:latest .`
`docker run -p 8080:8080 webapp`
