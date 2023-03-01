from belgium_development_indicators import be_indicators

##  the imported variable be_indicators contains data
##  collected by the World Bank (http://data.worldbank.org/data-catalog/world-development-indicators)
##  The original data was in comma-separated values (CSV) format, and has been
##  transformed into a list of lists. The value 'None' has been given
##  to missing elements
##
##  The convention with such data is that the first row specifies
##  attribute names, and the rest contains the actual data.
## 
## The first row specifies the following attributes:
## ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code',
##  '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968',
##  '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
##  '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
##  '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
##  '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
##  '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', None]
##
## Note, all subsequent usage of the word 'matrix' refers to a list of lists,
## where each row has equal length


def indicator_names():
    """ Returns a list specifying all the instances of
        attribute 'Indicator Name' """
    indicator_name_column = column(be_indicators, be_indicators[0].index('Indicator Name'))
    return indicator_name_column[1:]


def column(matrix, i):
    """ Returns the elements in column i of the given matrix """
    return list(map(lambda x: x[i], matrix))


assert(indicator_names()[5] == 'Imports of goods, services and primary income (BoP, current US$)')

assert column([['a', 'b', 'c'], ['a', 'c', 'e'], ['a', 'e', 'i']], 1) == ['b', 'c', 'e']
 

# Looking at the data, it seems that the last element of each row is empty,
# serving as a placeholder for data from the year 2014.
# Check to make sure this column does not contain any meaningful data
def is_last_column_empty():
    """ Returns true if the last element of each row in
        the given matrix is empty (i.e. None) """
    last_column_index = len(be_indicators[0])-1
    last_column = column(be_indicators, last_column_index)
    return not has_data(last_column)


def has_data(list):
    return any(map(lambda x: x is not None, list))

assert is_last_column_empty()


def transpose(matrix):
    """ Returns the transpose of the given matrix """
    return list(map(lambda x: column(matrix, x), range(len(matrix[0]))))

assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
symmetric_matrix = [[5, 1, 3], [1, 0, 2], [3, 2, 5]]
assert transpose(symmetric_matrix) == symmetric_matrix

standard_matrix = [[1, 5, 6, 4, 2],[9, 56, 3, 1, 6],[22, 41, 5, 9, 70],[0, 44, 9, 0, 0]]
assert transpose(transpose(standard_matrix)) == standard_matrix


def select_rows(attribute, instances, matrix):
    """ Return the rows of the given matrix whose value for the given attribute
        is listed in instances """
    indicator_name_index = matrix[0].index(attribute)
    return list(filter(lambda x: x[indicator_name_index] in instances, matrix))


example_matrix = [['Name', 'Course', 'Grade'],
                  ['rebecca', 'english', 'A+'],
                  ['jim', 'computer science', 'B'],
                  ['jim', 'geography', 'A'],
                  ['kathy', 'biology', 'B+'],
                  ['jude', 'biology', 'C-']]
filtered_example_matrix = [['rebecca', 'english', 'A+'], ['jude', 'biology', 'C-']]
assert select_rows('Name', ['rebecca', 'jude'], example_matrix) ==  filtered_example_matrix



def processed_belgium_development_indicators_matrix(matrix):
    """ Returns a matrix derived from be_indicators.
        The table has 4 attributes: the first one being 'Year', and the other ones
        being the indicators listed in variable 'features_of_interest'.
        Attribute 'Year' will have as its instances all the
        years for which the other attributes hold meaningful data """
    year_1960 = matrix[0].index('1960')
    year_2013 = matrix[0].index('2013')
    filtered_row_data = select_rows('Indicator Name', features_of_interest, matrix)
    annotated_filtered_row_data = [matrix[0]] + filtered_row_data
    annual_data = list(map(lambda x: x[year_1960:year_2013], annotated_filtered_row_data))
    feature_data = transpose(annual_data)
    filtered_feature_data = list(filter(lambda x: has_data(x[1:]), feature_data))
    return [['Year'] + features_of_interest] + filtered_feature_data

features_of_interest = ['Imports of goods and services (BoP, current US$)',
                        'Exports of goods and services (BoP, current US$)',
                        'Net trade in goods and services (BoP, current US$)']

final_matrix = processed_belgium_development_indicators_matrix(be_indicators)
assert final_matrix[0][0] == 'Year'
assert final_matrix[1][3] == '285320000000'
