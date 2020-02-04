# Coding and chill

<img src=https://github.com/ireneisdoomed/Pipeline-project/blob/master/header.jpg alt="200" width="850"/>

This is a data analysis pipeline project to know on which platform you can find your next movie from an existing database enriched with data from other sources;and to provide recommendations accordingly.

## Input

Pre-processing of a dataset downloaded from Kaggle.com that records a number of nearly 5000 movies. The raw file is located in the input folder.

Due to computing performance by the time of applying API and scraping functions to enrich the dataframe, I decided to operate on a subset of 1000 records.

## Usage

Download the files from this repository and run the ```main.py```file in the terminal by setting its two parameters: ```--- title``` and ```---genre```.

## To-Dos:

- The executable still needs a real implementation in the terminal for the program to deliver the expected output.

- Implement the result in such a way that the program generates a PDF report that is sent as an attachment to an email address. PDF report should contain:
    - Image of the chosen film as a header.
    - Overview of the movie.
    - Rating of the movie, if exists.
    - On which platforms it is available.
    - Recommendations for other good films of that genre.

- As an improvement, it would be better to do web scraping using Selenium to reduce the number of NaN values in the Rating column.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

