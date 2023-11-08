# bdd_20231108
Tech Radar BDD Repo

## Workshop Setup
### Setup virtualenv

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install packages

```bash
pip install -r requirements.txt
```

## Workshop 1: Execute Behave

To execute

```bash 
behave --tags=@basic
```

## Workshop 2: Scenario Outline

1. To link
```bash
ln -s features/calculator_scenario_outline._feature features/calculator_scenario_outline.feature
`````
2. Run
```bash 
behave
```
3. Task: Fix failing tests


## Reference:

Behave tutorial:

https://behave.readthedocs.io/en/stable/tutorial.html

Behave tags: 

https://jenisys.github.io/behave.example/tutorials/tutorial11.html


