---
id: uv_intro
title: UV Python Package Manager
---

## **UV commands**

- To find all avaiable option use
    ```python
    uv --help
    ```
- Startup the Project
    ```python 
    uv init --python 3.12 projectname
    ```
    
- Intall the package
   ```python
   uv add packagepages
   ```
- To sync the project with dependency
    ```python
    uv sync
    ```
- for adding the developement dependencies
    ```python
    uv add ruff pytest --dev
    ```
- Running Script file    
    - Running standalone or script file i.e without venv with few dependenies
        ```python
        uv run --with requests filename.py
        ```
    - If more dependencies are there then generate python inline script
        ```python
        #Generate the inline script in the python file
        uv run --script filename.py 'package names'
        # then you can run the python file
        uv run filename.py
        ```
## **Ruff commands**


- To check the Errors on all the folders and files then use 
    ```python
    # if you dont have pyproject.toml then use  
    # this will create temp virtual env internally
    uvx ruff check filename
    # else
    uv run ruff check 
    ```

- To check perticular file then 
    ```python
    uv run ruff check filepath/filename.py
    ```

- To Fix error use
    ```python
    uv run ruff check --fix
    ```

- For formatting use
    ```python
    uv run ruff format
    ```
    






