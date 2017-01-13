# PSF Interpolation Tests

> Author: **Samuel Farrens**

> Year: **2017**

> Version: **1.0**

> Email: **[samuel.farrens@gmail.com](mailto:samuel.farrens@gmail.com)**

## Q Metric Script

The file `script.py` reads a stack of interpolated PSF images and a stack of true PSF images (both in numpy binary format) and outputs the Q value for the whole sample.

To execute the code run

```bash
$ ./script.py -i INTERPOLATED_PSF_FILE.npy -t TRUE_PSF_FILE.npy
```

This script will output the Q value in the terminal.

### Q Metric

The metric used was derived from that of [Mandelbaum et al. (2015)](https://arxiv.org/pdf/1412.1825v2.pdf) by T. Kuntzer.
