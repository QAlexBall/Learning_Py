from ..nms.py_nms import py_nms

print(py_nms)


def nms(dets, thresh, force_cpu=False):
    if dets.shape[0] == 0:
        return []
