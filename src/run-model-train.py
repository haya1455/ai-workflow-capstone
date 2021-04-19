import os 
from src.model import model_train, model_load
from src.config import DATA_DIR

def main():
    
    data_dir = os.path.join(DATA_DIR, "cs-train")
    
    ## train the model
    model_train(data_dir ,test=False)

    ## load the model
    model = model_load()
    
    print("model training complete.")


if __name__ == "__main__":

    main()
