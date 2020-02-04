#!/usr/local/bin/python3

import argparse
import src.functions as f
#import src.Data_cleaning
import pandas as pd

def get_settings():
    parser = argparse.ArgumentParser(description="Find out on which platform to watch your favorite movie or find the best match according to the genre you want.")
    parser.add_argument('--title', type = str, help='Name of the movie you want to look up.')
    parser.add_argument('--genre', type = str, help='Name of the film genre you want to find.')
    args = parser.parse_args()
    return args


def main():
    config = get_settings()
    import src.functions as f
    df = pd.read_csv('./output/thousandRecords.csv')
    f.whereisit(args.title)
    
    




if __name__ == '__main__':
    main()