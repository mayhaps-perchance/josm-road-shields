APPNAME = 'josm-road-shields'
VERSION = '0.2.0'

top = '.'
out = 'build'

def configure(ctx):
    ctx.find_program('7z', var='7Z')


def build(bld):
    bld(rule='${7Z} a ${TGT} *.mapcss', target=f'{APPNAME}.zip')
