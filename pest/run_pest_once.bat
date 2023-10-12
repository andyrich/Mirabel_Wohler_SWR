rem cd ..
rem pestpp-opt.exe reg_pest.pst /H :4004 /j
start powershell.exe -ExecutionPolicy bypass
call C:\Users\arich\AppData\Local\mambaforge\condabin\conda_hook.bat
call conda activate gis_py_8
rem pest++.exe reg_pest.pst 
pest++.exe ies.pst