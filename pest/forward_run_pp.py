import os
from datetime import datetime
import numpy as np
import pandas as pd
import pyemu

bak_dir = "bak"
out_dir = "ref"
folder = 'pilot_points'
# if not os.path.exists(out_dir):
# 	os.mkdir(out_dir)
def prepare():

	# # apply drain conductance parameters
	# drn_df = pd.read_csv("drain_mlt.dat",delim_whitespace=True,header=None,names=["name","cond"])
	# drn_df.index = drn_df.name.apply(lambda x: (int(x[-5:-3])+1,int(x[-2:])+1))
	# drn_files = [f for f in os.listdir(bak_dir) if "drn" in f.lower()]
	# for drn_file in drn_files:
	# 	df = pd.read_csv(os.path.join(bak_dir,drn_file),header=None,
	# 		names=["l","r","c","stage","cond"],delim_whitespace=True)
	# 	df.index = df.apply(lambda x: (x.r,x.c),axis=1)
	#
	# 	df.loc[:,"cond"] = drn_df.cond
	# 	df.loc[:,["l","r","c","stage","cond"]].to_csv(os.path.join(out_dir,drn_file),
	# 		sep=' ',index=False,header=False)

	# apply pilot point parameters as multipliers
	pp_files = ["hk1pp.dat","hk2pp.dat","hk3pp.dat",
				"sy1pp.dat","sy2pp.dat",
				"ss1pp.dat", "ss2pp.dat", "ss3pp.dat"]
	# prefixes = ["hk","sy","ss"]
	# for pp_file,prefix in zip(pp_files,prefixes):
	for pp_file in pp_files:
		lay = ''.join(filter(str.isdigit, pp_file.strip('.dat')))
		facfile = f"pp{lay}.fac"
		arr = pyemu.utils.geostats.fac2real(pp_file=os.path.join(folder,pp_file),
			factors_file=os.path.join(folder,facfile),out_file=None)
		# base_arr_files = [f for f in os.listdir(bak_dir) if prefix in f.lower()]
		# base_arrs = [np.loadtxt(os.path.join(bak_dir,f)) for f in base_arr_files]
		fname = pp_file.replace('pp.dat', '.txt')
		np.savetxt(os.path.join(folder,fname),arr)
		# for fname in base_arr_files:
		# 	# base_arr = np.loadtxt(os.path.join(bak_dir,fname))
		# 	# base_arr *= arr
		# 	np.savetxt(os.path.join(out_dir,fname),arr)
		print(f'done creating {folder}\\{fname} with {folder}\\{pp_file}. facfile = {facfile}')

def run():

	os.system("MODFLOW-NWT_64.exe RRMF.nam")

def post_process():
	pass




if __name__ == "__main__":
	prepare()
	run()
	# run()
	# post_process()
