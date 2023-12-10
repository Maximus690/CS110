from byu_pytest_utils import test_files, max_score, this_folder
from test_quote_chooser_utils import run_script


@max_score(5)
def test_quotes():
    quotes = set()

    quotes_file = test_files / 'quotes.txt'
    quote_lines = quotes_file.read_text().splitlines()

    for rep in range(100):
        result, _ = run_script(this_folder / 'quote_chooser.py', quotes_file)
        quote = '|'.join([line.strip('\n') for line in result]).replace('\n', '|')
        assert quote in quote_lines
        quotes.add(quote)

    assert len(quotes) == 5
