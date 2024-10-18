import numpy as np
import xarray as xr

## https://www.statology.org/pandas-3d-dataframe/

#make this example reproducible
np.random.seed(1)

#create 3D dataset
xarray_3d = xr.Dataset(
    {"product_A": (("year", "quarter"), np.random.randn(2, 4))},
    coords={
        "year": [2021, 2022],
        "quarter": ["Q1", "Q2", "Q3", "Q4"],
        "product_B": ("year", np.random.randn(2)),
        "product_C": 50,
    },
)

'''
<xarray.Dataset> Size: 136B
Dimensions:    (year: 2, quarter: 4)
Coordinates:
  * year       (year) int64 16B 2021 2022
  * quarter    (quarter) <U2 32B 'Q1' 'Q2' 'Q3' 'Q4'
    product_B  (year) float64 16B 0.319 -0.2494
    product_C  int64 8B 50
Data variables:
    product_A  (year, quarter) float64 64B 1.624 -0.6118 ... 1.745 -0.7612
'''    


#view 3D dataset
print(xarray_3d)


df_3d = xarray_3d.to_dataframe()

#view 3D DataFrame
print(df_3d)

'''
              product_A  product_B  product_C
year quarter                                 
2021 Q1        1.624345   0.319039         50
     Q2       -0.611756   0.319039         50
     Q3       -0.528172   0.319039         50
     Q4       -1.072969   0.319039         50
2022 Q1        0.865408  -0.249370         50
     Q2       -2.301539  -0.249370         50
     Q3        1.744812  -0.249370         50
     Q4       -0.761207  -0.249370         50
'''