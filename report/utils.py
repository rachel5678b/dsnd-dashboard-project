import pickle
from pathlib import Path

# Using the Path object, create a `project_root` variable
# set to the absolute path for the root of this project directory
project_root = Path(__file__).resolve().parent 
 
# Using the `project_root` variable
# create a `model_path` variable
# that points to the file `model.pkl`
# inside the assets directory
model_path = project_root / 'assets' / 'model.pkl'

print(f"Project Root: {project_root}")
print(f"Model Path: {model_path}")

def load_model():

    with model_path.open('rb') as file:
        model = pickle.load(file)

    return model