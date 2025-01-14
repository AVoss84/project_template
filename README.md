# Template for generic Python package (Data Science) 

This is a blueprint of a generic end-to-end data science project, i.e. building a Python package along the usual steps: data preprocessing, model training, prediction, postprocessing, REST API construction (for real-time model serving) and containerization for final deployment as a microservice.

## Package structure

```
├── CHANGELOG.md
├── Dockerfile_Fastapi       # vanilla rest api image
├── Dockerfile_Streamlit     # vanilla streamlit image
├── README.md
├── deploy2aws.sh            # build image and push to AWS ECR
├── docker-compose.yaml
├── logs
├── main.py                  # REST API definition 
├── requirements.txt
├── setup.py
├── src
│   ├── my_package
│   │   ├── config
│   │   │   ├── config.py
│   │   │   ├── global_config.py
│   │   │   └── input_output.yaml
│   │   ├── resources
│   │   │   ├── postprocessor.py
│   │   │   ├── predictor.py
│   │   │   ├── preprocessor.py
│   │   │   └── trainer.py
│   │   ├── services
│   │   │   ├── file.py
│   │   │   ├── file_aws.py
│   │   │   ├── pipelines.py
│   │   │   └── publisher.py
│   │   └── utils
│   │       └── utils.py
│   └── notebooks
└── streamlit_app.py 
```

## Use Case description

**Business goal**: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

**Business stakeholders**: Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

**Input data description**: Iris data set

**Business impact KPI**: Faster STP (in hours/days)


## Package installation and application develoment

Create virtual environment with required packages 
```bash
uv venv env_mid --python 3.12
source env_mid/bin/activate
```

To install the package locally execute the following steps:

```bash
uv pip install -r requirements.txt
# pip install -r requirements.txt  
```

Start REST API locally:
```bash
uvicorn main:app --reload         # checkout Swagger docs: http://127.0.0.1:8000/docs 
```

Start Streamlit app locally:
```bash
streamlit run streamlit_app.py         
```

Build image and run app in container:
```bash                                 
docker-compose up -d 
```

 
