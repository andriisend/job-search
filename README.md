# job-search


## Configuration


[Obtain an API Key](https://developer.usajobs.gov/APIRequest/Index) from USAJobs.

Then create a local ".env" file and provide the key like this:

```sh
# this is the ".env" file...

api_key="_________"
```
## Setup

Create and activate a virtual environment:

```sh
conda create -n jobsearch-env python=3.8

conda activate jobsearch-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage



Run an example script:

```sh
#python app/my_script.py
```

Run a job search report 

```sh
#python app/stocks.py
python -m app.jobsearch
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```
