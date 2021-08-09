# Offerable - advertisements portal
CRUD application which consists of REST API based on DRF and SPA based on Angular.

## Setup

If you want to run project locally do the following:

```sh
git clone https://github.com/mateuszwwwrobel/Offerable.git
```
```sh
cd Offerable
```

Create a virtual environment and activate it:

```sh
python3 -m venv <venv-name>
```
```sh
source <venv-name>/bin/activate
```

Then simply start a pre-prepared start.sh script which will do everything for you:

```sh
(<venv-name>)$ bash start.sh
```
Note the `(venv-name)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Angular app will start automatically from script.

Navigate to `http://127.0.0.1:8000/` if you want to have a look at browsable rest api. 


### Dependencies

See requirements.txt file. 

### Running tests

In django directory run command:
```sh
(<venv-name>)$ python3 manage.py test
```

## Acknowledgments

For help with every trouble:
* [Stackoverflow](https://stackoverflow.com/)
