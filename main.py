"""
dddd
"""


from my_dash.app_table_simples import app
from my_templates.sidebar_multiple.app_template import app

server = app.server

if __name__ == '__main__':
    app.run_server(
        debug=True,
        port=8053,
    )
