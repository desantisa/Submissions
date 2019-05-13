from zillow_scraper import zillow_data
from trulia_scraper import trulia_data
from realtor_scraper import realtor_data
from historical_scraper import historical_data
from media_maker import plot_map, plot_historical, create_table
from flask import Flask, render_template, request
from bokeh.embed import components
import pandas as pd


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    zipcode = request.form.get('zipcode', '03049')

    df_zillow  = zillow_data(zipcode)
    df_trulia  = trulia_data(zipcode)
    df_realtor = realtor_data(zipcode)
    df_historical = historical_data(zipcode)


    p_map = plot_map(zipcode, df_zillow)

    p_hist = plot_historical(df_historical)

    script_map, div_map = components(p_map)
    script_hist, div_hist = components(p_hist)

    df = create_table(df_zillow, df_trulia, df_realtor)

    return render_template('index.html', script_map=script_map, div_map=div_map,
                           script_hist=script_hist, div_hist=div_hist,
                           table=df.to_html(), zipcode_val=zipcode)



if __name__ == '__main__':
    app.run(port=5000, debug=True)
