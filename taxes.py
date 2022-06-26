from pandas import DataFrame

# These values are valid only for CYL
# IRPF Sections

sections_irpf = DataFrame()
sections_irpf['base_liquidable_desde'] = [0,12450,20200,35200,53407,60000,300000]
sections_irpf['base_liquidable_hasta'] = [12450,20200,34000,53407,60000,300000,999999999]
sections_irpf['tipo_estatal'] = [0.095, 0.12, 0.14, 0.185, 0.185, 0.225, 0.235]
sections_irpf['tipo_autonomico'] = [0.095, 0.12, 0.14, 0.185, 0.215, 0.215, 0.215]
sections_irpf['tipo_total'] = sections_irpf['tipo_estatal'] + sections_irpf['tipo_autonomico']

# IVA

iva = 0.21

# Min without taxes

minimum_contributor = 5500

# Other taxes

ss = 0.05
unemployment = 0.0155
training = 0.001

# Other cases for deduct taxes

child_less_3_years = 2800
child_1_less_25_years = 2400
child_2_less_25_years = 2700
child_3_less_25_years = 4000
child_4_or_more_less_25_years = 4500