import pymel.core as pm

def main():
    pm.makeIdentity(apply = True, t = 1, r = 1, s = 1, pn = 1)
    pm.makeIdentity(apply = False, t = 1, r = 1, s = 1)
    pm.delete(ch = True)