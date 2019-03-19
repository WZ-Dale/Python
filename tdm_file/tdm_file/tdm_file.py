import numpy as np

if not path is None:
    with file(os.path.join(outpath,ctime + '_synopticscale_front_location.dat'), 'w') as outfile:
        for slice_2d in path:
            np.savetxt(outfile, slice_2d,fmt='%0.8f')
    with file(os.path.join(outpath,ctime + '_synopticscale_front_type.dat'),'w')as outfile:
        for slice_2d in smask:
            np.savetxt(outfile,slice_2d,fmt='%8d')
    np.savetxt(os.path.join(outpath,ctime + '_synopticscale_flont_influence_area.dat'), np.transpose(frontregion), fmt='%8d', delimiter=' ')
