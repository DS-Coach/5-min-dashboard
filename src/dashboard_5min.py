from pathlib import Path
from datetime import datetime as dt

import click
import pandas as pd
from pandas_profiling import ProfileReport


def load_dataset(filepath: str, ) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    return df


def profiling(df: pd.DataFrame, title: str="sales", 
              project_path: Path=Path("./"), 
              minimal: bool=False) -> None:
    """
    Creates a 5-minute dashboard.
    """
    today = dt.now().strftime("%Y-%m-%d")
    profile = ProfileReport(df, title=title.title(), minimal=minimal)
    profile.to_file(project_path.joinpath(f"5_min_dashboad_{title}_{today}.html")) 


@click.command()
@click.option("-f", "--filepath", default=None, type=str, required=True)
@click.option("-t", "--title", default="sales", type=str)
@click.option('-m', '--minimal', is_flag=True, default=False)
@click.option('-s', '--sample', default=None, type=float)
def main(filepath, title, minimal) -> None:
    df = load_dataset(filepath)
    profiling(df, title=title,  minimal=minimal)


if __name__ == '__main__':
    main()
