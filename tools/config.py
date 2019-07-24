from pathlib import Path

PROJECT_DIR = Path(__file__).parents[1].absolute()
PRON_DATA_DIR = PROJECT_DIR / 'pron_data'
IPA_HELP_DIR = PROJECT_DIR / 'ipa_help'

PRON_TRAIN_FILE = PRON_DATA_DIR / 'gold_data_train'
PRON_TEST_FILE = PRON_DATA_DIR / 'gold_data_test'

IPA_HELP_FILE = IPA_HELP_DIR / 'all.g-to-ipa.cleaned.table'
