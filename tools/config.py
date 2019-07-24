from pathlib import Path

PROJECT_DIR = Path(__file__).parents[1].absolute()
PRON_DATA_DIR = PROJECT_DIR / 'pron_data'

PRON_TRAIN_FILE = PRON_DATA_DIR / 'gold_data_train'
PRON_TEST_FILE = PRON_DATA_DIR / 'gold_data_test'
