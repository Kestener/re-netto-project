#%%
from supermarket_start import Supermarket
from class_plot_market import PlotMarket

#%%
re_netto = Supermarket(brand = 're-netto_2', open='07:00', closed = '22:00')

if __name__ == "__main__":
    
    while re_netto.is_open():
        re_netto.add_new_customers()
        re_netto.print_customers(to_csv=True)        
        re_netto.next_minute()
        re_netto.remove_exitsting_customers()

#%%
plot = PlotMarket(frames=1)
plot.create_plots()
#plot.create_giph()
# %%
#plot = PlotMarket(frames=1)
#plot.create_giph()
# %%
