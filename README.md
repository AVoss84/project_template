
### Install package and run application

Create conda virtual environment with required packages 
```bash
#conda env create -f environment.yml   # optionally
conda create -n proj_templ python=3.8 -y
conda activate proj_templ
```

To install the package locally, execute the following steps:

```bash
pip install -r requirements.txt         
pip install src
```

Start application locally:
```bash
uvicorn main:app --reload         # checkout docs http://127.0.0.1:8000/docs 
```

Build image and run app in container:
```bash                                 
docker-compose up -d 
```

 