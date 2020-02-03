import argparse

def get_settings():
    parser = argparse.ArgumentParser(description="Find out on which platform to watch your favorite movie or find the best match according to the genre you want.")
    parser.add_argument('--title', type = str, help='Name of the movie you want to look up.')
    parser.add_argument('--genre', type = str, help='Name of the film genre you want to find.')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    #aquí pongo mis funciones que quiero que salgan