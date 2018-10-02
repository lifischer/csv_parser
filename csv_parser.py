import matplotlib.pyplot as plt 
import pandas as pd
import sys
import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('filename')
def display(filename):
    """Display the column names and their data type."""
    df = pd.read_csv(filename)
    print(df.dtypes)
    
@cli.command()
@click.argument('filename')   
@click.option('--column', default=None, help='Name of column to plot. If not used, all will be plotted.')
def plot(filename, column):
    """Plots a histogram of a column of their data type."""
    df = pd.read_csv(filename)
    if column is None:
        df.hist()
    else:
        df[Column].hist()
        plt.title(column)
        plt.ylabel('frequency')
    plt.show()

#type python csv_parser.py oktoberfestgesamt1...


#if __name__ == '__main__':
 #   cli()
    

        