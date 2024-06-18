import pandas as pd

file_name = 'banking'
# Specify the path to your Excel file
file_path = file_name + '.xlsx'

# Read all sheets into a dictionary of DataFrames
dfs = pd.read_excel(file_path, sheet_name=None)

# Specify the output markdown file path
md_file_path = file_name + '.md'
txt_file_path = file_name + '.txt'
vertices = dict()
edges = dict()

def check_and_remove_number(string):
    parts = string.rsplit('#', 1)
    if len(parts) == 2 and parts[1].isdigit():
        return parts[0]
    return string

# Open the output file in write mode with utf-8 encoding
with open(md_file_path, 'w', encoding='utf-8') as f:
    # Iterate over the dictionary of DataFrames
    for sheet_name, df in dfs.items():
        # Write the sheet name as a header
        f.write(f'# {sheet_name}\n\n')
        # Convert the DataFrame to a Markdown table
        cols = df.columns.to_list()
        rows = df.iterrows()
        if len(cols) == 1:
            col = cols[0]
            vertices[col] = []
            for index, row in rows:
                vertices[col].append(row[col])
        else:
            print(cols)
            new_cols = []
            for col in cols:
                ncol = check_and_remove_number(col)
                if ncol not in vertices:
                    vertices[ncol] = []
                if ncol in new_cols:
                    df = df.drop(columns=col)
                else:
                    df = df.rename(columns={col:ncol})
                    new_cols.append(ncol)
            #print(df)
            new_cols = tuple(new_cols)
            edges[new_cols] = []
            rows = df.iterrows()
            for index, row in rows:
                new_row = df.iloc[index].values
                edges[new_cols].append(tuple(new_row))
                for col in new_cols:
                    if(row[col] not in vertices[col]):
                        vertices[col].append(row[col])
        f.write('\n\n')

with open(txt_file_path, 'w', encoding='utf-8') as f:
    for key, value in vertices.items():
        f.write(f"\'{key}\': {value},\n")

with open(txt_file_path, 'a', encoding='utf-8') as f:
    for key, value in edges.items():
        f.write(f"{key}: {value},\n")
#print(f"Markdown tables saved to {md_file_path}")
