# https://stackoverflow.com/questions/65656053/plotly-dash-how-to-filter-dashboard-with-multiple-dataframe-columns


import pandas as pd
from dash import Dash, html, dcc
from dash import Dash, dcc, html, Input, Output

data = {'Investor': {0: 'Rick', 1: 'Faye', 2: 'Rick', 3: 'Dre', 4: 'Faye', 5: 'Mike', 6: 'Mike', 7: 'Mike'},
        'Fund': {0: 'Fund 3', 1: 'Fund 2', 2: 'Fund 3', 3: 'Fund 4', 4: 'Fund 2', 5: 'Fund 1', 6: 'Fund 1',
                 7: 'Fund 1'},
        'Period Date': {0: '2019-06-30', 1: '2015-03-31', 2: '2018-12-31', 3: '2020-06-30', 4: '2015-03-31',
                        5: '2015-03-31', 6: '2018-12-31', 7: '2018-12-31'},
        'Symbol': {0: 'AVLR', 1: 'MEG', 2: 'BAC', 3: 'PLOW', 4: 'DNOW', 5: 'JNJ', 6: 'QSR', 7: 'LBTYA'},
        'Shares': {0: 3, 1: 11, 2: 10, 3: 2, 4: 10, 5: 1, 6: 4, 7: 3},
        'Value': {0: 9, 1: 80, 2: 200, 3: 10, 4: 100, 5: 10, 6: 20, 7: 12}}
df = pd.DataFrame.from_dict(data)


def generate_table(dataframe, max_rows=100):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


app = Dash()
app.layout = html.Div(
    children=[
        html.H4(children='Investor Portfolio'),
        dcc.Dropdown(
            id='dropdown',

            # Extend the options to consider unique Fund values as well
            options=(
                    [{'label': i, 'value': i} for i in df['Investor'].unique()] +
                    [{'label': i, 'value': i} for i in df['Fund'].unique()]
            ),
            multi=True,
            placeholder='Filter by Investor or Fund...'
        ),
        html.Div(id='table-container'),

    ]
)


@app.callback(
    Output('table-container', 'children'),
    [Input('dropdown', 'value')]
)
def display_table(dropdown_value):
    if dropdown_value is None:
        return generate_table(df)

    ## add an 'or' condition for the other column you want to use to slice the df
    ## and update the columns that are displayed
    dff = df[df.Investor.str.contains('|'.join(dropdown_value)) | df.Fund.str.contains('|'.join(dropdown_value))]
    dff = dff[['Investor', 'Fund', 'Period Date', 'Symbol', 'Shares', 'Value']]
    return generate_table(dff)




if __name__ == '__main__':
    app.run_server(
        debug=True,
        port=8053,
    )
