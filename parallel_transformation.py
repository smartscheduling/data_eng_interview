import multiprocessing
import pandas as pd
import math


"""
Write an implementation of the function parallel_transform().

Import and use any appropriate standard library modules, and also pandas and numpy if necessary.

parallel_transform() should apply a transformation to an input dataset in parallel,
and write out the transformed data to an output file. The degree of parallelism should be
the number of cores on the machine. parallel_transform should correctly work when the size
of the input dataset is much too large to fit in memory.

Input parameters:
    transformer: a callable that takes a pandas DataFrame, transforms it, and returns a new DataFrame
    input_csv: a filename with the location of the input csv file
    output_csv: a filename with the intended location of the transformed csv file
    group_by_column (optional): an optional column name. If specified, groups of this column must be
                                kept intact when partitioning for parallel execution

Optional extras:
    1. parallel_transform should correctly raise and log errors that happen when calling transformer() in parallel.
    2. Add an optional argument group_by_column=None which specifies a column name to group by for the partitions.

"""

def parallel_transform(transformer, input_csv, output_csv):
    pass

if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import os
    test_df = pd.DataFrame()
    test_df['a'] = np.arange(10000)
    test_df['b'] = 'abcdefghi'
    test_df['c'] = pd.to_datetime('now')
    test_df['d'] = 432
    test_df.loc[(test_df['a'] % 2 == 0), 'd'] = 333

    def transformer1(df):
        new_df = df.copy()
        new_df['a'] = new_df['a'] * 2
        return new_df

    def transformer2(df):
        return df.head(100)

    def transformer3(df):
        raise Exception('Something went wrong')


    input_file = 'input.csv'
    try:
        os.remove(input_file)
    except:
        pass

    test_df.to_csv(input_file)

    for output_file in ['output1.csv', 'output2.csv', 'output3.csv', 'output4.csv']:
        try:
            os.remove(output_file)
        except:
            pass
    
    parallel_transform(transformer1, input_file, 'output1.csv')
    parallel_transform(transformer2, input_file, 'output2.csv')
    parallel_transform(transformer3, input_file, 'output3.csv')
    parallel_transform(transformer1, input_file, 'output4.csv', group_by_column='d')
