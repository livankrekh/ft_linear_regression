# ft_linear_regression

Project for training linear models (with multiple features) and predict by trained model

![vizualizing](https://drive.google.com/uc?authuser=0&id=1uOPjDWVq4NDc_4pYvXE5OSlleY6S1LNx&export=download)

## Install and run

```
> ./install.sh
> ./train.py args...
> ./predict.py args_for_predict...
```
OR
```
(venv) > pip3 install -r requirements.txt
(venv) > python3 train.py args...
(venv) > python3 predict.py args_for_predict...
```

## Usage

### train.py

* `path/to/file.csv` - first argument, path to dataset file in csv format
* `-p` - flag to show precision value on every iteration
* `-v` - flag to vizualize trained model with dataset and cost function iterations
* `--alpha=0.01` - get learning rate value to 0.01
* `--iter=1000` - get maximum iterations value to 1000

### predict.py

This script run in format
```
> ./predict.py arg1 arg2 arg3 arg4...
```
`arg1 arg2 arg3 arg4...` - are real numbers. They are feature set
