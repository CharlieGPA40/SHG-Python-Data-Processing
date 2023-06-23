from Stoner import Data
import Stoner
import numpy as np

vsm_data = Stoner.Data.load("50K.DAT", filetype=Stoner.formats.instruments.QDFile)
temp = vsm_data.column(['Temperature (K)',0])
vsm_data.setas(x="Magnetic Field (Oe)" ,y="Moment (emu)")
vsm_data.plot(fmt="r.")
vsm_data= vsm_data.del_column(vsm_data.setas.not_set)
temp = np.ceil(temp[0][0])
vsm_data=Stoner.formats.generic.CSVFile(vsm_data)
vsm_data.save('{}.csv'.format(temp))
