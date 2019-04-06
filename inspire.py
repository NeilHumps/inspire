import os

from random import randint

def quotes_cleanup():
    work_dir = os.path.split(os.path.realpath(__file__))[0]
    quotes_clean = []
    with open(os.path.join(work_dir, 'data/quotes_clean.txt'), 'w') as output_fh:
        with open(os.path.join(work_dir, 'data/quotes_raw.txt')) as input_fh:
            for line in input_fh:
                if line.strip():
                    quote_list = line.strip().split('.', 1)
                    if len(quote_list) == 2:
                        quote = quote_list[1].replace('\xe2\x80\x94', '-')
                        quote = quote.replace('\xe2\x80\x94', '-')
                        output_fh.write(quote + '\n')


def get_quote():
    work_dir = os.path.split(os.path.realpath(__file__))[0]
    with open(os.path.join(work_dir, 'data/quotes_clean.txt')) as input_fh:
        quotes = [i.strip() for i in input_fh.readlines()]
    print(quotes[randint(0, len(quotes) - 1)])


if __name__ == '__main__':
    quotes_file = os.path.join(
        os.path.split(os.path.realpath(__file__))[0],
        'data/quotes_clean.txt',
    )
    if not os.path.exists(quotes_file):
        quotes_cleanup()
    get_quote()

