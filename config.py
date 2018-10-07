import os

NEBULOUSLABS_GIT_BASEURL = 'https://gitlab.com/NebulousLabs/'
SIACOINCLASSIC_GIT_BASEURL = 'git@github.com:SiacoinClassic/'

REPOSITORYS_DIR = os.path.join(os.getcwd(), 'repositorys')

DEPENDENCIES = {
    'demotemutex',
    'fastrand',
    'merkletree',
    'bolt',
    'entropy-mnemonics',
    'errors',
    'go-upnp',
    'ratelimit',
    'threadgroup',
    'writeaheadlog',
    'glyphcheck'
}
