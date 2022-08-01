"""
A simple app demonstrating how to manually construct a navbar with a customised
layout using the Navbar component and the supporting Nav, NavItem, NavLink,
NavbarBrand, and NavbarToggler components.
Requires dash-bootstrap-components 0.3.0 or later
"""
import os
from dash import Dash, dcc, html, Input, Output

import dash_bootstrap_components as dbc
from dash import Dash
from dash import Input, Output, State, html

# link fontawesome to get the chevron icons
FA = 'https://use.fontawesome.com/releases/v5.8.1/css/all.css'

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, FA])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '16rem',
    'padding': '2rem 1rem',
    'background-color': '#f8f9fa',
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    'margin-left': '18rem',
    'margin-right': '2rem',
    'padding': '2rem 1rem',
}

submenu_1 = [
    html.Li(
        # use Row and Col components to position the chevrons
        dbc.Row(
            [
                dbc.Col("Menu 1"),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        id="submenu-1",
    ),
    # we use the Collapse component to hide and reveal the navigation links
    dbc.Collapse(
        [
            dbc.NavLink('Page 1.1', href='/page-1/1'),
            dbc.NavLink('Page 1.2', href='/page-1/2'),
        ],
        id='submenu-1-collapse',
    ),
]

submenu_2 = [
    html.Li(
        dbc.Row(
            [
                dbc.Col("Menu 2"),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        id="submenu-2",
    ),
    dbc.Collapse(
        [
            dbc.NavLink("Page 2.1", href="/page-2/1"),
            dbc.NavLink("Page 2.2", href="/page-2/2"),
        ],
        id="submenu-2-collapse",
    ),
]

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-5"),
        html.Hr(),
        html.P(
            "A sidebar with collapsible navigation links", className="lead"
        ),
        dbc.Nav(submenu_1 + submenu_2, vertical=True),
    ],
    style=SIDEBAR_STYLE,
    id="sidebar",
)

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button("Search", color="primary", className="ml-2"),
            width="auto",
        ),
    ],
    #no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height='30px')),
                    dbc.Col(dbc.NavbarBrand('Navbar', className='ml-2')),
                ],
                align="center",
                #no_gutters=True,
            ),
            href="https://plot.ly",
        ),
        dbc.NavbarToggler(id='navbar-toggler'),
        dbc.Collapse(search_bar, id='navbar-collapse', navbar=True),
    ],
    color="dark",
    dark=True,
)

content = html.Div(id='page-content', style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id='url'), navbar, sidebar, content])


# this function is used to toggle the is_open property of each Collapse
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# this function applies the "open" class to rotate the chevron
def set_navitem_class(is_open):
    if is_open:
        return 'open'
    return ''


for i in [1, 2]:
    app.callback(
        Output(f'submenu-{i}-collapse', 'is_open'),
        [Input(f'submenu-{i}', 'n_clicks')],
        [State(f'submenu-{i}-collapse', 'is_open')],
    )(toggle_collapse)

    app.callback(
        Output(f'submenu-{i}', 'className'),
        [Input(f'submenu-{i}-collapse', 'is_open')],
    )(set_navitem_class)


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page_content(pathname):
    if pathname in ['/', '/page-1/1']:
        return html.P('This is the content of page 1.1!')
    elif pathname == '/page-1/2':
        return html.P('This is the content of page 1.2. Yay!')
    elif pathname == '/page-2/1':
        return html.P('Oh cool, this is page 2.1!')
    elif pathname == '/page-2/2':
        return html.P('No way! This is page 2.2!')
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1('404: Not found', className="text-danger"),
            html.Hr(),
            html.P(f'The pathname {pathname} was not recognised...'),
        ]
    )


# add callback for toggling the collapse on small screens
@app.callback(
    Output('navbar-collapse', 'is_open'),
    [Input('navbar-toggler', 'n_clicks')],
    [State('navbar-collapse', 'is_open')],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(port=8880, debug=True)
