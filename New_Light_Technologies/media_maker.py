from uszipcode import SearchEngine
from bokeh.models import (ColumnDataSource, GMapOptions, HoverTool,
                          WheelZoomTool, PanTool, BoxZoomTool, GMapPlot,
                          Range1d, ColumnDataSource, NumeralTickFormatter, Label)
from bokeh.plotting import gmap, figure
from bokeh.models.glyphs import Patch, Circle
import pandas as pd


def get_key(path = './googlemap_key.conf'):
    with open(path, 'r') as f:
        key = f.readline()

    return key


def plot_map(zipcode, df):
    search = SearchEngine(simple_zipcode=False)
    zipcode_data = search.by_zipcode(zipcode)
    zip_dict = zipcode_data.to_dict()

    zip_lat = zip_dict['lat']
    zip_lng = zip_dict['lng']

    zip_poly = zip_dict['polygon']
    zip_poly_lat = [poly[1] for poly in zip_poly]
    zip_poly_lng = [poly[0] for poly in zip_poly]

    radius = zip_dict['radius_in_miles']
    if radius < 1:
        p_zoom = 14
    elif radius < 10:
        p_zoom = 12
    else:
        p_zoom = 11

    map_options = GMapOptions(lat=zip_lat, lng=zip_lng, map_type='roadmap', zoom=p_zoom)
    plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)

    key = get_key()

    plot.api_key = key

    source_zip = ColumnDataSource(
        data=dict(
            lat=zip_poly_lat,
            lon=zip_poly_lng))

    patch = Patch(x='lon', y='lat', fill_color="blue", fill_alpha=0.08)
    plot.add_glyph(source_zip, patch)

    plot.add_tools(PanTool(), WheelZoomTool(), BoxZoomTool())

    source_houses = ColumnDataSource(
    data=dict(
        lat=df['latitude'].tolist(),
        lon=df['longitude'].tolist(),
        address=df['address'].tolist(),
        city=df['city'].tolist(),
        state=df['state'].tolist(),
        price=df['price'].tolist()))

    circle = Circle(x='lon', y='lat', size=8, fill_color='black', fill_alpha=0.8, line_color=None)
    plot.add_glyph(source_houses, circle)

    TOOLTIPS = [
        ('Price', '$@price{,}'),
        ('Address', '@address'),
        ('City', '@city'),
        ('State', '@state')]

    plot.add_tools(HoverTool(mode = 'mouse', tooltips=TOOLTIPS))

    return plot


def plot_historical(df):
    if (len(df) > 0):
        source_historical = ColumnDataSource(df)

        hover = HoverTool(mode='mouse',
            tooltips=[
                ('Date', "@Date{%F}"),
                ('Price', "$@Value{,}")],
            formatters={
                'Date'  : 'datetime',
                'Price' : 'printf'})

        TOOLS = 'pan,wheel_zoom,box_zoom,reset,save'

        p = figure(x_axis_type="datetime", tools=[TOOLS, hover], plot_width=700, plot_height=200)
        p.line('Date', 'Value', line_width = 3, source = source_historical)

        p.yaxis[0].formatter = NumeralTickFormatter(format='$0,0')
        p.xaxis.major_label_text_font_size = '15pt'
        p.yaxis.major_label_text_font_size = '15pt'
    else:
        p = figure(plot_width=700, plot_height=200)
        error_label = Label(x=100, y=60, x_units='screen', y_units='screen',
                            text='Data Unavailable', text_font_size='40pt')
        p.add_layout(error_label)

    return p


def nice_float(x):
    return '${0:,.0f}'.format(x)


def create_table(dfz, dft, dfr):
    source_list = ['Zillow', 'Trulia', 'Realtor']

    if (len(dfr) > 0):
        realtor_list = [dfr['Total Listing Count'].values[0],
                        nice_float(dfr['Avg Listing Price'].values[0]),
                        nice_float(dfr['Median Listing Price'].values[0])]
    else:
        realtor_list = [' ', ' ', ' ']

    number_list = [str(dfz.shape[0]),
                   str(dft.shape[0]),
                   realtor_list[0]]

    mean_list = [nice_float(dfz['price'].mean()),
                 nice_float(dft['price'].mean()),
                 realtor_list[1]]


    median_list = [nice_float(dfz['price'].median()),
                   nice_float(dft['price'].median()),
                   realtor_list[2]]

    max_list = [nice_float(dfz['price'].max()),
                nice_float(dft['price'].max()),
                ' ']

    min_list = [nice_float(dfz['price'].min()),
                nice_float(dft['price'].min()),
                ' ']

    data = {
        'No. of Listings': number_list,
        'Average Listing Price': mean_list,
        'Median Listing Price' : median_list,
        'Maximum Listing Price': max_list,
        'Minimum Listing Price': min_list}

    df = pd.DataFrame(data, index=source_list)

    return df
