# job-search


## Configuration


[Obtain a USAJobs API Key](https://developer.usajobs.gov/APIRequest/Index) and [Sendgrid API Key](https://docs.sendgrid.com/for-developers/sending-email/api-getting-started)

Your User Agent is your email address with which you obtained your API keys. 

Then create a local ".env" file and provide the key like this:

```sh
# this is the ".env" file...

api_key="_________"
user_agent="________"
sendgrid_key="________"
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

Run the web app (opens automatically in your browser or view in the browser at http://localhost:5000/):

```sh

streamlit run -m app/Home.py

```

Navigate to [this website](https://usajobs-search.streamlit.app) to launch the app on the admin host server. 

