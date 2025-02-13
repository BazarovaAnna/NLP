import click

from lab1.lab1 import *
from lab2.lab2 import *
from lab3.lab3 import *


@click.group()
def main():
    pass


@main.command()
@click.argument("paths", type=str)
@click.argument("pos_tags", type=bool, required=False)
def token(paths, pos_tags=False):
    lab1(paths, pos_tags)


@main.command()
@click.argument("path_t", type=str)
@click.argument("path_d", type=str)
@click.argument("path_c", type=str)
@click.argument("percent", type=int)
@click.argument("algo", type=str, required=False)
def typo(path_t, path_d, path_c, percent, algo):
    lab2(path_t, path_d, path_c, percent, algo)


@main.command()
@click.argument("train_path", type=str)
@click.argument("test_path", type=str)
@click.argument("vec_path", type=str)
@click.argument("word_count", type=int)
def vector(train_path, test_path, vec_path, word_count=1):
    fdict_file = Path(str(Path(Path.cwd()))[:-len("source")], "assets", "fdict.tsv")
    tdm_file = Path(str(Path(Path.cwd()))[:-len("source")], "assets", "tdm.tsv")
    vec = Path(str(Path(Path.cwd()))[:-len("source")], "assets", vec_path)
    lab3(train_path, test_path, vec, word_count, fdict_file, tdm_file)


if __name__ == "__main__":
    main()

